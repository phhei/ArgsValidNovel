from typing import Tuple

import pandas
from pathlib import Path
from loguru import logger
from pprint import pformat
from itertools import product

import argparse
import numpy

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("task", choices=["A", "B"], type=str)
    argument_parser.add_argument("reference_file", type=Path, action="store",
                                 help="The file with the ground truth labels")
    argument_parser.add_argument("prediction_file", type=Path, action="store",
                                 help="The file with the ground truth labels")

    args = argument_parser.parse_args()

    logger.info("Reference: {} <> Predictions: {}", args.reference_file, args.prediction_file)

    classes = [-1, 1] if args.task == "A" else [-1, 0, 1]

    df_reference = pandas.read_csv(str(args.reference_file), encoding="utf8")
    df_predicted = pandas.read_csv(str(args.prediction_file), encoding="utf8")

    keys = ["topic", "Premise", "Conclusion"] if args.task == "A" else \
        ["topic", "Premise", "Conclusion 1", "Conclusion 2"]
    joined_df = df_reference.set_index(keys).join(other=df_predicted.set_index(keys), how="inner")

    if len(joined_df) < (520 if args.task == "A" else 283):
        logger.warning("The prediction file was wrongly encoded/ composed, "
                       "collected only {} matches between reference and prediction", len(joined_df))
        joined_df = df_reference
        try:
            joined_df["predicted validity"] = df_reference["predicted validity"]
            joined_df["predicted novelty"] = df_reference["predicted novelty"]
        except Exception:
            logger.opt(exception=True).error("the prediction file ({}) is in the wrong format - reject!",
                                             args.prediction_file.absolute())

    df_checks = {
        "": joined_df,
        "in_topic": joined_df.drop(index=[rid for rid, row in joined_df.iterrows()
                                          if row["Topic-in-dev-split"] == "no"],
                                   inplace=False),
        "out_topic": joined_df.drop(index=[rid for rid, row in joined_df.iterrows()
                                           if row["Topic-in-dev-split"] == "yes"],
                                    inplace=False),
    }
    logger.info("Found following keys: {}",
                " / ".join(map(lambda kv: "{}: {} rows".format(kv[0], len(kv[1])), df_checks.items())))

    scores = dict()
    for aspect in ["Validity", "Novelty", ("Validity", "Novelty")]:
        for prefix, df in df_checks.items():
            if isinstance(aspect, Tuple):
                reference = numpy.stack(
                    [numpy.fromiter(iter=df[a], dtype=int) for a in aspect]
                )
                predicted = numpy.stack(
                    [numpy.fromiter(iter=df["predicted {}".format(a.lower())], dtype=int) for a in aspect]
                )
                aspect_key = "ValNov"
                considered_classes = list(product(classes, classes))
            else:
                reference = numpy.fromiter(iter=df[aspect], dtype=int)
                predicted = numpy.fromiter(iter=df["predicted {}".format(aspect.lower())], dtype=int)
                aspect_key = aspect
                considered_classes = classes
            for cls in considered_classes:
                if isinstance(cls, Tuple):
                    true_positives = numpy.sum(
                        numpy.multiply(*[numpy.where(reference[c_i] == c, 1, 0) * numpy.where(predicted[c_i] == c, 1, 0)
                                         for c_i, c in enumerate(cls)])
                    )
                    retrieved_elements = numpy.sum(
                        numpy.multiply(*[numpy.where(predicted[c_i] == c, 1, 0) for c_i, c in enumerate(cls)])
                    )
                    relevant_elements = numpy.sum(
                        numpy.multiply(*[numpy.where(reference[c_i] == c, 1, 0) for c_i, c in enumerate(cls)])
                    )
                else:
                    true_positives = numpy.sum(
                        numpy.where(reference == cls, 1, 0) * numpy.where(predicted == cls, 1, 0)
                    )
                    retrieved_elements = numpy.sum(numpy.where(predicted == cls, 1, 0))
                    relevant_elements = numpy.sum(numpy.where(reference == cls, 1, 0))
                scores["{}_{}_{}_precision".format(aspect_key, prefix, cls)] = true_positives/max(1., retrieved_elements)
                scores["{}_{}_{}_recall".format(aspect_key, prefix, cls)] = true_positives/max(1., relevant_elements)
                scores["{}_{}_{}_f1".format(aspect_key, prefix, cls)] = \
                    2*(scores["{}_{}_{}_precision".format(aspect_key, prefix, cls)] *
                        scores["{}_{}_{}_recall".format(aspect_key, prefix, cls)]) /\
                    max(1, scores["{}_{}_{}_precision".format(aspect_key, prefix, cls)] +
                    scores["{}_{}_{}_recall".format(aspect_key, prefix, cls)])
            scores["{}_{}_precision".format(aspect_key, prefix)] = \
                sum([scores["{}_{}_{}_precision".format(aspect_key, prefix, cls)] for cls in considered_classes])/len(considered_classes)
            scores["{}_{}_recall".format(aspect_key, prefix)] = \
                sum([scores["{}_{}_{}_recall".format(aspect_key, prefix, cls)] for cls in considered_classes]) / len(considered_classes)
            scores["{}_{}_f1".format(aspect_key, prefix)] = \
                sum([scores["{}_{}_{}_f1".format(aspect_key, prefix, cls)] for cls in considered_classes]) / len(considered_classes)

    logger.success("Calculated the scores: {}", pformat(object=scores, width=100, compact=False, sort_dicts=True))