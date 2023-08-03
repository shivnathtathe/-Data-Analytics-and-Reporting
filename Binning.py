import pandas as pds
data = pds.read_csv("Data_set.csv")

#new_data["payment_ratio_bin"]=pds.qcut(new_data["payment_ratio"],5, labels=['bin1', 'bin2', 'bin3', 'bin4', 'bin5'])
#print(new_data.payment_ratio_bin)

data["bins"]=pds.qcut(data["Debt"],5, labels=['bin1', 'bin2', 'bin3', 'bin4', 'bin5'])

#BIN1
data_bin1=data[data.bins=="bin1"]
defaults_bin1 = data_bin1["default payment next month"].value_counts()[1]
defaults_rate1 = (defaults_bin1/data_bin1.shape[0])*100
#print("default rate in bin1 is : ",defaults_rate1 ,"%")
print(f"default rate in bin1 is : {defaults_rate1:.2f}%")

#BIN2
data_bin2=data[data.bins=="bin2"]
defaults_bin2 = data_bin2["default payment next month"].value_counts()[1]
defaults_rate2 = (defaults_bin2/data_bin2.shape[0])*100
#print("default rate in bin2 is : ",defaults_rate2 ,"%")
print(f"default rate in bin2 is : {defaults_rate2:.2f}%")

#BIN3
data_bin3 = data[data.bins=="bin3"]
defaults_bin3 = data_bin3["default payment next month"].value_counts()[1]
defaults_rate3 = (defaults_bin3/data_bin3.shape[0])*100
#print("default rate in bin3 is : ",defaults_rate3 ,"%")
print(f"default rate in bin3 is : {defaults_rate3:.2f}%")

#BIN4
data_bin4 = data[data.bins=="bin4"]
defaults_bin4 = data_bin4["default payment next month"].value_counts()[1]
defaults_rate4 = (defaults_bin4/data_bin4.shape[0])*100
#print("default rate in bin4 is : ",defaults_rate4 ,"%")
print(f"default rate in bin4 is : {defaults_rate4:.2f}%")

#BIN5
data_bin5=data[data.bins=="bin5"]
defaults_bin5 = data_bin5["default payment next month"].value_counts()[1]
defaults_rate5 = (defaults_bin5/data_bin5.shape[0])*100
#print("default rate in bin5 is : ",defaults_rate5 ,"%")
print(f"default rate in bin5 is : {defaults_rate5:.2f}%")

#new_data["bin23"]=new_data[(new_data.payment_ratio=="bin1")]
#print(new_data["bin23"])