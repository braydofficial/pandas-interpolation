# Import the pandas libary and allocate it to the variable pd
import pandas as pd

# Define the variable df which stands for DataFrame and create a DataFrame from the CSV-File. Also setting the seperator to a semicolon
# because it would otherwise not work. By default this function uses a comma as the seperator. Because the CSV-file has a comment
# in the first line, we give an argument named comment and define which character specifies the comment in the CSV-file
df = pd.read_csv('./data.csv', sep=';', comment='#')

# We create a bool_series on the index column of the CSV-File called year
bool_series = pd.isnull(df['Year'])
# Now we asign the bool_series to the DataFrame we created
df[bool_series]
# And with this command we create a linear interpolation based on the data we created and print it out. It will now print out the data for the missing
# fields.
print(df.interpolate(method='linear', axis=0))