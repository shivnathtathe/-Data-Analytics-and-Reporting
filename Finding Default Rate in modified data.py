import pandas as pds
data = pds.read_csv("Data_set.csv")
new_data = data[(data.BILL_AMT6>0)&(data.Limit>0)&(data.Debt>31)]
defaults = new_data["default payment next month"].value_counts()[1]
defaults_rate = (defaults/25291)*100
print(f"default rate in model devlopement data is : {defaults_rate:.2f}%")