import pandas

from collections import Counter
from pandas.plotting import scatter_matrix
import os

#cancle the limitation of the max columns  and rows
# pandas.options.display.max_columns = None
# pandas.options.display.max_rows = None
#p1
address = "/Users/apple/Documents/INFOSYS/722/pm25/Shanghai.csv"
orignal_data = pandas.read_csv(address,index_col=0)
filter_two = orignal_data.drop(columns=['PM_Jingan', 'PM_Xuhui'],inplace=False)
# filter_two.to_csv(r'/Users/apple/Documents/COMPSI/722/Iteration 2/orignial_filtered.csv',encoding='gbk',index=False)
import pandas_profiling
# profile = filter_two.profile_report(title='PM2.5 in SH Report')
# profile.to_file(output_file='pm2.5SH_report.html')
# print(filter_two.info())

#Visualization
# import the matplotlib module
import matplotlib.pyplot as plt
# import the seaborn module
import seaborn as sns
#to show the graph
import matplotlib; matplotlib.use('TkAgg')

# print(filter_two.isnull())

sns.set(style="darkgrid")
# set the background colour of the plot to white
sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
sns.set(rc={'figure.figsize':(11.7,8.27)})
# ax = sns.countplot(x="PM_US Post", data=filter_two)
#bar-plot for year and mean of PM 2.5
# ax = sns.barplot(x="year", y="PM_US Post", data=filter_two)
ax = sns.relplot(x="PRES", y="PM_US Post", data=filter_two)
# plt.hist(filter_two['PM_US Post'])
plt.show()



#missing value
# address = "/Users/apple/Documents/COMPSI/722/Iteration 2/orignial_filtered.csv"
# orignal_data = pandas.read_csv(address)
# description = orignal_data.describe()
# print(description)
# orignal_data.info()
# fill_Missing = orignal_data.dropna()
# print(fill_Missing.info())
# fill_Missing.to_csv(r'/Users/apple/Documents/COMPSI/722/Iteration 2/no_MissingValue.csv',encoding='gbk',index=False)



#clean data

# #
# address = "/Users/apple/Documents/COMPSI/722/Iteration 2/no_MissingValue.csv"
# data = pandas.read_csv(address)
# print(data.describe())
#
# data1 = data[data['PM_US Post'] <= 500]
# # print(data1.describe())
#
# data2 = data1[data1['Iws'] <= 158.5]
# print(data2.describe())
# data2.to_csv(r'/Users/apple/Documents/COMPSI/722/Iteration 2/clean_data.csv',encoding='gbk',index=False)


#Construct data
# address = "/Users/apple/Documents/COMPSI/722/Iteration 2/clean_data.csv"
# data = pandas.read_csv(address)
# data1 = data
# def function(a):
#     if a <= 35:
#         return 1
#     elif a <= 75:
#         return 2
#     elif a <= 115:
#         return 3
#     elif a <= 150:
#         return 4
#     elif a <= 250:
#         return 5
#     else:
#         return 6
#
# data1['Air Quality'] = data1.apply(lambda x: function(x['PM_US Post']), axis = 1)

#     # another way for Group By do not use this part
#     # def createNewColumn(df):
#     #     df["Levels"] = df.apply(lambda x: "Good" if x['Air Quality'] == 1 else("Moderate" if x['Air Quality'] == 2 else()))
#     #       return df
#     #data1.groupby("Air Quality").apply(createNewColumn)
#     # another way for Group By do not use this part

# # print(Counter(data1['cbwd']))
# def function1(a):
#     if a == "NE":
#         return 1
#     elif a == "SE":
#         return 2
#     elif a == "NW":
#         return 3
#     elif a == "SW":
#         return 4
#     else:
#         return 5
# data1['cbwd_new'] = data1.apply(lambda x: function1(x['cbwd']), axis = 1)
# print(data1.head())
# data1.to_csv(r'/Users/apple/Documents/COMPSI/722/Iteration 2/construct_data.csv',encoding='gbk',index=False)


#
# address = "/Users/apple/Documents/COMPSI/722/Iteration 2/construct_data.csv"
# data = pandas.read_csv(address)
# data1 = data.drop('PM_US Post', 1)
# data2 = data1.drop('cbwd',1)
#
# #Visualization for the count of Air Quality
# ax = sns.countplot(x="Air Quality", data=data2)
# plt.show()

# data2.to_csv(r'/Users/apple/Documents/COMPSI/722/Iteration 2/integrate_data.csv',encoding='gbk',index=False)



#Balance data
# address = "/Users/apple/Documents/COMPSI/722/Iteration 2/integrate_data.csv"
# data = pandas.read_csv(address)
# y=data['Air Quality'].values
# X=data.drop('Air Quality',axis=1)
# # print(X.head())
# # print(Counter(data['Levels']))
# from imblearn.over_sampling import SMOTE
# smo = SMOTE(random_state=42)
# X_smo, y_smo = smo.fit_sample(X, y)
# # print(X_smo)
# data2 = pandas.DataFrame(
#     X_smo,
#     columns=['No','year','month','day','hour','season','DEWP','HUMI','PRES','TEMP','lws','precipitation','Iprec','cbwd_new']
# )
# data2["year"] = data2["year"].astype("int")
# data2["month"] = data2["month"].astype("int")
# data2["day"] = data2["day"].astype("int")
# data2["hour"] = data2["hour"].astype("int")
# data2["season"] = data2["season"].astype("int")
# data2["cbwd_new"] = data2["cbwd_new"].astype("int")
# data2["Air Quality"] = y_smo
# # print(data2.head())
# data2.sort_values(by=['year','month','day','hour'])
# data2.to_csv(r'/Users/apple/Documents/COMPSI/722/Iteration 2/balanced_data.csv',encoding='gbk',index=False)

#Reduce data(Check the importance)
# address = "/Users/apple/Documents/COMPSI/722/Iteration 2/balanced_data.csv"
# data = pandas.read_csv(address)
# print(data.describe())
# print(data.corr()['Air Quality'])
# print(data.describe())
# data1 =data.drop('No',axis=1)
# data1.to_csv(r'/Users/apple/Documents/COMPSI/722/Iteration 2/reduced_data.csv',encoding='gbk',index=False)
