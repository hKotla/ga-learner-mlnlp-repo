# --------------
# Importing header files
import warnings

import numpy as np

warnings.filterwarnings('ignore')

# New record
new_record = [[50, 9, 4, 1, 0, 0, 40, 0]]

# Reading file
# path = 'File path of subset_1000.csv'
data = np.genfromtxt(path, delimiter=",", skip_header=1)

# Code starts here
print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

census = np.concatenate((data, new_record))
print(census)

print(data.shape)
print(census.shape)

age = census[:, 0]
max_age = int(np.max(age))
min_age = int(np.min(age))
age_mean = round(np.mean(age), 2)
age_std = round(np.std(age), 2)

print(age)
print("\nMaximum age : ", max_age)
print("Minimum age : ", min_age)
print("Mean age : ", age_mean)
print("Standard deviation of age : ", age_std)

race_0 = []
race_1 = []
race_2 = []
race_3 = []
race_4 = []

for person in census:
    if person[2] == 0:
        race_0.append([person])
    elif person[2] == 1:
        race_1.append([person])
    elif person[2] == 2:
        race_2.append([person])
    elif person[2] == 3:
        race_3.append([person])
    elif person[2] == 4:
        race_4.append([person])

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

race_lengths = [len_0, len_1, len_2, len_3, len_4]
print("\n Race lengths - ", race_lengths)

minority_race = race_lengths.index(min(race_lengths))

print("\n Minority race - ", minority_race)

# STEP 4

senior_citizens_temp = []

for person in census:
    if person[0] > 60:
        senior_citizens_temp.append([person])

senior_citizens_len = len(senior_citizens_temp)

senior_citizens = np.array(senior_citizens_temp)

sum_temp = sum(senior_citizens)
print(sum_temp)

working_hours_sum = sum_temp[0][6]

# Matrix =[[0, 2, 2],
#          [0, 2, 2],
#          [0, 0, 2]]
# matrix_arr = np.array(Matrix)
#
# sum1 = sum(matrix_arr[: , 1])

avg_working_hours = round((working_hours_sum/senior_citizens_len), 2)

print("\nWorking_hours_sum - ", working_hours_sum)
print("Avg_working_hours - ", avg_working_hours)

# STEP 5

high =[]
low = []

for person in census:
    if person[1] > 10:
        high.append([person])
    elif person[1] <= 10:
        low.append([person])

high_mean = np.mean(high, axis = 0)
low_mean = np.mean(low, axis = 0)

avg_pay_high = round(high_mean[0][7], 2)
avg_pay_low = round(low_mean[0][7], 2)

print("\n Avg_pay_high - ", avg_pay_high)
print(" Avg_pay_low - ", avg_pay_low)





