import pandas as pds
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")
data=pds.read_csv("Data_set.csv")
new_data=data[(data.BILL_AMT6>0) & (data.Limit>0) & (data.Debt>31)]
new_data["credit_limit"]=data.Limit/1000
new_data["payment_ratio"]=new_data.PAY_AMT6/new_data.BILL_AMT6
new_data["intercept"]=1
new_data['total_debt']=new_data.Debt
new_data['payment_ratio_cap']=np.where(new_data['payment_ratio']>new_data.payment_ratio.quantile(0.99),new_data.payment_ratio.quantile(0.99),new_data["payment_ratio"])
new_data['rescaled_limit_cap']=np.where(new_data['credit_limit']>new_data.credit_limit.quantile(0.99),new_data.credit_limit.quantile(0.99),new_data["credit_limit"])
new_data['Debt_cap']=np.where(new_data['total_debt']>new_data.total_debt.quantile(0.99),new_data.total_debt.quantile(0.99),new_data["total_debt"])

X=new_data[['Debt_cap','rescaled_limit_cap','payment_ratio_cap','intercept']]
Y=new_data['default payment next month']

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

lr_model=LogisticRegression(solver="liblinear").fit(x_train,y_train)

print("train_n_auc_value",round(roc_auc_score(y_train,lr_model.predict_proba(x_train)[:,1]),4))
print("test_n_auc_value",round(roc_auc_score(y_test,lr_model.predict_proba(x_test)[:,1]),4))