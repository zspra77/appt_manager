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
    print(' 1) Schedule appoint.')
    print(' 2) Find appoint. by name')
    print(' 3) Print calender for specific day')
    print(' 4) Cancel appoint.')
    print(' 5) Change appoint.')
    print(' 6) Calculate total fees for a day')
    print(' 7) Calculate total weekly fees')
    print(' 9) Exit')
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
        print(f'{'Client Name'} {'Phone':>10} {'Day':>10} {'Start':>15} {'End':>15} {'Type':>10}')
        print('_' * 76)
        print('No appointments found . . . ')

    elif name in addedName:

        print(f'Appointments for {name} . . .')
        print(f'{'Client Name'} {'Phone':>10} {'Day':>10} {'Start':>15} {'End':>15} {'Type':>10}')
        print('_' * 76)
        #ENTER STATUS FOR VALID 



def cancel_appoint(time):

    if time in addedTime and day in addedDay:
        index = addedName.index(addedTime)
        addedDay.remove(addedDay)
        addedPhone.pop(index)
        addedType.pop(index)
        addedTime.pop(index)
        addedName.pop(index)

        print(f'{addedDay} {addedTime} for {addedName.index(index)} has been removed!')

    else:

        print(f'Time slot is not appointed!')



def day_charges():
    
    if not addedCost:
        print("No charges to display.")

    else:

        print(f'Appointments for . . .')
        print(f'{'Client Name'} {'Phone':>10} {'Day':>10} {'Start':>15} {'End':>15} {'Type':>10}')
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
            file.write(f"{'License Plate':<15}{'Credit Card':<20}{'Hours':<8}{'Charge':<8}\n")
            file.write("-" * 60 + "\n")
            total_charges = 0
            for i in range(len(addedName)):
                plate = addedName[i]
                creditNum = addedDay[i]
                hours = addedTime[i]
                fee = addedPhone[i]
                type = addedType[i]
                file.write(f"{plate:<15}{creditNum:<20}{hours:<8.1f}${fee:<8.2f}\n")
                total_charges += fee
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
            print(addedName)
 
    elif userinput == 2:

        name = input('Enter Name: ')
        find_appoint_by_name(name)
 
    elif userinput == 3:  
        #PRINT SCHEDULE
        []
 
    elif userinput == 4:
        cancel_appoint()
 
    elif userinput == 5: 
        #CHANGE APPOINT
        []
 
    elif userinput == 6:  
        day_charges()
 
    elif userinput == 7:
        #WEEKLY CHARGES
        []
    
    elif userinput == 9:  
        print('System Shutting down . . .')
        print('Thank you and goodbye! : )')
        break
 
    else:
        print('')
        print('Invalid option, please try again.')
        print('')