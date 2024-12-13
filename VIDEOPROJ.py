# Initialize lists
addedName = ['Gabriela', 'Tyler', 'Stephanie']
addedDay = ['Thursday', 'Saturday', 'Saturday']
addedTime = [13, 9, 10]
addedCost = [80, 40, 60]
addedPhone = ['368-111-9999', '587-123-4567', '368-999-1111']
addedType = [4, 3, 2]
# Validate the input day
valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
 
 
 
 
 
# Display startup interface at the start and when option is fulfilled
def main():
    print("=" * 31)
    print('Hair Salon Appointment Manager!')
    print("=" * 31)
    print(' 1 Schedule appoint.')
    print(' 2 Find appoint. by name')
    print(' 3 Print calendar for specific day')
    print(' 4 Cancel appoint.')
    print(' 5 Change appoint.')
    print(' 6 Calculate total fees for a day')
    print(' 7 Calculate total weekly fees')
    print(' 9 Exit')
    print("=" * 31)
 
 
 
 
 
def schedule_appoint(day, time, name, phone, type):
    # Define costs for each appointment type
    cost_mapping = {
        1: 40.00,  # Mens Cut
        2: 60.00,  # Ladies Cut
        3: 40.00,  # Mens Colouring
        4: 80.00   # Ladies Colouring
    }
    cost = cost_mapping.get(type, 0)  # Default cost is 0 if type is invalid
    addedDay.append(day)
    addedTime.append(time)
    addedName.append(name)
    addedPhone.append(phone)
    addedType.append(type)
    addedCost.append(cost)  # Add the cost to the list
    print(f"OK, {name}'s appointment is booked! Cost: ${cost:.2f}")
 
 
 
 
 
