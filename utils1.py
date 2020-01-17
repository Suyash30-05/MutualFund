#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.externals import joblib
import re
import bs4
import requests


# In[3]:


import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "newagent-vrapji-fbf68c05033b.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "newagent-vrapji"


# In[ ]:


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(query,session_id):
    response=detect_intent_from_text(query,session_id)
    return response.fulfillment_text ### gives a reply

import pandas as pd
import numpy as np
import pickle 
import re
import bs4
import requests
import joblib


def ML_pred(list_2):
    ml= joblib.load('python_project_knn.pkl' , mmap_mode ='r')### will have to add joblib file in project folder
    print('u-1')
    age=list_2[0]
    tenure=list_2[2]
    capital=list_2[1]
    a=[]
    t=[]
    a.append(age)
    t.append(tenure)
    df=pd.DataFrame()
    df['age']=a
    df['tenure']=t
    pred=ml.predict(df)
    line2=''
    ## balanced funds
    if pred[0]=='medium':
        fund='balanced fund'
        url='https://www.moneycontrol.com/mutual-funds/best-funds/hybrid/returns/2'
    elif pred[0]=='high':
        fund='Equity fund'
        url='https://www.moneycontrol.com/mutual-funds/best-funds/equity/returns/2'
    else :#pred[0]=='low':
        fund='Debt fund'
        url='https://www.moneycontrol.com/mutual-funds/best-funds/equity/returns/2'

    
    return fund+' would be a good choice according to your needs' + '/n' + 'you can search best mutual funds on the following link' + '/n' + url
  