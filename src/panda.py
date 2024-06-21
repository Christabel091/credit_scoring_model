import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sales_data = pd.read_csv('sales_data.csv')
print("Data before cleeaning sales data")
print(sales_data)
patients = pd.read_csv("patients.csv")
print("Data before cleeaning patients data")
print([patients])
patients = patients.dropna()
print("Patients data after cleaning")
print(patients)
#raed_csv loads data into a data frame, also the function dataframe
sales_data.dropna(inplace=True)  # Remove missing values
print("Data after cleansing")
print(sales_data)
#dropna cleans data removes rows that are missing etc
sales_data['date'] = pd.to_datetime(sales_data['date'])  # Convert date column to datetime
print("Data after adding data time")
print(sales_data)
# Resample the data to calculate monthly sales totals
monthly_sales = sales_data.resample('M', on='date')['revenue'].sum()

# Calculate the average monthly sales
average_monthly_sales = np.mean(monthly_sales)

# Display the results
print("Monthly Sales Totals is : ")
print(monthly_sales)
print("\nAverage Monthly Sales:", end="")
print(average_monthly_sales)
monthly_sales.plot()
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.savefig("plot.png")
plt.show()
