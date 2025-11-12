#Name: Khushi Panwar
# Date: 07 November 2025
# Assignment Title: Attendance Tracker System

from datetime import datetime   # For getting current date and time

# Welcome message
print("===========================================")
print(" Welcome to the Attendance Tracker System ")
print("===========================================")
print("This tool helps record and manage student attendance.")
print("You can add, view, and summarize attendance records easily!")
print()

# Ask number of entries
num_entries = int(input("How many attendance entries do you want to record?"))

# Create dictionary to store attendance
attendance = {}

# Loop to collect data
for i in range(num_entries):
    print(f'\nEntry{i+1}')
    # Get student name and validate
    while True:
        name = input("Enter the Student Name:").strip()
        if name == "":
            print("Name cannot be empty.Please enter a valid name.")
        elif name in attendance:
            print("This student's name already exists.Please enter a different name. ")
        else:
            break       #valid name entered
    
    # Get check-in time and validate
    while True:
        time = input("Enter check-in time:").strip()
        if time == "":
            print("Check-in time cannot be empty.Please re-enter the time")
        else:
            break   #valid time entered
    attendance[name] = time


# Ask for total class strength
total_students = int(input("\nEnter total number of students in the class: "))

# Calculate attendance summary
total_present = len(attendance)
total_absent = total_students - total_present

print("\n\n\tATTENDANCE SUMMARY")
print("\t----------------------------")
print(f"{'Student Name':<20}\t{'Check-in Time'}")
print("\t------------------------------------------")

# Display each record using f-string formatting
for name, time in attendance.items():
    print(f"\t{name:<20}\t{time}")

print("\t--------------------------------------")
print(f"\n\tTotal Students in Class: {total_students}")
print(f"\tTotal Present:           {total_present}")
print(f"\tTotal Absent:            {total_absent}")
print("\n\tThank you for using the Attendance Tracker!\n")

save_option = input("Would you like to save this attendance record? (yes/no): ").strip().lower()

if save_option in ['yes', 'y']:
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open file for writing
    with open("attendance_log.txt", "w") as file:
        file.write("ATTENDANCE REPORT\n")
        file.write("--------------------------------------\n")
        file.write(f"{'Student Name':<20}\tCheck-in Time\n")
        file.write("--------------------------------------\n")
        for name, time in attendance.items():
            file.write(f"{name:<20}\t{time}\n")
        file.write("--------------------------------------\n")
        file.write(f"\nTotal Students in Class: {total_students}\n")
        file.write(f"Total Present:           {total_present}\n")
        file.write(f"Total Absent:            {total_absent}\n")
        file.write(f"\nReport Generated On: {current_time}\n")
        file.write("--------------------------------------\n")
        print("\n Attendance successfully saved to 'attendance_log.txt'!")
else:
    print("\n Record not saved. Exiting program.")