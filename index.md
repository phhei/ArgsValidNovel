# Shared task on predicting validity and novelty of arguments

In recent years, there has been increased interest in understanding how to assess the quality of arguments systematically. [Wachsmuth et al.](https://aclanthology.org/E17-1017) proposed a framework for quality assessment consisting of the following top dimensions: logic, rhetoric, and dialectic. Regarding the dimension of logic, there has been some work to assess the quality of an argument or conclusion automatically.

Recently, there has also been interest in generation conclusions or arguments. In order to guide the process of automatically generating a conclusion, our assumption is that we might need metrics that can be automatically computed to estimate the suitability and quality  of a certain conclusion. Two important metrics/objectives are that the conclusion is **valid**, that is, that the conclusion “follows” from the premise. At the same time, it is easy to produce conclusions that “follow” from the premise by repeating (parts of) the premise in the conclusion, trivially generating a “valid” but vacuous conclusion. In this sense, it is important to assess whether conclusions/arguments are not only valid, but also **novel**.

We define **validity** as requiring the existence of logical inferences that link the premise to the conclusion. In contrast, **novelty** requires the presence of novel _premise-related_ content and/or combination of the content in the premises in a way that goes beyond what is stated in the premise. Hence, a conclusion that is valid but not novel could be a repetition, a paraphrase or a summary of the premise, and only a novel conclusion offers a piece of information that extends what is already covered by the premise – whether it supports or contests the premise.

---

## Tasks

We divide the task of Validity-Novelty-Prediction into two subtasks.

1. Task A: The first task consists of a binary classification task along the dimensions of novelty and validity, classifying a conclusion as being valid/novel or not given a textual premise. 
1. Task B: The second subtask will consist in classifying the degree to which a conclusion is valid / novel as a regression task. 

Participants can choose whether to address Task A or Task B, or both.

### Subtask A: binary novelty-validity-classification

Given a premise and a conclusion in natural language, the task is to predict:

1. whether the given conclusion is valid with respect to the premise
1. whether the given conclusion is novel with respect to the premise

Hence, we expect two binary decisions as output.

#### Example: Wind energy

Premise: Unlike many other forms of energy generation, wind generators do not require the cycling of water for cooling or as the medium for transferring heat energy into usable electric energy (such as with coal or gas).	

| **Conclusion** | **Validity** | **Novelty** |
|------------|----------|---------|
| Wind energy does not require transferring heat into electricity. | no | no |
| Wind energy does not require water as a medium | yes | no |
| Wind energy requires very little energy | no | yes |
| Wind energy has several advantages in comparison to conventional energies. | yes | yes |

#### Datasets & Evaluation

### Subtask B: recognizing relative validity / novelty

Given a premise and two conclusions A and B in natural language, the task is to predict:

1. whether conclusion A is better than conclusion B in terms of validity 
1. whether conclusion A is better than  conclusion B in terms of novelty

There are three possible labels for this task: better/worse/tie.

#### Example: Wind energy

Premise: Unlike many other forms of energy generation, wind generators do not require the cycling of water for cooling or as the medium for transferring heat energy into usable electric energy (such as with coal or gas).	

| **Conclusion A** | **Conclusion B** | **Validity** | **Novelty** |
|--------------|--------------|----------|---------|
| Wind energy does not require transferring heat into electricity. |  Wind energy does not require a cooling system. | A = B | A < B |
| Wind energy requires no heating/cooling. | Wind energy does not require a cooling system. | A < B | A = B |

#### Datasets & Evaluation

---

## Orgainisation & Submission

_coming soon_

### Timeline

- End of Mai: release ot task description and data on a website for the task
- June-Beginning of August: Teams work on their solutions
- Beginning of August: Test data without labels is released
- Mid of August: Final submission of teams of results on test data
- End of August: Publication of overall results of the task
- Mid-September: Paper for proceedings with task description ready

### Terms and Conditions

By participating in this task you agree to these terms and conditions. If, however, one or more of this conditions is a concern for you, send us an email and we will consider if an exception can be made.

- By submitting results to this competition, you consent to the public release of your scores at this website and at ArgMining-2022 workshop and in the associated proceedings, at the task organizers' discretion. Scores may include, but are not limited to, automatic and manual quantitative judgements, qualitative judgements, and such other metrics as the task organizers see fit. You accept that the ultimate decision of metric choice and score value is that of the task organizers.
- You further agree that the task organizers are under no obligation to release scores and that scores may be withheld if it is the task organizers' judgement that the submission was incomplete, erroneous, deceptive, or violated the letter or spirit of the competition's rules. Inclusion of a submission's scores is not an endorsement of a team or individual's submission, system, or science.
- A participant can be involved in exactly one team (no more). If there are reasons why it makes sense for you to be on more than one team, then email us before the evaluation period begins. In special circumstances this may be allowed.
  - There is only submission allowed per team and per subtask. The submission must be uploaded in the provided website. You are allowed to overwrite your final submission anytime until the final deadline
- Once the competition is over, we will release the gold labels and you will be able to determine results on various system variants you may have developed. We encourage you to report results on all of your systems (or system variants) in the system-description paper. However, we will ask you to clearly indicate the result of your official submission.
  - We will make the final submissions of the teams public at some point after the evaluation period.
  - The organizers and their affiliated institutions makes no warranties regarding the datasets provided, including but not limited to being correct or complete. They cannot be held liable for providing access to the datasets or the usage of the datasets.
  - The dataset should only be used for scientific or research purposes. Any other use is explicitly prohibited.
  - The datasets must not be redistributed or shared in part or full with any third party. Redirect interested parties to this website.

## Results

_coming soon_

## Task Organizers

- Bielefeld University
  - **Philipp Heinisch: pheinisch@techfak.uni-bielefeld.de**
  - Philipp Cimiano: cimiano@cit-ec.uni-bielefeld.de
- Heidelberg University
  - Anette Frank: frank@cl.uni-heidelberg.de
  - Juri Opitz: opitz@cl.uni-heidelberg.de
