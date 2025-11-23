#Task 1 - Initialization
print("Welcome to my Python Program!! :D")

#Task 2 - Input
hours = input("How many hours did you sleep last night? ")

#Task 3 + 5 - Calculation + Error Handling
try:
    hours = float(hours)
except ValueError:
    print("Please provide a valid number!")
    exit()
monthly_sleep = hours * 30

#Task 4 - Display
print(f"You sleep an estimated {monthly_sleep} hours of sleep per month.")