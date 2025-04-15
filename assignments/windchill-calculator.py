#I added a loop to ensure the user only selects the temperature in either C or F

def calculate_windchill(t, v):
    windchill = 35.74 + 0.6215 * t - 35.75 * (v**0.16) + 0.4275 * t * (v**0.16)
    return windchill

def convert_c_to_f(celcius):
    return (celcius * 9/5) + 32


temp = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").lower()
wind_speed = 5

while unit !="c" and unit !="f":
    print("Please select either C or F")
    unit = input("Fahrenheit or Celsius (F/C)? ").lower()

if unit=="c":
    temp = convert_c_to_f(temp)

while wind_speed < 65:
    wind_chill = calculate_windchill(temp, wind_speed)

    print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

    wind_speed +=5
