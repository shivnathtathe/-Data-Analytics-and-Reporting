import pandas as pds
import warnings
warnings.filterwarnings("ignore")
data = pds.read_csv("Data_set.csv")
new_data = data[(data.BILL_AMT6>0)&(data.Limit>0)&(data.Debt>31)]
new_data["payment_ratio"]=new_data.PAY_AMT6/new_data.BILL_AMT6
new_data["bins"]=pds.qcut(new_data["payment_ratio"],5, labels=['bin1', 'bin2', 'bin3', 'bin4', 'bin5'])

#BIN1
new_data_bin1=new_data[new_data.bins=="bin1"]
defaults_bin1 = new_data_bin1["default payment next month"].value_counts()[1]
defaults_rate1 = (defaults_bin1/new_data_bin1.shape[0])*100
print(f"default rate in bin1 is : {defaults_rate1:.2f}%")

#BIN2
new_data_bin2=new_data[new_data.bins=="bin2"]
defaults_bin2 = new_data_bin2["default payment next month"].value_counts()[1]
defaults_rate2 = (defaults_bin2/new_data_bin2.shape[0])*100
print(f"default rate in bin2 is : {defaults_rate2:.2f}%")

#BIN3
new_data_bin3 = new_data[new_data.bins=="bin3"]
defaults_bin3 = new_data_bin3["default payment next month"].value_counts()[1]
defaults_rate3 = (defaults_bin3/new_data_bin3.shape[0])*100
print(f"default rate in bin3 is : {defaults_rate3:.2f}%")

#BIN4
new_data_bin4 = new_data[new_data.bins=="bin4"]
defaults_bin4 = new_data_bin4["default payment next month"].value_counts()[1]
defaults_rate4 = (defaults_bin4/new_data_bin4.shape[0])*100
print(f"default rate in bin4 is : {defaults_rate4:.2f}%")

#BIN5
new_data_bin5=new_data[new_data.bins=="bin5"]
defaults_bin5 = new_data_bin5["default payment next month"].value_counts()[1]
defaults_rate5 = (defaults_bin5/new_data_bin5.shape[0])*100
print(f"default rate in bin5 is : {defaults_rate5:.2f}%")
