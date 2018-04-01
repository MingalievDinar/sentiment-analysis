# sentiment-analysis

## The project is to analyse of text tonality / sentiment analysis.

The aim - is to develop a model that will give accurate predictions for the customer's feedback (in russian language) on electronic goods. There is no trining set. It should be collected.

## Projects steps overview
The first step was to build a model with the given data about on films review. At this step, I learnt how to analyze the text, what metrics to use, how the classifiers and their settings are better able to cope with this task.
Then, the second step is sentiment analysis of product reviews in the store.
This task is divided into the following sub-tasks:
1. Data collection / parsing of a real online store
2. Data processing and cleaning
3. Model selection, cross-validation tests
4. Make an interactive demonstration for your algorithm

## Folders and files:

* [parsingModelDev](https://github.com/MingalievDinar/sentiment-analysis/tree/master/parsingModelDev) - steps lelated to data collection and model development:
  * data parsing (BeautifulSoup bs4)
  * data processing
  * feature extraction (CountVectorizer and TfidfVectorizer from sklearn.feature_extraction.text)
  * creating Pipeline
  * model selection (cross_val_score and GridSearchCV from sklearn.model_selection)
  * considered models: SVC, SGD and Logistic
* [webServer](https://github.com/MingalievDinar/sentiment-analysis/tree/master/webServer) - steps lelated to creating small server on Flask
