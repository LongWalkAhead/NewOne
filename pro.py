place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: action == "cross a river"
    print("You found a boat!")
elif place == "cave": #task2
    print("You find a hidden treasure!")
    cave = input("go in the dark or light a torch?")
    if cave == "go in the dark":
        print("be wary, traveler!")
    else: cave == "light a torch"
    print("you light a torch a proceed forward!")