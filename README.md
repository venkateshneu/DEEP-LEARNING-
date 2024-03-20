# EMAIL CLASSIFIER  
Email Spam Classification using NLP and ML Techniques
Overview
This project aims to develop a classifier to distinguish between spam and non-spam emails using Natural Language 
Processing (NLP) techniques and Machine Learning (ML) algorithms. 
The dataset comprises labeled email messages as either "ham" (non-spam) or "spam".


Key Insights:
Imbalanced Dataset: The dataset exhibits an imbalance, with a higher proportion of spam emails.
Higher Word Counts: Spam emails tend to have higher word counts compared to non-spam emails,
as observed during Exploratory Data Analysis (EDA).

NLP Techniques Utilized:
Text Preprocessing:
Convert text to lowercase.
Tokenization: Split text into individual words.
Removal of stopwords and punctuation.
Stemming: Reduce words to their root form.

TF-IDF Vectorization:
Term Frequency-Inverse Document Frequency considers the importance of terms in the entire dataset.
This is advantageous for text classification tasks, especially with an imbalanced dataset.

ML Algorithms Employed:
Multinomial Naive Bayes (MNB):

Initially explored for its suitability in text classification tasks.
Support Vector Machine (SVM):

Demonstrated high accuracy in classifying emails.
K-Nearest Neighbors (KNN):

Achieved decent accuracy but lower precision compared to MNB and SVM.
Random Forest:

Yielded high accuracy and precision.

Ultimate Selection:
Multinomial Naive Bayes (MNB):
Chosen ultimately for its effectiveness in text classification tasks, particularly when combined with TF-IDF vectorization.
MNB Accuracy: 96.13%
MNB Precision: 99.07%
Further Enhancements:
Precision over Accuracy: Due to the dataset's imbalance, emphasis was placed on 
precision over accuracy in model evaluation.

TF-IDF vs Bag-of-Words: TF-IDF was chosen over Bag-of-Words due to its ability to a
ssign higher weights to rare terms, making it more suitable for imbalanced datasets.

Conclusion:
This project demonstrates the effectiveness of NLP techniques combined with ML algorithms in classifying spam emails. By prioritizing precision and leveraging Multinomial Naive Bayes ultimately, the classifier achieves reliable performance, accurately identifying spam emails while minimizing false positives.


