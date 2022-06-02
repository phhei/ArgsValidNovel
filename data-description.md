# Data Description

All data is manually annotated by three annotators. All three annotators annotated individually without any consultation with each other during the annotation process.

## Subtask A

Each line consists following fields:

1. topic: title of the debate
2. Premise
3. Conclusion
4. **Validity**
   1. 1 means: conclusion is valid
   2. 0 means: conclusion is defeasibly valid (this is not an own class itself - you are free to exclude such samples)
   3. -1 means: conclusion is **not** valid
5. Validity-Confidence
   1. "very confident": all three annotators agree in the validity-judgement
   2. "confident": two out of three annotators agree in the validity-judgment while one annotator abstains
   3. "majority": two out of three annotators agree in the validity-judgement, one disagrees
   4. "defeasible": there is no majority in votes - either all three annotators can't decide a validity rating or one annotator can't decide and the two others disagree each other (probably a very subjective sample)
6. **Novelty**
   1. 1 means: conclusion is novel
   2. 0 means: conclusion is somewhat novel/ borderline case (this is not an own class itself - you are free to exclude such samples)
   3. -1 means: conclusion is **not** novel
7. Novelty-Confidence
   1. same as validity-Confidence, only for novelty

### Additional remarks for Subtask A

- the confidence of a validity/ novelty judgment is just additional information - you are free to consider it or not. You do have not to predict the confidence
- the test set doesn't contain any defeasible validity/novelty instances hence there are no "0"-ratings, just "1" and "-1" for validity and novelty, respectively

## Subtask B

Each line consists following fields:

1. topic: : title of the debate
2. Premise
3. Conclusion 1
4. Conclusion 2
5. **Validity**
   1. 1 means: Conclusion 2 is more valid
   2. 0 means: both conclusions are equally valid
   3. -1 means: Conclusion 1 is more valid
6. Votes_Concl1IsMoreValid: number of votes voting for Conclusion 1 in terms of validity
7. Votes_ValidTie: numbers of votes voting for a tie in terms of validity
8. Votes_Concl2IsMoreValid: number of votes voting for Conclusion 2 in terms of validity
9. **Novelity**
   1. 1 means: Conclusion 2 is more novel
   2. 0 means: both conclusions are equally novel
   3. -1 means: Conclusion 1 is more novel
10. Votes_Concl1IsMoreNovel: number of votes voting for Conclusion 1 in terms of novelty
11. Votes_NovelTie: numbers of votes voting for a tie in terms of novelty
12. Votes_Concl2IsMoreNovel: number of votes voting for Conclusion 2 in terms of novelty

### Additional remarks for Subtask B

- the vote distribution is just additional information - you are free to consider it or not. You do have not to predict the distribution
- the test set also contains ties (in terms of validity/ novelty). Hence, there are three predictable classes per validity and novelty (worse, tie, better)
- this is a symmetric task. This means that if Conclusion A is better in Y than Conclusion B, B is also worse in Y than Conclusion A (ties are analogies). However, we include only one direction in the provided datasets, not both
- you're free to extend the provided datasets with additional samples from Subtask A (we do not provide each conclusion combination in the datasets in this subtask). Please notice three things if you do that:
  - if you extend the datasets, please provide this information later on in the submission form of your results
  - please beware: if two Conclusions received the same validity and/or novelty judgment (of course, given the same premise), you **can not** infer that both conclusions are equally valid and/or novel. Still, one conclusion can be (but have not to be) better in terms of validity and/ or novelty
  - please do not mix the different splits. If you want to extend the training split, you're not allowed to use the dev- or test-split from subtask A. If you want to extend the dev-split, you're not allowed to use the train- or test-split from subtask A
