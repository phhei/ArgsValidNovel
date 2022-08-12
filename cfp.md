# Call for papers (system description papers)

The shared task of the ArgMining 2022 invites the submission of short papers on system/ approach descriptions to achieve either [subtask A or B](https://phhei.github.io/ArgsValidNovel/). A submission of such a paper requires a [submission of test predictions according to our test production submission procedure](https://phhei.github.io/ArgsValidNovel/submission) beforehand. The deadline is already expired.

## Submission Information

By default, we accept one type of papers: short papers (2 to 4 pages + references + appendix (optional)). All papers will be treated equally in the workshop proceedings. The workshop follows ACL’s policies for submission, review, and citation. Moreover, authors are expected to adhere to the ethical code set out in the ACL Code of Ethics. Submissions that violate any of the policies will be rejected without review.

Please use the COLING 2022 style sheets for formatting your paper: https://coling2022.org/

Submission address: [email](mailto:argmining22_shared_task-organizers@cl.uni-heidelberg.de)

The Shared Task is running a small single-blind review process. The title section of your manuscript should contain author names, email addresses and affiliation status of all team members given in the previous submission of the test prediction.

### Small guidance on writing a system description paper

Structure of a system description could look as follows:

1. Abstract
2. Introduction
3. Related work
4. Task/Data
5. Description of your approach
6. Experiments & Results
   1. Please analyse your results and/ or do an error analysis
   2. We provided a [metric script](https://github.com/phhei/ArgsValidNovel/blob/gh-pages/Evaluation/Evaluator.py). By setting ``--verbose``, you get a bunch of possible interesting performance numbers, also including a separation into _in-topic_ (topic/ premises occurred already in the validation set in opposite to the conclusions) and _out-topic_ (completely novel topics, did not occur in the training/ validation data). The tast data is now also released.
7. Conclusion
(8. References)

## Important Dates

- Submission due: August 26, 2022
- Notification of acceptance+feedback: September 5, 2022
- Camera-ready papers due: September 12, 2022

All deadlines are 11:59 pm UTC -12h (“anywhere on Earth”).
