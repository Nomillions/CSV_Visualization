import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)  # skips header row

# the enumerate() function returns both the index of each item and the
# value of each item, as you loop through the list

for index, column_header in enumerate(header_row):
    print("Index: ", index, "Column Name: ", column_header)
    # allows us to know the index value of each header item

highs = []
dates = []

# mydate = "2018-07-01"
# converted_date = datetime.strptime(mydate, "%Y-%m-%d")
# print(converted_date)

# we call strptime() containing the date as the first argument, and the second argument will format the date how we want it.

for row in csv_file:
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)
    highs.append(int(row[5]))
    # this will grab the high temperates from the file.
    # 5 is the index value for all high temperates


# print(highs)

######################################

# Plot the highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()

fig.autofmt_xdate()


plt.plot(dates, highs, c="red")
# this expects a list, in this case "Highs"
plt.title("daily high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)


plt.show()