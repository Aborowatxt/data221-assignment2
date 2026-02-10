import pandas as pd
crime_dataframe = pd.read_csv("crime.csv") # Load the crime dataset into a DataFrame


# Create a new column that labels areas as LowCrime or High-Crime based on violent crime rate
crime_dataframe["risk"] = pd.cut(crime_dataframe["ViolentCrimesPerPop"],
                                bins = [-1,0.50,float("inf")],
                                labels =["LowCrime", "High-Crime"],
                                right=False)  #left inclusive for 0.50

# Group data by crime risk and calculate average unemployment rate
average_unemployment = crime_dataframe.groupby("risk")["PctUnemployed"].mean()

print("Average Unemployment Rate by Crime Risk")

print(f"HighCrime: {average_unemployment['High-Crime']:.2f}")
print(f"LowCrime:  {average_unemployment['LowCrime']:.2f}")