layout: page
title: "Submission information"
permalink: /submit/

# How to submit

In order to keep it simple, we ask you to write an e-mail to <pheinisch@techfak.uni-bielefeld.de> with <opitz@cl.uni-heidelberg.de> in Cc. We ask to contribute exactly one approach per e-mail. If you have developed several approaches/ systems, write multiple e-mails, one e-mail for one approach/ system.

We remember our terms:

> There are up to **5** submissions from different approaches (systems) allowed per team and per subtask. The submission must be submitted via e-mail. You are allowed to withdraw your submission at anytime until the final deadline (also via e-mail).

You are free to participate only in one subtask or both.

**Please read the following e-mail-instructions carefully since we can only accept e-mails following the given instructions:**

## How to structure a submission e-mail

You have to structure your e-mail in the following way:

### Subject of the e-mail

``[ArgMining22-SharedTask-Subtask`` _(A or B)_ ``]`` _team name_ ``(``number of appraoch``)``

(the _number of approach_ is an incrementing number starting with 1 to identify this submission. If you just submit one approach/ submission (per subtask), it's just ``[ArgMining22-SharedTask-Subtask `` _(A or B)_ ``]`` _team name_ ``(1)``. However, let's say you submit your already third approach for subtask A, the subject should be ``[ArgMining22-SharedTask-Subtask A]`` _team name_ ``(3)``.)

### Text body of the e-mail

#### 1. General information

Please provide a list of information containing the following information in the following order:

1. The name of your team (if you submit without having a team, you can write your name here)
2. All team members' full names and e-mail addresses, separated by a comma. The first name in the list should be the main contact person
3. (optional: the affiliation of each team member)
4. the name/ short title of your approach

#### 2. Abstract describing your approach/ system

Please describe in 5-10 sentences your approach/ system.

#### 3. Additional [training] data used?

If you used additional [training] data (data differing from [the given training data](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskA_train.csv) and/or [evaluation data](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/TaskA_dev.csv)), please descibe here:

- the source(s) of the additional data (links). If the data was artificially generated, please describe (shortly) the generation process instead.
- how you used the data for this task

### Appendix

Only **1** single **csv** file (please ensure an _uft-8_-encoding)! Don't use an archive file (hence, no **.zip** files)!

The **csv** file should contain the predictions for the test data and should be structured as follows:

#### In the case of Subtask A

``topic, Premise, Conclusion, predicted validity, predicted novelty``

The predicted validity/ novelty has to be either ``-1`` (not valid/ novel) or ``1`` (valid/ novel). No floating numbers!

#### In the case of Subtask B

``topic, Premise, Conclusion 1, Conclusion 2, predicted validity, predicted novelty``

The predicted validity/ novelty has to be either ``-1`` (conclusion 1 outperforms) or ``0`` (tie) or ``1`` (conclusion 2 outperforms). No floating numbers!
