import pandas as pd
dataframe = pd.read_csv("student.csv")    #Store csv file in a variable

# Filter students who, study at least 3 hours, have internet access, 5 or fewer absences
filtered_data = dataframe[(dataframe['studytime'] >= 3) & (dataframe['internet'] == 1) & (dataframe['absences'] <= 5)]
filtered_data.to_csv("high_engagement.csv", index=False)

number_of_students = len(filtered_data)
average_grade = filtered_data["grade"].mean() # Calculate the average grade of the filtered students


print("Number of students saved:", number_of_students) # Print the number of students saved to the new file

print("Average grade:", average_grade) # Print the average grade of the filtered students

