# Data Description

All data is manually annotated by three annotators. All three annotators annotated individually without any consultation with each other during the annotation process.

## Subtask A

Each line consists following fields:

1. topic: title of the debate
2. Premise
3. Conclusion
4. Validity
   1. 1 means: conclusion is valid
   2. 0 means: conclusion is defeasibly valid (this is not an own class itself - you are free to exclude such samples)
   3. -1 means: conclusion is **not** valid
5. Validity-Confidence
   1. "very confident": all three annotators agree in the validity-judgement
   2. "confident": two out of three annotators agree in the validity-judgment while one annotator abstains
   3. "majority": two out of three annotators agree in the validity-judgement, one disagrees
   4. "defeasible": there is no majority in votes - either all three annotators can't decide a validity rating or one annotator can't decide and the two others disagree each other (probably a very subjective sample)
6. Novelty
   1. 1 means: conclusion is novel
   2. 0 means: conclusion is somewhat novel/ borderline case (this is not an own class itself - you are free to exclude such samples)
   3. -1 means: conclusion is **not** novel
7. Novelty-Confidence
   1. same as validity-Confidence, only for novelty

### Additional remarks

- the confidence of a validity/ novelty judgement is just an additional information - you are free to consider it or not. You have not to predict the confidence
- the test set doesn't contain any defeasible validity/novelty samples, hence there are no "0"-ratings, just "1" and "-1" for validity and novelty, respectively
