input_hours = input("Enter Hours: ")
hours = float(input_hours)

input_rate = input("Enter Hourly Rate: ")
rate = float(input_rate)

if hours <= 40:
    payment = hours * rate
else:
    normal_rate = 40 * rate
    overtime_rate = (hours-40) * (1.5 * rate)
    payment = normal_rate + overtime_rate

print(payment)
