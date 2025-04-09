inp_year = ""

while not inp_year.isnumeric():
    print("Please input a valid year")
    inp_year = input("\nEnter the year of interest ")

print()

with open("./life-expectancy.csv") as data:
    overall_max_expectancy = 75
    overall_max_exp_country = ""
    overall_max_exp_year = ""

    overall_min_expectancy = 27
    overall_min_exp_country = ""
    overall_min_exp_year = ""

    total_expectancy = 0
    total_countries = 0
    

    inp_year_max_exp = 17
    inp_year_min_exp = 87

    inp_year_max_exp_country = ""
    inp_year_min_exp_country = ""


    header = data.readline()

    for line in data:
        parts = line.strip().split(",")
        country, _, year, exp = parts

        if float(exp) > overall_max_expectancy:
            overall_max_expectancy = float(exp)
            overall_max_exp_country,overall_max_exp_year = [country, year]
            

        if float(exp) < overall_min_expectancy:
            overall_min_expectancy = float(exp)
            overall_min_exp_country,overall_min_exp_year = [country, year]

        if year == inp_year:
            total_expectancy += float(exp)
            total_countries += 1
            if float(exp) > inp_year_max_exp:
                inp_year_max_exp = float(exp)
                inp_year_max_exp_country = country
            if float(exp) < inp_year_min_exp:
                inp_year_min_exp = float(exp)
                inp_year_min_exp_country = country

    avr_exp = total_expectancy/total_countries
            
    print(f"The overall max life expectancy is: {overall_max_expectancy} from {overall_max_exp_country} in {overall_max_exp_year}")

    print(f"The overall min life expectancy is: {overall_min_expectancy} from {overall_min_exp_country} in {overall_min_exp_year}")

    print()

    print(f"For the year {inp_year}:")
    print(f"The average life expectancy across all countries was {avr_exp:.2f}")
    print(f"The max life expectancy was in {inp_year_max_exp_country} with {inp_year_max_exp}")
    print(f"The min life expectancy was in {inp_year_min_exp_country} with {inp_year_min_exp}")
    


        # for i in range(10):
        #     line = data.readline()
        #     parts = line.strip().split(",")
        #     print(parts)

        # ["Afghanistan","AFG",1950,27.638]
        # ["entity","code","year","life expectancy"]