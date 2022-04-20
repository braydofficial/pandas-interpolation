# Import the pandas libary and allocate it to the variable pd
import pandas as pd
import matplotlib.pyplot as plt

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
df = df.interpolate(method='linear', axis=0)
print(df)

# Create a diagramm with matplotlib and set it's figure to 1 and it's title to Data. Include all data from the CSV in it and use the column Year as
# it's index.
df.set_index('Year').plot()
plt.figure(1)
plt.title('Data')

# Now create another diagramm with only the data for January in the CSV. Set it's figure to 2 and call both diagrams in the end, so both will be shown at
# the same time.
plt.figure(2)
plt.plot(df.Jan, df.Year)
plt.title('Januar Data')
plt.show()