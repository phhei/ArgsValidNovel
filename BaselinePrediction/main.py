from pathlib import Path
from typing import Literal, Optional

import torch
from torch.utils.data import Dataset
import transformers
from pandas import DataFrame, read_csv
from const import TOPIC_SPECIAL_TOKEN, PREMISE_SPECIAL_TOKEN, CONCLUSION1_SPECIAL_TOKEN, CONCLUSION2_SPECIAL_TOKEN

import argparse


class ClassificationDataset(Dataset):
    def __init__(self, f_subtask: Literal["A", "B"], f_tokenizer: transformers.PreTrainedTokenizer,
                 f_data: DataFrame, f_max_length: int, f_y: Optional[Literal["Validity", "Novelty"]]):
        if f_subtask == "A":
            self.x = f_tokenizer(
                text=["{}: {}".format(row["topic"], row["Premise"]) for _, row in f_data.iterrows()],
                text_pair=[row["Conclusion"] for _, row in f_data.iterrows()],
                add_special_tokens=True,
                truncation="longest_first",
                padding="max_length",
                max_length=f_max_length,
                return_tensors="pt"
            )
            self.y = None if f_y is None else torch.LongTensor([min(1, y + 1) for y in f_data[f_y]])
        else:
            self.x = f_tokenizer(
                text=["{}{}{}{}{}{}{}{}".format(TOPIC_SPECIAL_TOKEN,
                                                row["topic"],
                                                PREMISE_SPECIAL_TOKEN,
                                                row["Premise"],
                                                CONCLUSION1_SPECIAL_TOKEN,
                                                row["Conclusion 1"],
                                                CONCLUSION2_SPECIAL_TOKEN,
                                                row["Conclusion 2"]) for _, row in f_data.iterrows()],
                add_special_tokens=True,
                truncation="longest_first",
                padding="max_length",
                max_length=f_max_length,
                return_tensors="pt",
                verbose=False
            )
            self.y = None if f_y is None else torch.LongTensor([y+1 for y in f_data[f_y]])

    def __getitem__(self, index):
        ret = {k: v[index] for k, v in self.x.items()}
        if self.y is not None:
            ret.update({"labels": self.y[index]})
        return ret

    def __len__(self) -> int:
        return len(self.x["input_ids"])


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog="Baseline for solving either subtask A or subtask B",
        description="The baseline uses pretrained language models (RoBERTa-base), fine-tuned separately on validity "
                    "and novelty (without further training data/ techniques)",
        allow_abbrev=True
    )
    arg_parser.add_argument("-t", "--task", action="store", type=str, default="A", choices=["A", "B"],
                            help="Subtask A (binary novelty-validity-classification) or Subtask B "
                                 "(recognizing relative validity / novelty)?")
    arg_parser.add_argument("-l", "--max_length", action="store", type=int, default=200,
                            help="The maximum length of each input token sequence")
    arg_parser.add_argument("-e", "--epochs", action="store", type=int, default=3, help="The number of epochs")

    args = arg_parser.parse_args()

    tokenizer = transformers.RobertaTokenizer.from_pretrained("roberta-base")
    test_df = read_csv("../Task{}_test-without-labels.csv".format(args.task), encoding="utf8")
    test_dataset = ClassificationDataset(f_subtask=args.task,
                                         f_tokenizer=tokenizer,
                                         f_data=test_df,
                                         f_max_length=args.max_length,
                                         f_y=None)

    for aspect in ["Validity", "Novelty"]:
        model = transformers.RobertaForSequenceClassification.from_pretrained("roberta-base",
                                                                              num_labels=2+int(args.task == "B"))
        if args.task == "B":
            num_added = tokenizer.add_special_tokens(special_tokens_dict={
                "additional_special_tokens": [TOPIC_SPECIAL_TOKEN, PREMISE_SPECIAL_TOKEN,
                                              CONCLUSION1_SPECIAL_TOKEN, CONCLUSION2_SPECIAL_TOKEN]
            })
            model.resize_token_embeddings(new_num_tokens=len(tokenizer.get_vocab()))

        train_df = read_csv("../Task{}_train.csv".format(args.task), encoding="utf8")
        if args.task == "A":
            train_df.drop(index=[k for k, v in train_df.iterrows() if v[aspect] == 0], inplace=True)
        train_dataset = ClassificationDataset(f_subtask=args.task,
                                              f_tokenizer=tokenizer,
                                              f_data=train_df,
                                              f_max_length=args.max_length,
                                              f_y=aspect)
        dev_df = read_csv("../Task{}_dev.csv".format(args.task), encoding="utf8")
        if args.task == "A":
            dev_df.drop(index=[k for k, v in train_df.iterrows() if v[aspect] == 0], inplace=True)
        dev_dataset = ClassificationDataset(f_subtask=args.task,
                                            f_tokenizer=tokenizer,
                                            f_data=dev_df,
                                            f_max_length=args.max_length,
                                            f_y=aspect)

        trainer = transformers.Trainer(
            model=model,
            train_dataset=train_dataset,
            eval_dataset=dev_dataset,
            args=transformers.TrainingArguments(
                output_dir=".out/roberta-base/subtask {}/{}-{}".format(args.task, aspect, args.epochs),
                overwrite_output_dir=False,
                per_device_train_batch_size=8,
                per_device_eval_batch_size=16,
                num_train_epochs=args.epochs,
                warmup_steps=100,
                evaluation_strategy="epoch",
                save_strategy="epoch",
                save_total_limit=args.epochs-1,
                load_best_model_at_end=True,
                metric_for_best_model="eval_loss",
                greater_is_better=False
            )
        )

        trainer.train()

        trainer.model.eval()
        trainer.save_model(output_dir=".out/roberta-base/subtask {}/{}-{}".format(args.task, aspect, args.epochs))

        all_predictions = []
        prediction_mapper = {0: -1, 1: 1} if args.task == "A" else {0: -1, 1: 0, 2: 1}
        for i in range(0, len(test_dataset), 16):
            input_ids = torch.stack([test_dataset[j]["input_ids"] for j in range(i, min(i+16, len(test_dataset)))],
                                    dim=0)
            attention_mask = torch.stack([test_dataset[j]["attention_mask"]
                                          for j in range(i, min(i+16, len(test_dataset)))],
                                         dim=0)
            predictions = trainer.model(input_ids=input_ids, attention_mask=attention_mask)

            all_predictions.extend([prediction_mapper[v] for v in torch.argmax(predictions.logits, dim=1).tolist()])

        test_df["predicted {}".format(aspect.lower())] = all_predictions

    Path(".out/roberta-base/subtask {}/single-task-combined {} epochs".format(args.task, args.epochs)).mkdir(
        exist_ok=True, parents=True
    )
    test_df.to_csv(
        path_or_buf=".out/roberta-base/subtask {}/single-task-combined {} epochs/test-with-predicted-labels.csv".format(
            args.task, args.epochs
        ),
        encoding="utf8",
        index=False
    )