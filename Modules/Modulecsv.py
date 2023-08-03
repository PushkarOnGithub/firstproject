import csv
import names
import random

# Creating a program to generate fake people and their mail IDs


# CAPS = "QWERTYUIOPASDFGHJKLZXCVBNM"
# lows = CAPS.lower()
#
# with open("RandomPeople.csv", 'w', newline='') as rp:
#
#     headers = ['first_name', 'last_name', 'email']
#     file = csv.writer(rp, delimiter=',')
#
#     file.writerow(headers)
#
#     for i in range(50):
#         data = [names.get_first_name(), names.get_last_name(), ''.join(random.choices(CAPS+lows, k=10)) + '@gmail.com']
#
#         file.writerow(data)


# Program to Merge two csv files together into another csv file

with open("RandomPeopleHeaders.csv", 'r') as rph:
    file = csv.reader(rph)
    with open("RandomPeople.csv", 'r') as rp:
        file2 = csv.reader(rp)
        with open("New_file.csv", 'w', newline='') as new_file:
            file3 = csv.writer(new_file)

            file3.writerows(file)
            # for line in file2:
            file3.writerows(file2)


