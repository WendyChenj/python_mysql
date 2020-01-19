import csv
import analysis

with open('actual_total_grants.csv', 'w', newline='') as csvfile:
    fieldnames=['year', 'total_grants_every_year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in analysis.count:
        year=i[0]
        # mine=i[1]
        # sum=i[2]
        sum=i[1]
        writer.writerow({'year': year, 'total_grants_every_year':sum})