def find_appoint_by_name(name):
    # Checks if name is currently registered successfully
    if name not in addedName:
        print(f"Appointments for {name} . . .")
        print(f"{'Client Name':<15} {'Phone':<15} {'Day':<10} {'Start':<10} {'End':<10} {'Type':<20}")
        print('-' * 80)
        print("No appointments found.")
    else:
        print(f"Appointments for {name} . . .")
        print(f"{'Client Name':<15} {'Phone':<15} {'Day':<10} {'Start':<10} {'End':<10} {'Type':<20}")
        print('-' * 80)
 
        appt_types = {
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
 
        # Loop through all appointments and display matching ones
        for i in range(len(addedName)):
            if addedName[i] == name:
                start_time = f"{addedTime[i]}:00"
                end_time = f"{addedTime[i] + 1}:00"  # Assuming the appointment lasts 1 hour
                appt_type = appt_types.get(addedType[i], "Unknown")
                print(f"{addedName[i]:<15} {addedPhone[i]:<15} {addedDay[i]:<10} {start_time:<10} {end_time:<10} {appt_type:<20}")
 
 
 
 
def cancel_appoint(day, time):
    # Once all inputs are valid, successfully remove appointment details from all lists
    index = addedTime.index(time)
    print(f'Schedule for {day} at {time} has been removed!')
    addedDay.pop(index)
    addedPhone.pop(index)
    addedType.pop(index)
    addedTime.pop(index)
    addedName.pop(index)
 
 
 
 
def display_calendar_for_day(day):
    # If no one is registered for the day, print empty message, otherwise print all appointments pending.
    if day not in addedDay:
        print(f"No appointments scheduled for {day}.")
    else:
        print(f"Schedule for {day}:")
        print(f"{'Time':<10}{'Client Name':<15}{'Phone':<15}{'Type':<20}")
        print('-' * 60)
        for i in range(len(addedDay)):
            if addedDay[i] == day:
                appt_type = ['Available', 'Mens Cut', 'Ladies Cut', 'Mens Colouring', 'Ladies Colouring']
                start_time = f"{addedTime[i]}:00"
                end_time = f"{addedTime[i] + 1}:00"
                print(f"{start_time:<10}{addedName[i]:<15}{addedPhone[i]:<15}{appt_type[addedType[i]]:<20}")
 
 
 
 
def day_charges():
    # If no appointments are registered, or closed days are inputted, print no appt message, otherwise, print costs.
    if not addedDay:
        print("No appointments scheduled for any day.")
    else:
        day = input("Enter the day to calculate charges for: ")
       
        if day not in valid_days:
            if day == "Sunday":
                print("The salon is closed on Sundays.")
            else:
                print("Invalid day entered. Please enter a valid day of the week.")
        elif day not in addedDay:
            print(f"No appointments scheduled for {day}.")
        else:
            total_charges = sum(addedCost[i] for i in range(len(addedDay)) if addedDay[i] == day)
            print(f"Total Charges for {day}: ${total_charges:.2f}")
 
 
 
 
def save_daily_charges_to_file():
    #save to file if appointments are registered.
    if not addedName:
        print("No charges to save.")
    else:
        with open("appointments1.csv", "w") as file:
            file.write("----- Charges -----\n")
            file.write(f"{'Client Name':<15}{'Phone':<20}{'Day':<8}{'Start':<8}{'Type':<8}\n")
            file.write("-" * 60 + "\n")
            total_charges = 0
            for i in range(len(addedName)):
                name = addedName[i]
                day = addedDay[i]
                start_time = addedTime[i]
                phone = addedPhone[i]
                appt_type = addedType[i]
                file.write(f"{name:<15}{phone:<20}{day:<8}{start_time:<8}{appt_type:<8}\n")
                total_charges += addedCost[i] if i < len(addedCost) else 0
            file.write("-" * 60 + "\n")
            file.write(f"{'Total Daily Charges':<43}${total_charges:<8.2f}\n")
            file.write("-------------------------\n")
        print("Charges have been successfully saved to 'appointments1.csv'.")
 
 
 
 
def weekly_charges():
    # Print charge total in the whole week if appointments are registered.
    if not addedCost:
        print("No appointments scheduled for the week.")
    else:
        total_weekly_charges = sum(addedCost)
        print(f"Total Weekly Charges: ${total_weekly_charges:.2f}")
 
 
# Initiate loop until option 9 (exit) is chosen.
while True:
    input("Please press enter to continue....")
    main()
    
    # Ask for user choice
    userinput = int(input('>>> '))
 
    if userinput == 1:
        # Appoint. registration undergoes valid or invalid process based on inputs
        day = input('What day: ')
        while day not in valid_days:
            day = input('What day: ')
        time = int(input('Enter start hour (Between 9AM and 16PM): '))
        while time > 16 or time < 9:
            time = int(input('Invalid, not in time slot! Try again: '))
        if day in addedDay and time in addedTime:
            print(f'Sorry, time slot has been taken!')
        else:
            name = input('Name: ')
            phone = (input('Phone number: '))
            print('Appoint. types:')
            print('1: Mens haircut 2: Ladies haircut 3: Mens Coloring 4: Ladies Coloring')
            type = int(input('>>> '))
            schedule_appoint(day, time, name, phone, type)
    
    # Ask user for name to verify
    elif userinput == 2:
        name = input('Enter Name: ')
        find_appoint_by_name(name)
 
    # Ask user for day to view on calendar
    elif userinput == 3:
        day = input('Enter the day for which you want to see the schedule: ')
        display_calendar_for_day(day)
    
    # Cancel appoint. based on day and time, if registered, remove from appointments
    elif userinput == 4:
        day = input('What day: ')
        time = int(input('Start hour: '))
        if day in addedDay and time in addedTime:
            cancel_appoint(day, time)
        else:
            print(f'Time slot is not appointed!')
    
    # Verify the old time, and replace it if time slot is available
    elif userinput == 5:
        old_day = input("Enter the current appointment day: ")
        old_time = int(input("Enter the current appointment start hour: "))
        if old_day in addedDay and old_time in addedTime:
            index = addedDay.index(old_day)
            if addedTime[index] == old_time:
                new_day = input(("Enter the new appointment: "))
                new_time = int(input("Enter the new appointment start hour (Between 9AM or 16PM)"))
                while new_time > 16 or new_time < 9:
                    new_time = int(input("Invalid, not in the time slot! Try again: "))
                if new_day in addedDay and new_time in addedTime:
                    print("Sorry, the new time slot is already taken!")
                else:
                    addedDay[index] = new_day
                    addedTime[index] = new_time
                    print(f"Appointment successfully moved to {new_day} at {new_time}:00.")
            else:
                print("Appointment not found for the specific time.")
        else:
            print("No appointment found to change.")
    
    # Call function when 6 is user choice
    elif userinput == 6:
        day_charges()
    
    # Call function when 7 is user choice
    elif userinput == 7:
        weekly_charges()
 
    # Exit system, but ask user if he/she wants to save current appointments to file.
    elif userinput == 9:
        print('* * Exit System * *')
        save_file = input('Would you like to save all appointments to a file (Y/N): ').capitalize()
        while save_file not in ['Y', 'N']:
            save_file = input('Would you like to save all appointments to a file (Y/N): ').capitalize()
        if save_file == 'Y':
            save_daily_charges_to_file()
        elif save_file == 'N':
            print('System Shutting down . . .')
            print('Thank you and goodbye! : )')
            break
                
    # If user choice is not 1, 2, 3, 4, 5, 6, 7 or 9, print error message.
    else:
        print('')
        print('Invalid option, please try again.')
        print('')

    #END OF PROGRAM