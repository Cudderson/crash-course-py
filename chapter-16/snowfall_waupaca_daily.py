import csv

from datetime import datetime

from matplotlib import pyplot as plt

"""Examining snowfall for Waupaca, WI from December 1 2020 - January 23 2021"""

filename = '../data-vis-intro/2424405.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)

    wau_dates, snowfall_for_dates = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            daily_snow = float(row[4])
        except ValueError:
            print(f"invalid information for date {current_date}. date data excluded.")
        else:
            wau_dates.append(current_date)
            snowfall_for_dates.append(daily_snow)

    print(snowfall_for_dates)

# Creating visualization
# plotting dates/snowfall

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(wau_dates, snowfall_for_dates, c='blue')

plt.title("Waupaca Snowfall, Dec 1 2020 - Jan 23 2021", fontsize=20)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Daily Snowfall (in)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
