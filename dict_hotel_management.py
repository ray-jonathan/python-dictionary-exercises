# Let's imagine that you're running a hotel, and you want to keep 
# track of guests by floor and room number:

# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.


hotel = { '1': {'101': ['George Jefferson', 'Wheezy Jefferson'],}, '2': {'237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}



# Display a menu asking whether to check in or check out.

guest_input = input("Hello, would you like to check-in or check-out? (IN or OUT) ").upper()
while (guest_input != "OUT") and (guest_input != "IN"):
    return ("I cannot help you at this time. Check your answer and try again later.")
    guest_input = input("Would you like to check-in or check-out? (IN or OUT) ").upper()
# Prompt the user for a floor number, then a room number.

guest_room = str(input("Excellent! Please remind me of your room number... "))
guest_floor = guest_room[0]


# If checking in, ask for the number of occupants and what their names are.
guest_names_list = []
if guest_input == "IN":
    for room in hotel[guest_floor]:
        # Do not allow anyone to check into a room that is already occupied.
        if room == guest_room:
            return ("Oh no, I believe you may be mistaken. That room is already occupied!")
            quit()
    guest_num = int(input("How many guests are in your room? "))
    if guest_num == 1:
        guest_names = input("Wonderful! What was your name again? ")
        guest_names_list = [guest_names]
    if guest_num > 1:
        guest_names = input("Wonderful! What was your name again? ") + ";"
        for guests in range(guest_num-1):
            guest_names += input("Who else? ") + ";"
        guest_names = guest_names[0:len(guest_names)-1]
        guest_names_list = guest_names.split(";")
# # # Cannot add guests at this time


# If checking out, remove the occupants from that room.
if guest_input == "OUT" :
    try:
        if hotel[guest_floor][guest_room] in (hotel[guest_floor].values()):
            return ("We're sorry to see you go! We hope you'll visit again soon.")
            del hotel[guest_floor][guest_room]
# Do not allow checking out of a room that isn't occupied.
    except KeyError:
        return ("Oh no, I believe you may be mistaken. That room isn't occupied!")
