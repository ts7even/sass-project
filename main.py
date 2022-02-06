import numpy as np
import pandas as pd

# You will start working with the dataset SASS. There are nine different data files that you will download. You will work with the public teacher file. 
# Download the dataset to your local computer.
# Provide a description of the dataset.
# Provide summary statistics on this data file. 
# Provide a frequency table on teachers' age(AGE_T), race/ethnicity(RACETH_T), and main teaching assignment(ASSIGN). Answer the following questions:

# How many observations or rows of data does this data file have?
# How many variables or columns of data does this data file have?
# What is the average age of the teachers in this data file?
# How many black teachers are there in this data file?
# How many math and science teachers are there in this data file?

public_teacher_data = 'source/dataset/SASS_99_00_S4a_v1_0.csv' # Public Teachers
# public_teacher_data = 'source/dataset/SASS_99_00_S4b_v1_0.csv' # Private Teachers



# Teacher Data Frame
df = pd.read_csv(public_teacher_data)
total_rows = df.shape[0]   # Number of Rows (Observations)
total_columns = df.shape[1] # Number of Columns (Varibles)



# Appending to dicitonary
age1 = [] # 1 = 'Less than 30 years'
age2 = [] # 2 = '30 to 39 years'
age3 = [] # 3 = '40 to 49 years'
age4 = [] # 4 = '50 years or older'



def main():
    print(f'The amount of rows (Observations)in the data frame: {total_rows}')
    print(f'The amount of columns (Varibles) in the data frame: {total_columns}')

    

def black_teachers():
   black_teacher_filter = df[   (df['RACETH_T'] == 3)  ]
   total_black_teachers = black_teacher_filter.shape[0] 
   print(f'The total amount of black teachers: {total_black_teachers}')

def teacher_age():    
    data_age_1 = df[ (df['AGE_T']== 1)]
    total_age_1 = data_age_1.shape[0]
    data_age_2 = df[ (df['AGE_T']== 2)]
    total_age_2 = data_age_2.shape[0]
    data_age_3 = df[ (df['AGE_T']== 3)]
    total_age_3 = data_age_3.shape[0]
    data_age_4 = df[ (df['AGE_T']== 4)]
    total_age_4 = data_age_4.shape[0]
   # print(f'There are {total_age_1} teachers that are 30 years or younger old')
   # print(f'There are {total_age_2} teachers that are between 30 to 39 years old')
   # print(f'There are {total_age_3} teachers that are 40 to 49 years old')
   # print(f'There are {total_age_4} teachers that are 50+ years old')

    age1.append(total_age_1)
    age2.append(total_age_2)
    age3.append(total_age_3)
    age4.append(total_age_4)

    # Total Teachers that Completed the age varible
    total_teachers_ages = np.sum((age1)+ (age2) + (age3) + (age4))
    # print(f'Total Teachers: {total_teachers_ages}')

    percent_age1 = ((age1/total_teachers_ages) * 100)
    # print(f'Percentage of teachers age between 0 to 30: {percent_age1}')

    percent_age2 = ((age2/total_teachers_ages) * 100)
    # print(f'Percentage of teachers age between 30 to 39: {percent_age2}')

    percent_age3 = ((age3/total_teachers_ages) * 100)
    # print(f'Percentage of teachers age between 40 to 49: {percent_age3}')

    percent_age4 = ((age4/total_teachers_ages) * 100)
    # print(f'Percentage of teachers age between 50+: {percent_age4}')

    print("The average age of Teachers is between 40 to 49 years old")
    


    
def math_science_teachers():
    math_science_filter = df[ (df['ASSIGN'] == 2)]
    total_math_science_teachers = math_science_filter.shape[0]
    print(f'The total amount of Math and Science Teachers: {total_math_science_teachers}')

main()
black_teachers()
teacher_age()
math_science_teachers()