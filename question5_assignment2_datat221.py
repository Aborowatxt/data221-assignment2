import pandas as pd
dataframe = pd.read_csv("student.csv")    #Store csv file in a variable

#Categorize grades into bands: # Low (≤ 9), Medium (10–14), High (≥ 15)
dataframe["grade_band"] = pd.cut(dataframe['grade'], bins = [-1,9,14, float("inf")], labels =["Low", "Medium","High"])

summary_table = dataframe.groupby("grade_band").agg(   #.agg() is used to apply multiple aggregation functions
    number_of_students=("grade", "count"),  #Counts how many rows (students) are in each grade band
    average_absences=("absences", "mean"),  #Calculates the average absences for each grade band
    percent_with_internet=("internet", "mean"))  #proportion

summary_table["percent_with_internet"] = summary_table["percent_with_internet"] * 100  #changes to percentage

summary_table.to_csv("student_bands.csv", index = False)  #Creates a new csv file for the summary table



