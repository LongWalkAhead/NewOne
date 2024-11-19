attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if venue == "large hall":
    print("projector is needed")
else: venue == "conference room"
print("audio device")
menu = input("veggie? yes/no?")
food =  "Veggie Delight Caterers" if menu == "yes" else "Gourmet Meals Catere"
print(food)