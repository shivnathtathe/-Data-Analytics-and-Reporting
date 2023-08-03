from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import pandas as pds
import warnings
warnings.filterwarnings("ignore")
data = pds.read_csv("Data_set.csv")
data['intercept']=1
new_data= data[(data.BILL_AMT6 > 0 ) & (data.Limit > 0 ) & (data.Debt > 31)]
new_data["payment_ratio"]= new_data.PAY_AMT6/new_data.BILL_AMT6
new_data["credit_limit"]= new_data.Limit/1000
X = new_data[['Debt','credit_limit','intercept','payment_ratio']]
Y = new_data ['default payment next month']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

Log_mod_coff = sm.Logit(Y_train,X_train).fit()
print(Log_mod_coff.summary())