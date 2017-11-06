input_hours = input("Enter Hours: ")
input_rate = input("Enter Hourly Rate: ")
try:
    hours = float(input_hours)
    rate = float(input_rate)
except:
    print("There is a error in input!I am going to quit!")
    quit()

if hours <= 40:
    payment = hours * rate
else:
    normal_rate = 40 * rate
    overtime_rate = (hours-40) * (1.5 * rate)
    payment = normal_rate + overtime_rate

print(payment)
