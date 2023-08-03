#print((50/100)*100)
import pandas as pds
data = pds.read_csv("Data_set.csv")
defaults = data["default payment next month"].value_counts()[1]
#print(defaults)
defaults_rate = (defaults/30000)*100
print(f"default rate is : {defaults_rate:.2f}%")