import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
data=pd.read_csv("Data_set.csv")
new_data=data[(data.BILL_AMT6>0) & (data.Limit>0) & (data.Debt>31)]
new_data["credit_limit"]=data.Limit/1000
new_data["payment_ratio"]=new_data.PAY_AMT6/new_data.BILL_AMT6
new_data["intercept"]=1
X=new_data[['Debt','credit_limit','payment_ratio','intercept']]
Y=new_data['default payment next month']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

lr_model=LogisticRegression(solver="liblinear").fit(X_train,Y_train)
print("Train_n_auc_value",round(roc_auc_score(Y_train,lr_model.predict_proba(X_train)[:,1]),4))
print("Test_n_auc_value",round(roc_auc_score(Y_test,lr_model.predict_proba(X_test)[:,1]),4))