# BLTFuzzyLogic

```
This readme is not done, and will be continued when I got the desire to.
```

This simple code is an implementation of Fuzzy Logic usage to solve a simple task. The task is, given the data in 'DataTugas2.csv'
which includes 100 data of a person's income and debts, we have to choose 20 of them to be given a BLT (Bantuan Langsung Tunai) or to simply
say it in english, a direct cash assistance. The output is a file 'TebakanTugas2.csv' which contains 20 rows of numbers (person's sequence number in 'DataTugas2.csv')
that are chosen to be given the cash assistance.

That are 6 main steps of making this algorithm:

## 1. Linguistic
In this step, I have to make categories for the income and debts, and also the acceptance. The purpose is so we can calculate the scores
of each categories for each person. Then the scores will be used to calculate the final score that will decide whether the person is suitable
to receive the assistance.

### Income
For the income I've splitted it to four categories:
* Low income (L)
* Below average income (B)
* Average income (A)
* High income (H)

### Debts
For the debts, I've decided to split it into three:
* Few debts (F)
* Normal debts (N)
* Much debts (M)

### Acceptance
For the acceptance, again, I've splitted it to three:
* YES
* MAYBE
* NO

## 2. Membership Function
The second step is to define the range of each categories. From the data that we've got, I've assumed that the income have the range of:
```
0 ≤ x ≤ 2.0
```
And the debts have the range of:
```
0 ≤ x ≤ 100
```

From that, we can start to define the ranges.

### Low income (L)



## 3. Fuzzification
## 4. Rules
## 5. Inference
## 6. Defuzzification
