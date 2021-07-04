#We can use an array or a database table to structure or present data.#

#Example of an array:#
from numpy import inf
import pandas as pd
from pandas.core import indexing

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)
#Count the number of columns:


df = pd.DataFrame(data=d)
count_column = df.shape[1]
print("")
print("number of column:")
print(count_column)



# Array = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
# print(Array)
# print(Array+ [150, 160])

#use the read_csv() function to import a CSV file with the health data:
health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data)

