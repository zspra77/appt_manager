addedName = []
addedDay = []
addedTime = []  
addedCost = []
addedPhone = []
addedType = []




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
    print(f"OK, {name}'s appointment is booked!")
    addedDay.append(day)
    addedTime.append(time)
    addedName.append(name)
    addedPhone.append(phone)
    addedType.append(type)

def find_appoint_by_name(name):
    if name not in addedName:
        print(f'Appointments for {name} . . .')
        print(f'{"Client Name"} {"Phone":>10} {"Day":>10} {"Start":>15} {"End":>15} {"Type":>10}')
        print('_' * 76)
        print('No appointments found . . . ')
    elif name in addedName:
        print(f'Appointments for {name} . . .')
        print(f'{"Client Name"} {"Phone":>10} {"Day":>10} {"Start":>15} {"End":>15} {"Type":>10}')
        print('_' * 76)
        # Add logic to display valid appointments here

def cancel_appoint(day, time):
    index = addedTime.index(time)
    print(f'Schedule for {day} at {time} has been removed!')
    addedDay.pop(index)
    addedPhone.pop(index)
    addedType.pop(index)
    addedTime.pop(index)
    addedName.pop(index)

def day_charges():
    if not addedCost:
        print("No charges to display.")
    else:
        print(f'Appointments for . . .')
        print(f'{"Client Name"} {"Phone":>10} {"Day":>10} {"Start":>15} {"End":>15} {"Type":>10}')
        print('_' * 76)
        total_charges = 0
        for i in range(len(addedName)):
            fee = addedCost[i]
            total_charges += fee
        print(f"Total Daily Charge ${total_charges}")

def save_daily_charges_to_file():
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



while True:
    input("Please press enter to continue....")
    main()

    userinput = int(input('>>> '))
 
    if userinput == 1:
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
            print(addedName, addedDay, addedTime)
 


    elif userinput == 2:
        name = input('Enter Name: ')
        find_appoint_by_name(name)
 
    elif userinput == 3:  
        # Print calendar for specific day
        day = input('Enter the day for which you want to see the schedule: ')
        if day not in addedDay:
            print(f'No appointments scheduled for {day}.')
        else:
            print(f'Schedule for {day}:')
            print(f"{'Time':<10}{'Client Name':<15}{'Phone':<15}{'Type':<15}")
            print('-' * 50)
            for i in range(len(addedDay)):
                if addedDay[i] == day:
                    appt_type = ['Available', 'Mens Cut', 'Ladies Cut', 'Mens Colouring', 'Ladies Colouring']
                    start_time = f"{addedTime[i]}:00"
                    end_time = f"{addedTime[i] + 1}:00"
                    print(f"{start_time:<10}{addedName[i]:<15}{addedPhone[i]:<15}{appt_type[addedType[i]]:<15}")



    elif userinput == 4:
        day = input('What day: ')
        time = int(input('Start hour: '))
        if day in addedDay and time in addedTime:
            cancel_appoint(day, time)
        else:
            print(f'Time slot is not appointed!')
 
    elif userinput == 5: 
        # Placeholder for change appointment
        pass
 
    elif userinput == 6:  
        day_charges()
 
    elif userinput == 7:
        # Placeholder for weekly charges
        pass
    
    elif userinput == 9:  
        print('System Shutting down . . .')
        print('Thank you and goodbye! : )')
        break
 
    else:
        print('')
        print('Invalid option, please try again.')
        print('')

