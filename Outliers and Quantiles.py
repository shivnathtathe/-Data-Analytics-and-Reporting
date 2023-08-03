import pandas as pds
data = pds.read_csv("Data_set.csv")
new_data= data.loc[(data.BILL_AMT6 > 0) & (data.Limit > 0) & (data.Debt > 31)]
new_data["payment_ratio"]= new_data.PAY_AMT6/new_data.BILL_AMT6
new_data["credit_limit"]= new_data.Limit/1000
new_data["total_debt"]= new_data.Debt

#1st percentile for payment ratio,credit limit,total debt.
#print(new_data[['payment ratio','credit limit','total debt']].quantile(0.01))
print("Payment ratio 1st percentile : ",new_data.payment_ratio.quantile(0.01))
print("credit_limit 1st percentile : ",new_data.credit_limit.quantile(0.01))
print("total_debt 1st percentile : ",new_data.total_debt.quantile(0.01))
print("\n")
#99th percentile for payment ratio,credit limit,total debt.
print(f"Payment ratio 99th percentile : {new_data.payment_ratio.quantile(0.99):.2f}")
print("credit_limit 99th percentile : ",new_data.credit_limit.quantile(0.99))
print("total_debt 99th percentile : ",new_data.total_debt.quantile(0.99))