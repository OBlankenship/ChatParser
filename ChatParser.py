def chat_parser():
    contents = []  # Contains lines of chat to be parsed
    print("Enter chat to parse (Press enter to begin parsing): ")
    # Adds the lines of chat to the contents list
    while True:
        line = input()
        if line == "":
            break
        contents.append(line)
    entries_dict = {}  # Contains players and their associated rolls
    for item in contents:
        words = item.split()
        # Adds all players/rolls to the entries_dict.
        if words[0] == "Random!":
            number_rough = words[5]
            number = number_rough.split(".")[0]
            player_name = words[1] + words[2]
            # Checks for duplicate rolls and ignores them
            if player_name in entries_dict:
                print("Duplicate roll detected for " + player_name + "! Ignoring second roll.")
            else:
                entries_dict[player_name] = number
    # Prompts (and validates the input) for high or low roll
    while True:
        print("High (H) or Low (L) roll?: ")
        high_low = input()
        if high_low.upper() == "H":
            winner = max(entries_dict, key=entries_dict.get)
            winning_number = max(entries_dict.values())
            break
        elif high_low.upper() == "L":
            winner = min(entries_dict, key=entries_dict.get)
            winning_number = min(entries_dict.values())
            break
        else:
            print("Invalid Input!")
    # Prints the winner
    print("Winner: " + winner + " with a roll of " + winning_number)


# Driver for the chat parser.
while True:
    chat_parser()

