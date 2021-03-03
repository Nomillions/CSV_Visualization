import csv
from datetime import datetime

print()
print()
print("------------------------------------------------------------")
print("Greetings and welcome to the Temperature Selection Station!")
print("Please type ('Sitka') to view the Sitka temperatures.")
print("    or type ('Death') to view the Death valley temperatures.")
print("------------------------------------------------------------")
print()
response = input("Type response here: \n")

if response == "Sitka":
    open_file = open("sitka_weather_2018_simple.csv", "r")
else:
    open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)  # skips header row


# the enumerate() function returns both the index of each item and the
# value of each item, as you loop through the list


for index, column_header in enumerate(header_row):
    print("Index: ", index, "Column Name: ", column_header)
    MAX = header_row.index("TMAX")
    MIN = header_row.index("TMIN")
    DATE = header_row.index("DATE")
    NAME = header_row.index("NAME")


# allows us to know the index value of each header item


highs = []
lows = []
dates = []

# mydate = "2018-07-01"
# converted_date = datetime.strptime(mydate, "%Y-%m-%d")
# print(converted_date)

# we call strptime() containing the date as the first argument, and the second argument will format the date how we want it.

for row in csv_file:
    try:
        sn = row[NAME]
        high = int(row[MAX])
        low = int(row[MIN])
        converted_date = datetime.strptime(row[DATE], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

    # this will grab the high temperates from the file.
    # 5 is the index value for all high temperates


# print(highs)

######################################

# Plot the highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()

fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.3)


plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
# this expects a list, in this case "Highs"
plt.title(sn, fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)


plt.show()

fig2, a = plt.subplots(2)
a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
