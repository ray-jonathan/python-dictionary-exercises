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

def get_in_or_out(guest_reply):
    while (guest_reply != "OUT") and (guest_reply != "IN"):
        guest_reply = input("Your answer is not clear. Please provide an answer of \"in\" or \"out\" ").upper()
    guest_room = input("Splendid. What is the room number on your reservation? ")
    while ((len(guest_room) != 3) or int(guest_room[0]) > 3)  or (not guest_room.isdigit()):
        guest_room = input("That is not a valid room number. Our room numbers are three digits long, starting with 1 through 3. What is the room number on your reservation? ")
    return guest_room

room_num = get_in_or_out(input("Goodday, are you read to check in or out? ").upper())
floor_num = room_num[0]
# taken_rooms = []
# for room in hotel[floor_num]:
#     taken_rooms.append(room)

while room_num not in hotel[floor_num]:
    

# If checking in, ask for the number of occupants and what their names are.
if (guest_input == "IN") and (room_num not in taken_rooms):
    guest_num = (input("Great, and how many people are on that reservation? "))
    while (not guest_num.isdigit()):
        guest_num = input("That is not a valid number. What is the number of guests on your reservation? ")
    guest_num = int(guest_num)
    guest_names.append(input("Oh, I'm sorry, I didn't catch your name...? "))
    if guest_num > 1:
        for guests in range(guest_num-1):
            guest_names.append(input("What is the name of another guest on the reservation? "))
    print("Thank you. Your room is now ready. ")
    hotel[floor_num][room_num] = guest_names

# Do not allow anyone to check into a room that is already occupied.
elif (guest_input == "IN") and (room_num in taken_rooms):
    print("I'm sorry, that room is taken. Please check your room number and try again. ")

# If checking out, remove the occupants from that room.
elif (guest_input == "OUT") and (room_num in taken_rooms):
    print("Thank you, you are checked out. Please come again soon! ")
    del hotel[floor_num][room_num]

# Do not allow checking out of a room that isn't occupied.
elif (guest_input == "OUT") and (room_num not in taken_rooms):
    print("I'm sorry, that room isn't occupied. Please check your room number and try again. ")
