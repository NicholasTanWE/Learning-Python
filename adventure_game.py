# variables to hold state of entire game:
player_position=0 # This says what room number the player is currently in
got_key=False # This is true when the player has picked the key up and false otherwise.
items_held=[] # This is a list of items the player has picked up
item_locations={
    "golden key": 2, # This is the room where the golden key is located
    "treasure chest": 4, # This is the room where the treasure chest is located
} 
# This is a list of the rooms where items are located
def get_location_description(location_number):
    if location_number==0:
        return("You are in the entrance hall of a mansion.\nTo continue through the mansion head east (E).")
    elif location_number==1:
        return("You are in the main corridor. It stretches out before you.\nYou can go East or West (E or W).")
    elif location_number==2:
        return("You are standing in a huge dining area.\nYou can go East or West (E or W).")
    elif location_number==3:
        return("You are plain-looking room. There is a secret door at the back,\nbut you need a key to open it.\nYou can go East or West (E or W).")
    elif location_number==4:
        return("You are in a magnificent throne room, at the far end of the house.\nYou can only head west (W) from here.")
    return "x" 
    
# main game loop.  Continues forever until a break statement is reached:
while True:
    print("DEBUG MESSAGE: ","player_position=",player_position,"items held=",items_held, "item locations=",item_locations, sep=" ")
    print(get_location_description(player_position))
    if player_position==item_locations["golden key"]: #logic for printing golden key
        print("There is a golden key on the floor.")
    if player_position==item_locations["treasure chest"]: #logic for printing treasure chest
        print("There is a treasure chest here, but it is locked.")
    user_command=input("What do you want to do next?").lower()

    if user_command=="quit": #logic for Quit
        break
    elif user_command=="get key": #logic for picking up the key:
        if "golden key" not in items_held and player_position==item_locations["golden key"]:
            print("You now have the golden key.")
            item_locations["golden key"]="n/a"
            items_held.append("golden key")
        else:
            print("There is no golden key here.")
    elif user_command=="drop key":
        if "golden key" in items_held:
            print("You have dropped the key.")
            items_held.remove("golden key")
            item_locations["golden key"]=player_position
        else:
            print("You do not have the key.")
    elif user_command=="e": #move east logic
        if player_position==4:
            print("Your way is blocked.")
        else:
            player_position+=1
    elif user_command=="w": #move west logic
        if player_position==0:
            print("Your way is blocked.")
        else:
            player_position-=1   
    elif user_command=="open door": #win logic
        if player_position==3 and got_key==True:
            print("Congratulations, you have won!")
            break
        elif player_position==3 and got_key==False:
            print("You do not have the key.")
    else:
        print("I don't understand that command.") #logic for unknown command
    print() # print a blank line to separate each game step