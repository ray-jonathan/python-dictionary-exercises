
# Let's imagine that you're running a hotel, and you want to keep track of guests by floor and room number:

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
# Write a program that works with this hotel data:
guest_names = []
# Display a menu asking whether to check in or check out.
guest_input = (input("Are you checking in or checking out? (IN or OUT) ").upper()).strip()
while (guest_input != "OUT") and (guest_input != "IN"):
    guest_input = input("Your answer is not clear. Check your answer and try again. ").upper()
# Prompt the user for a floor number, then a room number.
guest_room = input("Splendid. What is the room number on your reservation? ")
while ((len(guest_room) != 3) or int(guest_room[0]) > 3)  or (not guest_room.isdigit()):
    guest_room = input("That is not a valid room number. What is the room number on your reservation? ")
guest_floor = guest_room[0]

# Make a list of taken rooms to compare for later
taken_rooms = []
for room in hotel[guest_floor]:
    taken_rooms.append(room)

# If checking in, ask for the number of occupants and what their names are.
if (guest_input == "IN") and (guest_room not in taken_rooms):
    guest_num = (input("Great, and how many people are on that reservation? "))
    while (not guest_num.isdigit()):
        guest_num = input("That is not a valid number. What is the number of guests on your reservation? ")
    guest_num = int(guest_num)
    guest_names.append(input("Oh, I'm sorry, I didn't catch your name...? "))
    if guest_num > 1:
        for guests in range(guest_num-1):
            guest_names.append(input("What is the name of another guest on the reservation? "))
    print("Thank you. Your room is now ready. ")
    hotel[guest_floor][guest_room] = guest_names

# Do not allow anyone to check into a room that is already occupied.
elif (guest_input == "IN") and (guest_room in taken_rooms):
    print("I'm sorry, that room is taken. Please check your room number and try again. ")

# If checking out, remove the occupants from that room.
elif (guest_input == "OUT") and (guest_room in taken_rooms):
    print("Thank you, you are checked out. Please come again soon! ")
    del hotel[guest_floor][guest_room]

# Do not allow checking out of a room that isn't occupied.
elif (guest_input == "OUT") and (guest_room not in taken_rooms):
    print("I'm sorry, that room isn't occupied. Please check your room number and try again. ")
