import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#Exception Handling
try:
    # Open the file in read mode
    with open('olympic_medals.csv', 'r', encoding='Latin1') as file:
        df = pd.read_csv(file)
except FileNotFoundError:
    st.error('File not found.')
    st.stop()
except pd.errors.EmptyDataError:
    st.error('File is empty.')
    st.stop()
except ValueError:
    st.error('Value error occurred,check the values in your data.')
    st.stop()
except KeyError:
    st.error('Key error occurred,check the column names in your data.')
    st.stop()
except Exception as e:
    st.error(f'An unexpected error occurred: {e}')
    st.stop()

# File Handling
summary = df.describe()
file_path = 'summary_olympic_analysis.txt'   # Define the file path
try:
    with open(file_path, 'w') as f:
        f.write(summary.to_string(header=True, index=True))
    print(f"Summary statistics saved to '{file_path}' successfully.")
except IOError as e:
    print(f"Error: Unable to write summary statistics to '{file_path}'. {e}")

# Streamlit app
st.title('EDA of Olympic Analysis')   

# Printing the DataFrame
st.subheader('Original dataset')
st.write(df)
st.write(df.shape)

# Handling missing values
st.subheader("After handling missing values")
df.dropna(inplace=True)
st.write(df)
st.write(df.shape)

# Handling duplicates
st.subheader("After handling duplicates")
df.drop_duplicates(inplace=True)
st.write(df)
st.write(df.shape)

# Example of EDA with Streamlit
st.subheader('Data Visualization:')
x_column = st.selectbox('Select X-axis column', df.columns)

# Ensure x_column is selected
if x_column:
    # Bar chart
    st.subheader('Bar Chart')
    st.bar_chart(df[x_column].head(10))

    # Line chart
    st.subheader('Line Chart')
    st.line_chart(df[x_column].head(60))

    # Scatter plot
    st.subheader('Scatter Plot')
    # Streamlit does not have st.scatter_chart, using matplotlib for scatter plot instead
    plt.figure(figsize=[10,5])
    plt.scatter(df.index[:60], df[x_column].head(60))
    plt.xlabel('Index')
    plt.ylabel(x_column)
    st.pyplot(plt)

    # Area chart
    st.subheader('Area Chart')
    st.area_chart(df[x_column].head(60))

    # Pie chart using matplotlib
    st.subheader("Pie chart using matplotlib")
    plt.figure(figsize=[10,10])
    plt.pie(df[x_column].value_counts().values, autopct='%1.1f%%', labels=df[x_column].value_counts().index, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    st.pyplot(plt)

    # Barh chart using matplotlib
    st.subheader("Barh chart using matplotlib")
    plt.figure(figsize=[10,5])
    plt.barh(
        df[x_column].value_counts().index[:10], 
        df[x_column].value_counts().values[:10], 
        color=['lightblue', 'pink'],
        label='x_column'
    )
    plt.xlabel('Count')
    plt.ylabel(x_column)
    st.pyplot(plt)
else:
    st.error('Please select a column for the X-axis.')
