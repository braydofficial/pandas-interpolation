# Import the pandas libary and allocate it to the variable pd
import pandas as pd

# Define the variable df which stands for DataFrame and create a DataFrame from the CSV-File. Also setting the seperator to a semicolon
# because it would otherwise not work. By default this function uses a comma as the seperator.
df = pd.read_csv('./data.csv', sep=';')

# Accessing the column called Jan from the DataFrame created in the last step and make a linear interpolation on it.
# The argument axis defines in which direction the interpolation should be made. axis=0 means it will interpolate the column.
# If the axis would be set to 1 it would try to interpolate the row instead of the column, which isn't what we want to do here.
df['Jan'] = df['Jan'].interpolate(method='linear', axis=0)

# Print out the result from the interpolation.
print('\n\nJan: \n')
print(df['Jan'])

df['Feb'] = df['Feb'].interpolate(method='linear', axis=0)
print('\n\nFeb: \n')
print(df['Feb'])

df['Mar'] = df['Mar'].interpolate(method='linear', axis=0)
print('\n\nMar: \n')
print(df['Mar'])