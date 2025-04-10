# I added a loop to ensure the user inputs a valid year

# I identified the year and country that has the largest drop and also the largest rise in life expectancy from one year to the next (consecutive years).

import csv

inp_year = ""
country_data = {}

while not inp_year.isnumeric():
    inp_year = input("\nEnter the year of interest: ")
    if not inp_year.isnumeric():
        print("Please input a valid year")

print()

with open("life-expectancy.csv", newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header

    overall_max_expectancy = float('-inf')
    overall_max_exp_country = ""
    overall_max_exp_year = ""

    overall_min_expectancy = float("inf")
    overall_min_exp_country = ""
    overall_min_exp_year = ""

    total_expectancy = 0
    total_countries = 0

    inp_year_max_exp = float('-inf')
    inp_year_min_exp = float("inf")

    inp_year_max_exp_country = ""
    inp_year_min_exp_country = ""

    largest_drop = 0
    drop_country = ""
    drop_year_from = 0
    drop_year_to = 0

    largest_rise = 0
    rise_country = ""
    rise_year_from = 0
    rise_year_to = 0


    for row in reader:
        country = row[0]
        year = int(row[2])
        exp = float(row[3])

        # Overall max/min
        if exp > overall_max_expectancy:
            overall_max_expectancy = exp
            overall_max_exp_country = country
            overall_max_exp_year = year

        if exp < overall_min_expectancy:
            overall_min_expectancy = exp
            overall_min_exp_country = country
            overall_min_exp_year = year

        # Year-specific data
        if str(year) == inp_year:
            total_expectancy += exp
            total_countries += 1
            if exp > inp_year_max_exp:
                inp_year_max_exp = exp
                inp_year_max_exp_country = country
            if exp < inp_year_min_exp:
                inp_year_min_exp = exp
                inp_year_min_exp_country = country

        if country not in country_data:
            country_data[country] = []

        country_data[country].append((year, exp))

    for country, records in country_data.items():
        records.sort()  # Sort by year

        for i in range(1, len(records)):
            prev_year, prev_exp = records[i - 1]
            curr_year, curr_exp = records[i]
            
            # Calculate drop and rise in life expectancy for consecutive years
            if prev_year == curr_year - 1:
                drop = prev_exp - curr_exp
                rise = curr_exp - prev_exp

            if drop > largest_drop:
                largest_drop = drop
                drop_country = country
                drop_year_from = prev_year
                drop_year_to = curr_year

            if rise > largest_rise:
                largest_rise = rise
                rise_country = country
                rise_year_from = prev_year
                rise_year_to = curr_year
            
    if total_countries == 0:
        print(f"No data found for the year {inp_year}.")
    else:
        avr_exp = total_expectancy / total_countries

        print(f"The overall max life expectancy is: {overall_max_expectancy} from {overall_max_exp_country} in {overall_max_exp_year}")
        print(f"The overall min life expectancy is: {overall_min_expectancy} from {overall_min_exp_country} in {overall_min_exp_year}")

        print()
        print(f"The largest drop in life expectancy was {largest_drop:.2f} from {drop_year_from} to {drop_year_to} in {drop_country}")
        print(f"The largest rise in life expectancy was {largest_rise:.2f} from {rise_year_from} to {rise_year_to} in {rise_country}")
        print()
        
        print(f"For the year {inp_year}:")
        print(f"The average life expectancy across all countries was {avr_exp:.2f}")
        print(f"The max life expectancy was in {inp_year_max_exp_country} with {inp_year_max_exp}")
        print(f"The min life expectancy was in {inp_year_min_exp_country} with {inp_year_min_exp}")
