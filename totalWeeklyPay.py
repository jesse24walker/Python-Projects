# total pay = (hourly wage * total hours) + (hours * 1.5)
hourlyWage = float(input("Enter your hourly wage:"))
regularHours = float(input("Enter your total regular hours:"))
overtimeHours = float(input("Enter your total overtime hours:"))

overtime = overtimeHours * (1.5 * hourlyWage)
total_Weekly_Pay = (hourlyWage * regularHours) + overtime

print("My total weekly pay is $", total_Weekly_Pay)
