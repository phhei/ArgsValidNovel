# Shared task on predicting validity and novelty of arguments

In recent years, there has been increased interest in understanding how to assess the quality of arguments systematically. [Wachsmuth et al.](https://aclanthology.org/E17-1017) proposed a framework for quality assessment consisting of the following top dimensions: logic, rhetoric, and dialectic. Regarding the dimension of logic, there has been some work to assess the quality of an argument or conclusion automatically.

Recently, there has also been interest in the generation of conclusions or arguments. In order to guide the process of automatically generating a conclusion, our assumption is that we might need metrics that can be automatically computed to estimate the suitability and quality  of a certain conclusion. Two important metrics/objectives are that the conclusion is **valid**, that is, that the conclusion “follows” from the premise. At the same time, it is easy to produce conclusions that “follow” from the premise by repeating (parts of) the premise in the conclusion, trivially generating a “valid” but vacuous conclusion. In this sense, it is important to assess whether conclusions/arguments are not only valid, but also **novel**.

We define **validity** as requiring the existence of logical inferences that link the premise to the conclusion. In contrast, **novelty** requires the presence of novel _premise-related_ content and/or combination of the content in the premises in a way that goes beyond what is stated in the premise. Hence, a conclusion that is valid but not novel could be a repetition, a paraphrase or a summary of the premise, and only a novel conclusion offers a piece of information that extends what is already covered by the premise – whether it supports or contests the premise.

---

## Tasks

We divide the task of Validity-Novelty-Prediction into two subtasks.

1. Task A: The first task consists of a binary classification task along the dimensions of novelty and validity, classifying a conclusion as being valid/novel or not given a textual premise. 
1. Task B: The second subtask will consist a comparinson of two conclusions in terms of validty / novelty 

Participants can choose whether to address Task A or Task B, or both.

### Subtask A: binary novelty-validity-classification

Given a premise and a conclusion in natural language, the task is to predict:

1. whether the given conclusion is valid with respect to the premise
1. whether the given conclusion is novel with respect to the premise

Hence, we expect two binary decisions as output.

#### Example: Vegetarism

Premise: The notion of man's dominion over animals need not be thought of as a blank check for man to exploit animals. Indeed, it may be appropriate to connect the notion of "dominion" to stewardship" over animals. Yet, humans can be good stewards of animals while continuing to eat them. It is merely necessary that humans maintain balance, order, and sustainability in the animal kingdom. But, again, this does not require the abandonment of meat-eating.

| **Conclusion** | **Validity** | **Novelty** |
|------------|----------|---------|
| Two-party systems are more stable | no | no |
| Man's "dominion" over animals does not imply abandoning meat. | yes | no |
| The idea of "domiminism" is unnecessary. | no | yes |
| Dominion over animals can and should be used responsibly | yes | yes |

#### Datasets & Evaluation

Please read the [Data Description](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/data-description.md) beforehand.

- Train: [here](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskA_train.csv)
  - you're allowed to extend the train set with further (synthetic) samples. However, if you do that, you have to describe/ provide the algorithm which extends the training set. This algorithm must be automatically executable without any human interaction (hence, without further manual annotation/ manual user feedback)
- Dev: [here](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskA_dev.csv)
- Test: [without labels](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskA_test-without-labels.csv) => [submit](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/submission.md)

**Evaluation:** we consider the _f1_macro_-score calculated by the Python-method [here](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/eval-metric.py). The (predicted) values for validity and novelty can be continuous. In any case, the values for validity and novelty must be in the range of 0 (aspect not fulfilled) to 1 (aspect fulfilled).

### Subtask B: recognizing relative validity / novelty

Given a premise and two conclusions A and B in natural language, the task is to predict:

1. whether conclusion A is better than conclusion B in terms of validity 
1. whether conclusion A is better than  conclusion B in terms of novelty

There are three possible labels for this task: better/worse/tie.

#### Example: US offshore oil drilling	

Premise: These large ships release significant pollution into the oceans, and carry some risk of hitting the shore, and causing a spill.

| **Conclusion A** | **Conclusion B** | **Validity** | **Novelty** |
|--------------|--------------|----------|---------|
| Transporting offshore oil to shores by ship has environmental costs. | Need for water does not qualify water as a right. | A > B | A > B |
| Oil drilling releases significant pollutants into the ocean | Transporting offshore oil to shores by ship has environmental costs. | A = B | A < B |

#### Datasets & Evaluation

Please read the [Data Description](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/data-description.md) beforehand.

- Train: [here](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskB_train.csv)
  - you're allowed to extend the train set with further (synthetic) samples. However, if you do that, you have to describe/ provide the algorithm which extends the training set. This algorithm must be automatically executable without any human interaction (hence, without further manual annotation/ manual user feedback)
- Dev: [here](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskB_dev.csv)
- Test: [without labels](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskB_test-without-labels.csv) => [submit](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/submission.md)

**Evaluation:** We require follwing format for each instance for each aspect (validity/ novelty).

- -1: A>B: Conclusion A is more (valid/ novel)
- 0: A=B: Conclusion A and B are equalliy valid/ novel
- 1: A<B: Conclusion B is more  (valid/ novel)

We consider the _f1_macro_-score averaging the _f1_-score of all 3x3 classes ((-1, -1), (-1, 0), (-1, 1), (0, -1), ..., (1, 1)).

---

## Orgainisation & Submission

_coming soon_

### Timeline

- 01.08.22: Test data without labels is released
- 05.08.22: Final submission of team results on test data
- (until) 12.08.22: Publication of overall results of the task
- 05.09.22: Paper for proceedings with task description ready

### Terms and Conditions

By participating in this task you agree to these terms and conditions. If, however, one or more of this conditions is a concern for you, send us an email and we will consider if an exception can be made.

- By submitting results to this competition, you consent to the public release of your scores at this website and at ArgMining-2022 workshop and in the associated proceedings, at the task organizers' discretion. Scores may include, but are not limited to, automatic and manual quantitative judgements, qualitative judgements, and such other metrics as the task organizers see fit. You accept that the ultimate decision of metric choice and score value is that of the task organizers.
- You further agree that the task organizers are under no obligation to release scores and that scores may be withheld if it is the task organizers' judgement that the submission was incomplete, erroneous, deceptive, or violated the letter or spirit of the competition's rules. Inclusion of a submission's scores is not an endorsement of a team or individual's submission, system, or science.
- A participant can be involved in one team. Participating in more than one team is not recommended, but not forbidden (if the person does not apply the same approach in different teams)
  - There are up to 5 submissions from different approaches (systems) allowed per team and per subtask. [The submission must be submitted via e-mail](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/submission.md). You are allowed to withdraw your submission at anytime until the final deadline (also via e-mail).
  - You must not use any data from the development split as training instances. You must not use any test instance in the training of the model (also not indirectly for model selection). Approaches that violate this data separation are disqualified.
- Once the competition is over, we will release the gold labels and you will be able to determine results on various system variants you may have developed. We encourage you to report results on all of your systems (or system variants) in the system-description paper. However, we will ask you to clearly indicate the result of your official submission.
  - We will make the final submissions of the teams public at some point after the evaluation period.
  - The organizers and their affiliated institutions makes no warranties regarding the datasets provided, including but not limited to being correct or complete. They cannot be held liable for providing access to the datasets or the usage of the datasets.
  - The dataset should only be used for scientific or research purposes. Any other use is explicitly prohibited.
  - The datasets must not be redistributed or shared in part or full with any third party. Redirect interested parties to this website.

## Results

_coming soon_

## Task Organizers

Newsletter/ Google-Group: <https://groups.google.com/g/argmining2022-shared-task>

- Bielefeld University
  - Philipp Heinisch: pheinisch@techfak.uni-bielefeld.de _(main organizer + contact person)_
  - Philipp Cimiano: cimiano@cit-ec.uni-bielefeld.de
- Heidelberg University
  - Anette Frank: frank@cl.uni-heidelberg.de
  - Juri Opitz: opitz@cl.uni-heidelberg.de
