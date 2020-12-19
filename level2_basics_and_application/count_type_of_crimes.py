"""
Task-3.4.1
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
"""

import csv
from datetime import datetime, timedelta
from os import path

crimes_in_2015 = []
crimes_file_path = path.join(".", "file_samples", "Crimes.csv")
date_start = datetime(2015, 1, 1)
date_end = date_start + timedelta(days=365)
count_crime_types = {}

with open(crimes_file_path) as crimes_file:
    reader_crimes = csv.DictReader(crimes_file)
    for row in reader_crimes:
        if date_start <= datetime.strptime(row["Date"], "%m/%d/%Y %I:%M:%S %p") <= date_end:
            if row["Primary Type"] not in count_crime_types:
                count_crime_types[row["Primary Type"]] = 0
            count_crime_types[row["Primary Type"]] += 1

print(count_crime_types)
print(sorted(count_crime_types.values()))
