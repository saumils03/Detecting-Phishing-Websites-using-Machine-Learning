# Detecting-Phishing-Websites-using-Machine-Learning
Classifying a URL as phishing or benign using Machine Learning

# Objective:
Phishing is a major cybersecurity attack in today's time which targets home internet users to large office employees. It can be described as the process of tricking online users into giving up their sensitive information such as usernames, passwords and financial credentials. The objective of this project is to train machine learning models on the dataset to predict phishing websites. A dataset is taken which contains both benign and phishing URLs and from them, the required URL and website content-based features are extracted. The performance metrics of each model are compared.

## Dataset Used:
https://www.kaggle.com/datasets/siddharthkumar25/malicious-and-benign-urls

## Feature Extraction:
The dataset till now consist of only legit and malicious urls, in this part some useful features from these urls are extracted and our dataset is further improved to make it more suitable for training ML models.

The below mentioned category of features are extracted from the URL data :
- Length based Features ( 5 features extracted)
- Count based Features ( 11 features extracted)
- Binary Features  ( 2 features extracted)

 All together 18 features are extracted from each url of the dataset.
 
## Model Training:
This is a binary classiication problem that is being solved i.e. a URL has to be classifed as either benign or malicious.
The ML models used in the project are:
- Decision Tree
- Random Forest
- Naive Bayes
- Logistic Regression

Out of all these models, Decision Tree gives the highest accuracy score and is selected for prediction in the final application.

## How to Run:
app.py file needs to be run (preferably using Anaconda because it has a few requirements that need to be installed but already come with Anaconda).
Then the URL will be entered in the input field, then after clicking the Check URL button the prediction output will be displayed on the screen whether the URL is benign or phishing.
