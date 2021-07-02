#We can use an array or a database table to structure or present data.#

#Example of an array:#
import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)
#Count the number of columns:


df = pd.DataFrame(data=d)
count_column = df.shape[1]
print("number of column:")
print(count_column)



# Array = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
# print(Array)
# print(Array+ [150, 160])
