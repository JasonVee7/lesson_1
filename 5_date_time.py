import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format and display the current date and time

print(current_datetime)

formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date and Time:", formatted_datetime)
