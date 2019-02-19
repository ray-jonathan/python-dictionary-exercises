import time

hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

# an easy thank you statement and simple taken room function
def Thanks():
    print('Thank you!')


# Display a menu asking whether to check in or check out.
print('Welcome to Hotel California! We are here to serve your every need')
time.sleep(.5)

asking = True
while asking:
    print('Will you be checking in or checking out?')
    in_out_status = input('please enter[IN or OUT] ').upper()
    if in_out_status == 'IN' or in_out_status == 'OUT':
        Thanks()
        asking = False
    else:
        print("Im sorry, I do not understand your response...")


# Prompt the user for a floor number, then a room number. and add room to list

def ask_room():
    asking = True
    while asking:
        time.sleep(.5)
        global room_num
        room_num = input('What room is on your reservation? ')
        while (len(room_num) == 3 and room_num.isdigit()):
            if room_num[0] == '1' or room_num[0] == '2' or room_num[0] == '3':
                global floor_num
                floor_num = room_num[0]
                global taken_rooms
                taken_rooms = []
                for room in hotel[floor_num]:
                    taken_rooms.append(room)
                asking = False
                break
            else:
                print('I am sorry I dont understand, please give me a 3 digit room number starting with 1-3')
                break
        else:
            print('I am sorry I dont understand, please give me a 3 digit room number starting with 1-3')

ask_room()


# If checking in, ask for the number of occupants and what their names are.
# Do not allow anyone to check into a room that is already occupied.
def check_in ():
    asking = True
    while asking:
        if room_num not in taken_rooms:
            guest_num = int(input('How many guests will be checking in? '))
            guests= []
            for guest in range(guest_num):
                name =  input('Guest name: ')
                guests.append(name)
                hotel[floor_num][room_num] = guests
            taken_rooms.append(room_num)
            time.sleep(.5)
            print('Thank you, I hope you enjoy your stay! Please let us know if there is anyting we can do to make your stay even more amazing')
            asking = False
        else:
            print('sorry that rooms taken')
            ask_room()
            check_in()
            break
            

if in_out_status == 'IN':
    check_in()


# If checking out, remove the occupants from that room.
# Do not allow checking out of a room that isn't occupied.
def check_out():
    asking = True
    while asking:
        if room_num in taken_rooms:
            print('I hope you ejoyed your stay with us here at Hotel California')
            time.sleep(.5)
            del hotel[floor_num][room_num]
            taken_rooms.remove(room_num)
            print('You have officially been checked out. We hope to see you soon!')
            asking = False
        else:
            print('I am sorry there is no one in that room!')
            ask_room()
            check_out()
            break

if in_out_status == 'OUT':
    check_out()

print(hotel)