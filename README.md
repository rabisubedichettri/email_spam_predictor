# Welcome to Email Spam Predictor

This system is made by Ensemble Modeling(Voting Classifier) with accuracy of 0.9816247582205029
and  precision 0.983739837398374 where Support Vector Classification ,BernoulliNB,ExtraTreesClassifier',LogisticRegression 
are used with hard voting. Here i have used dataset [spam.csv](https://www.kaggle.com/uciml/sms-spam-collection-dataset) for training model.

## Setup

- First step : create virtual environment

      virtualenv -p python3 venv

- Second step : activate virtual environment

      source venv/bin/activate

- Third step : install package | library from requirements.txt

       pip install -r requirements.txt

- Last step run streamlit server

      streamlit run app.py

## Demo

Click [here ](https://emailspampredictor.herokuapp.com/) to see demo

<img src="https://github.com/rabisubedichettri/email_spam_predictor/blob/main/demo.jpg" alt="demo" style="height: 500px; width:500px;"/>
