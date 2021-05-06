# NLP_2021
Text classification: Book Genres

## To get bag of words features:
* Download data from http://www.cs.cmu.edu/~dbamman/booksummaries.html
* run **python clean.py**
* run **python bag_of_words.py**

## Linear Regression Model:
* run with tf-idf preprocesing **python linear_regression_model.py**
### Example Output:
```
              precision    recall  f1-score   support

           0       0.68      0.23      0.35        56
           1       0.67      0.19      0.29        74
           2       0.62      0.07      0.12        72
           3       1.00      0.06      0.11        35
           4       0.78      0.59      0.67       509
           5       0.74      0.30      0.43       256
           6       0.73      0.50      0.59       452
           7       0.00      0.00      0.00        25
           8       0.67      0.21      0.32       114
           9       0.40      0.28      0.33       378
          10       0.58      0.19      0.29       100
          11       0.78      0.63      0.69       580
          12       0.78      0.49      0.60       303
          13       0.67      0.57      0.62       533

   micro avg       0.70      0.46      0.55      3487
   macro avg       0.65      0.31      0.39      3487
weighted avg       0.69      0.46      0.54      3487
 samples avg       0.49      0.47      0.47      3487
```
