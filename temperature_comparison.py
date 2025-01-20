# Program to compare temperatures of two cities

city_a_temp = float(input("Enter the temperature of City A (in Celsius): "))
city_b_temp = float(input("Enter the temperature of City B (in Celsius): "))

if city_a_temp > city_b_temp:
    print("City A is hotter than City B.")
elif city_a_temp < city_b_temp:
    print("City A is cooler than City B.")
else:
    print("City A and City B have the same temperature.")
