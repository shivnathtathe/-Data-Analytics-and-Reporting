#Q16:
from sklearn.model_selection import train_test_split
import pandas as pds
import numpy as np
import warnings
warnings.filterwarnings("ignore")
data = pds.read_csv("data_set.csv")
data['intercept'] = 1
new_data = data[(data.BILL_AMT6 > 0) & (data.Limit > 0) & (data.Debt > 31)]
new_data["payment_ratio"] = new_data.PAY_AMT6 / new_data.BILL_AMT6
new_data["credit_limit"] = new_data.Limit/1000
new_data['total_debt'] = new_data.Debt

#after capping
new_data['payment_ratio_cap'] = np.where(new_data['payment_ratio'] > new_data.payment_ratio.quantile(0.99) , new_data.payment_ratio.quantile(0.99) , new_data['payment_ratio'])
new_data['credit_limit_cap'] = np.where(new_data['credit_limit'] > new_data.credit_limit.quantile(0.99) , new_data.credit_limit.quantile(0.99) , new_data['credit_limit'])
new_data['Debt_cap'] = np.where(new_data['total_debt'] > new_data.total_debt.quantile(0.99) , new_data.total_debt.quantile(0.99) , new_data['total_debt'])

X = new_data[['Debt_cap','credit_limit_cap','intercept','payment_ratio_cap']]
Y = new_data ['default payment next month']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#print(Y_train.shape)
print("Rows in x_train : ",X_train.shape[0])
print("Columns in x_train : ",X_train.shape[1])

#print(Y_test.shape)
print("Rows in x_test : ",X_test.shape[0])
print("Columns in x_test : ",X_test.shape[1])