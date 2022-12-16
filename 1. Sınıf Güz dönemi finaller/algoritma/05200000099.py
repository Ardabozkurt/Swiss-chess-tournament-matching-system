# 05200000099 - Arda Bozkurt
# Importing and creating constants
import math
LOWER_BASE = 0  # Limit for ukd and elo points
UPPER_BASE = 1000    # Limit for ukd and elo points
MAX_RESULT = 5  # Limit for match result
MIN_RESULT = 0  # Limit for match result


def gettingValues(players_dict):  # Function that gets values from each player
    point = 0.00    # A variable for assigment
    again = 'y'    # Command for loop
    while again == 'y':  # Loop for each player
        licence_no = int(input("Oyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz):"))    # Getting license no
        if licence_no > LOWER_BASE:     # Checking for no if its bigger than 0
            try:    # Checking for any errors
                while licence_no in players_dict:   # Checking for if there is the same license no in dictionary
                    licence_no = int(input("Oyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz):"))     # If so wants input again
                name = input("Oyuncunun adini-soyadini giriniz:")   # Getting name
                name = name.replace("i", "İ")   # Changing for Turkish letters
                name = name.upper()  # Uppering all letters in text
                elo = int(input("Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0):"))       # Getting ELO
                while elo < UPPER_BASE and elo != LOWER_BASE:   # Checking for elo if its between limits
                    elo = int(input("Oyuncunun ELO’sunu giriniz (en az 1000, yoksa 0):"))   # If not wants input again
                ukd = int(input("Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0):"))   # Getting UKD
                while ukd < UPPER_BASE and ukd != LOWER_BASE:   # Checking for elo if its between limits
                    ukd = int(input("Oyuncunun UKD’sini giriniz (en az 1000, yoksa 0):"))   # If not wants input again
                if licence_no not in players_dict:  # If license no entered first time
                    BSNo = ''   # Creating variable for that license no
                    SNo = ''    # Creating variable for that license no
                    GS = ''     # Creating variable for that license no
                    list = [name, elo, ukd, point, BSNo, SNo, GS]       # Creating a list that contains these variables
                    players_dict[licence_no] = list  # Appending this list to that license no
            except ValueError:   # Creating output for error
                print("HATA!")
            except:     # Creating output for error
                print("HATA!")
        else:
            again = 'n'     # Breaking loop


def startSortedChart(players_dict):     # Function that creates starting chart
    BSNo = 0    # Creating variable for each player
    try:    # Checking for any errors
        sorted_players_dict = sorted(players_dict.items(), key=lambda x: (-x[1][3], -x[1][1], -x[1][2], x[1][0], x[0]))     # Sorting dictionary to the desired order
        print()
        print("Başlangıç Sıralama Listesi:")
        print("BSNo", end=' ')
        print("LNo", end="   ")
        print("Ad-Soyad", end="     ")
        print("ELO", end='  ')
        print("UKD")
        print("----", end=' ')
        print("-----", end=' ')
        print("------------", end=' ')
        print("----", end=' ')
        print("----")
        for i in range(len(players_dict)):  # Creating loop for each player
            BSNo += 1   # Adding value to variable
            sorted_players_dict[i][1][4] = BSNo     # Adding variebles to each player
            print(format(sorted_players_dict[i][1][4], ">4d"), end=' ')
            print(format(sorted_players_dict[i][0], ">5d"), end=' ')
            print(format(sorted_players_dict[i][1][0], "12"), end=' ')
            print(format(sorted_players_dict[i][1][1], ">4d"), end=' ')
            print(format(sorted_players_dict[i][1][2], ">4d"))
    except ZeroDivisionError:   # Creating output for error
        print("HATA!")


def turnList(players_dict, number_of_turn, number_of_players, main_color, side_color):      # Function that creates and calculates each turn
    for key in players_dict:    # Loop for each player
        turnValueKeeper = [["", "", ""] for i in range(number_of_turn)]     # Creating list for each turn
        players_dict[key].append(turnValueKeeper)   # Appending those lists to each player
        endValueKeeper = []     # List for tiebreaker criterias
        players_dict[key].append(endValueKeeper)    # Appending this list to each player
    sorted_players_dict = sorted(players_dict.items(), key=lambda x: (-x[1][3], -x[1][1], -x[1][2], x[1][0], x[0]))     # Sorting dictionary to the desired order
    for i in range(len(sorted_players_dict)):   # Appending Selected color to odd numbers for starting chart
        if i % 2 == 1:  # Looking for players order odd
            sorted_players_dict[i][1][7][0][1] = side_color     # Adding selected color
        if i % 2 == 0:  # Looking for players order even
            sorted_players_dict[i][1][7][0][1] = main_color     # Adding other color
    for turn_number in range(number_of_turn):  # Loop for each turn
        opponentDict ={}    # List for players point groups
        MSNo = 0    # Table no (variable)
        turnMSNoDict = {}   # Turn table no dictionary
        oddevenplayers = 'even'     # Variable that looks for if total player number is odd or even
        sorted_players_dict = sorted(players_dict.items(), key=lambda x: (-x[1][3], -x[1][1], -x[1][2], x[1][0], x[0]))     # Sorting dict per turn
        if (len(sorted_players_dict) % 2) == 1:     # Checking for total player number is odd
            oddevenplayers = "odd"  # Total player number is odd
            for last_man in range(-1, -(number_of_players + 1), -1):    # Finding BYE passer
                BYE_search = 'y'    # Variable for looking for early turns
                turn_search = 0     # Early turn searching variable
                while BYE_search == 'y' and turn_search <= number_of_turn-1:    # Loop for searching players early turns
                    if sorted_players_dict[last_man][1][7][turn_search][0] == "-":      # If player already passed unmatched or non played  turn
                        BYE_search = 'n'    # Changing variable
                    elif sorted_players_dict[last_man][1][7][turn_search][2] == "+":    # If player already passed unmatched or non played turn
                        BYE_search = "n"    # Changing variable
                    turn_search += 1    # Adding value for loop's functionality
                if BYE_search == 'y':   # If player did'nt pass unmatched or non played turn
                    sorted_players_dict[last_man][1][7][turn_number][0] = "-"   # Passing last man in list unmatched
                    sorted_players_dict[last_man][1][7][turn_number][1] = "-"   # Passing last man in list unmatched
                    sorted_players_dict[last_man][1][7][turn_number][2] = 1     # Adding point
                    break
        for i in range(len(sorted_players_dict)):   # Loop for each player in dict
            point = sorted_players_dict[i][1][3]    # Getting players that turn's point
            if point in opponentDict:   # Looking for that point has already added
                opponentDict[point] += [sorted_players_dict[i]]     # If so adding +1 for counter
            else:   # If not
                opponentDict[point] = [sorted_players_dict[i]]   # Creating that points key in dict
        for player_number in range(number_of_players):      # Loop for every player
            no_need_MSNo = 'n'  # Variable for looks for table no match
            matched = 'n'   # Variable for players match status
            while matched == 'n':   # Matching each player
                go_on = 'y'     # Variable for telling continue or not
                if sorted_players_dict[player_number][1][7][turn_number][0] != "" and sorted_players_dict[player_number][1][7][turn_number][0] != "-":      # Looking for unmatched player
                    no_need_MSNo = 'y'  # Changing variable
                if sorted_players_dict[player_number][1][7][turn_number][0] != "":  # Checking for if player already matched
                    matched = "y"   # Changing variable
                elif sorted_players_dict[player_number][1][7][turn_number][0] == "":    # If player not matched
                    player_search = 0   # Resetting variable
                    opponent_found = 'n'    # Resetting variable
                    while opponent_found == 'n' and player_search <= number_of_players-1:  # Loop for searching opponent for our player
                        for key in opponentDict:    # Splitting dict into players that has same point
                            same_point_counter = len(opponentDict[key])     # Number of  players that  has same point part
                            conditions = 0  # Resetting variable
                            if opponent_found == 'y':    # Looking for if player found opponent
                                break
                            while conditions < 3 and opponent_found == 'n': #Loop for 1.1, 1.2, 1.3 conditions
                                if conditions == 0:   # 1.1 condition
                                    counter = 0     # Resetting variable
                                    already_played = 'n'    # Variable for opponents status
                                    while counter <= same_point_counter-1:      # Player in the same point group loop
                                        if opponent_found == 'y':   # Looking for if player found opponent
                                            go_on = "n"   # Changing variable
                                        if player_number != player_search+counter:  #   Looking for this player is the same with our player
                                            if sorted_players_dict[player_search+counter][1][7][turn_number][0] == "":  # Looking for if opponent already matched that round
                                                for search_turn_opponent in range(turn_number):     # Loop for each turn
                                                    if sorted_players_dict[player_search+counter][1][7][search_turn_opponent][0] == sorted_players_dict[player_number][1][4]:   # Looking for if they already played a match
                                                        already_played = 'y'    # Creating a variable
                                                if already_played == 'n' and go_on != "n":      # Checking for match
                                                    if turn_number == 0:    # If statement for checking turn number
                                                        sorted_players_dict[player_search+counter][1][7][turn_number][0] = sorted_players_dict[player_number][1][4]     # Matching players in first turn
                                                        sorted_players_dict[player_number][1][7][turn_number][0] = sorted_players_dict[player_search+counter][1][4]     # Matching players in first turn
                                                        matched = 'y'   # Changing variable
                                                        opponent_found = 'y'      # Changing variable
                                                    else:
                                                        first_players_color = sorted_players_dict[player_number][1][7][turn_number-1][1]    # Color of our player
                                                        second_players_color = sorted_players_dict[player_search+counter][1][7][turn_number-1][1]   # Color of our player's opponent
                                                        if second_players_color == '-': # If statement for defining other color
                                                            if first_players_color == "b":  # If statement for defining other color
                                                                other_color = 's'   # Defining other color
                                                            elif first_players_color == "s":    # If statement for defining other color
                                                                other_color = 'b'   # Defining other color
                                                        elif first_players_color == '-':    # If statement for defining other color
                                                            if second_players_color == "b": # If statement for defining other color
                                                                other_color = 's'   # Defining other color
                                                            elif second_players_color == "s":   # If statement for defining other color
                                                                other_color = 'b'   # Defining other color
                                                        if first_players_color != second_players_color: # Looking for if player's color are the same
                                                            sorted_players_dict[player_search+counter][1][7][turn_number][0] = sorted_players_dict[player_number][1][4] # Matching players
                                                            sorted_players_dict[player_number][1][7][turn_number][0] = sorted_players_dict[player_search+counter][1][4] # Matching players
                                                            matched = 'y'   # Changing variable
                                                            opponent_found = 'y'    # Changing variable
                                                            if second_players_color == "-":     # Looking for opponents unmatched color
                                                                sorted_players_dict[player_search+counter][1][7][turn_number][1] = first_players_color  # Matching players colors
                                                                sorted_players_dict[player_number][1][7][turn_number][1] = other_color  # Matching players colors
                                                            elif first_players_color == "-":    # Looking for opponents unmatched color
                                                                sorted_players_dict[player_search + counter][1][7][turn_number][1] = other_color    # Matching players colors
                                                                sorted_players_dict[player_number][1][7][turn_number][1] = second_players_color # Matching players colors
                                                            else:   # Looking for opponents unmatched color
                                                                sorted_players_dict[player_search + counter][1][7][turn_number][1] = first_players_color    # Matching players colors
                                                                sorted_players_dict[player_number][1][7][turn_number][1] = second_players_color # Matching players colors

                                        already_played = 'n'    # Changing variable
                                        counter += 1     # Adding +1 for looking for next same point player
                                elif conditions == 1:  # 1.2 condition
                                    counter = 0     # Resetting variable
                                    already_played = 'n'    # Variable for opponents status
                                    while counter <= same_point_counter-1:  # Player in the same point group loop
                                        if opponent_found == 'y':   # Looking for if player found opponent
                                            go_on = "n" # Changing variable
                                        if player_number != player_search + counter:  # Looking for this player is the same with our player
                                            if sorted_players_dict[player_search + counter][1][7][turn_number][0] == "":    # Looking for if opponent already matched that round
                                                for search_turn_opponent in range(turn_number):     # Loop for each turn
                                                    if sorted_players_dict[player_search + counter][1][7][search_turn_opponent][0] == sorted_players_dict[player_number][1][4]: # Looking for if they already played a match
                                                        already_played = 'y'    # Changing variable
                                                if already_played == 'n' and go_on != 'n':  # Checking for match
                                                    first_players_color = sorted_players_dict[player_number][1][7][turn_number - 1][1]  # Defining players color
                                                    second_players_color = sorted_players_dict[player_search + counter][1][7][turn_number - 1][1]   # Defining opponents color
                                                    if first_players_color == second_players_color: # Looking for if player's color are the same
                                                        if sorted_players_dict[player_search+counter][1][7][turn_number-2][1] != second_players_color:  # Looking for if opponents last turn color and current color is the same
                                                            if second_players_color == "b": # If statement for defining other color
                                                                other_color = 's'   # Defining other color
                                                            elif second_players_color == "s":   # If statement for defining other color
                                                                other_color = 'b'   # Defining other color
                                                            sorted_players_dict[player_search + counter][1][7][turn_number][0] = sorted_players_dict[player_number][1][4]   # Matching players
                                                            sorted_players_dict[player_number][1][7][turn_number][0] = sorted_players_dict[player_search + counter][1][4]   # Matching players
                                                            matched = 'y'   # Changing variable
                                                            opponent_found = 'y'    # Changing variable
                                                            sorted_players_dict[player_search + counter][1][7][turn_number][1] = first_players_color    # Matching players colors
                                                            sorted_players_dict[player_number][1][7][turn_number][1] = other_color  # Matching players colors
                                        already_played = 'n'    # Changing variable
                                        counter += 1     # Adding +1 for looking for next same point player
                                elif conditions == 2:  # 1.3 condition
                                    counter = 0     # Resetting variable
                                    already_played = 'n'    # Variable for opponents status
                                    while counter <= same_point_counter-1:  # Player in the same point group loop
                                        if opponent_found == 'y':   # Looking for if player found opponent
                                            go_on = "n" # Changing variable
                                        if player_number != player_search + counter:  # Looking for this player is the same with our player
                                            if sorted_players_dict[player_search + counter][1][7][turn_number][0] == "":    # Looking for if opponent already matched that round
                                                for search_turn_opponent in range(turn_number):     # Loop for each turn
                                                    if sorted_players_dict[player_search + counter][1][7][search_turn_opponent][0] == sorted_players_dict[player_number][1][4]: # Looking for if they already played a match
                                                        already_played = 'y'    # Changing variable
                                                if already_played == 'n' and go_on != 'n':  # Checking for match
                                                    first_players_color = sorted_players_dict[player_number][1][7][turn_number - 1][1]  # Defining players color
                                                    second_players_color = sorted_players_dict[player_search + counter][1][7][turn_number - 1][1]   # Defining opponents color
                                                    if first_players_color == second_players_color: # Looking for if player's color are the same
                                                        if sorted_players_dict[player_number][1][7][turn_number - 2][1] != second_players_color:    # Looking for if player's last turn color and current color is the same
                                                            if second_players_color == "b":  # If statement for defining other color
                                                                other_color = 's'   # Defining other color
                                                            elif second_players_color == "s":   # If statement for defining other color
                                                                other_color = 'b'   # Defining other color
                                                            sorted_players_dict[player_search + counter][1][7][turn_number][0] = sorted_players_dict[player_number][1][4]   # Matching players
                                                            sorted_players_dict[player_number][1][7][turn_number][0] = sorted_players_dict[player_search + counter][1][4]   # Matching players
                                                            matched = 'y'   # Changing variable
                                                            opponent_found = 'y'    # Changing variable
                                                            sorted_players_dict[player_search + counter][1][7][turn_number][1] = other_color    # Matching players colors
                                                            sorted_players_dict[player_number][1][7][turn_number][1] = second_players_color     # Matching players colors
                                        already_played = 'n'    # Changing variable
                                        counter += 1    # Adding +1 for looking for next same point player
                                conditions += 1     # Adding +1 for stepping next condition
                            player_search += same_point_counter # Adding number of same point players to searcher variable
            if oddevenplayers == 'odd':     # Looking for if player number is odd
                for key in turnMSNoDict:    # Loop for each table number
                    if sorted_players_dict[player_number] in turnMSNoDict[key]: # Looking for if player already on a table
                        no_need_MSNo = 'y'  # Changing variable
                if MSNo <= ((number_of_players+1)/2) and no_need_MSNo == 'n':   # Looking for variables match
                    dict_key = 0    # Resetting variable
                    if sorted_players_dict[player_number][1][7][turn_number][0] != "-":  # Looking for players matched condition
                        MSNo += 1   # Changing variable
                        if sorted_players_dict[player_number][1][7][turn_number][1] == "b":  # Looking for color
                            for key in players_dict:    # Loop for each player
                                if players_dict[key][4] == sorted_players_dict[player_number][1][7][turn_number][0]:    # Looking for if players found
                                    dict_key += key  # Adding value to variable
                            turnMSNoDict[MSNo] = sorted_players_dict[player_number], (dict_key, players_dict[dict_key])  # Adding players in order to the table number
                        else:   # Looking for color
                            for key in players_dict:    # Loop for each player
                                if players_dict[key][4] == sorted_players_dict[player_number][1][7][turn_number][0]:     # Looking for if players found
                                    dict_key += key  # Adding value to variable
                            turnMSNoDict[MSNo] = (dict_key, players_dict[dict_key]), sorted_players_dict[player_number]  # Adding players in order to the table number
                    else:
                        turnMSNoDict[int((number_of_players+1)/2)] = sorted_players_dict[player_number]     # Appending last guy to last table
            elif oddevenplayers == 'even':  # Looking if player number is even
                for key in turnMSNoDict:    # Loop for each table number
                    if sorted_players_dict[player_number] in turnMSNoDict[key]:  # Looking for if player already on a table
                        no_need_MSNo = 'y'  # Changing variable
                if MSNo <= (number_of_players/2) and no_need_MSNo == 'n':   # Creating loop for even table
                    MSNo += 1   # Changing variable
                    dict_key = 0    # Resetting variable
                    if sorted_players_dict[player_number][1][7][turn_number][1] == "b":  # Looking for color
                        for key in players_dict:     # Loop for each player
                            if players_dict[key][4] == sorted_players_dict[player_number][1][7][turn_number][0]:    # Looking for if players found
                                dict_key += key     # Adding value to variable
                        turnMSNoDict[MSNo] = sorted_players_dict[player_number], (dict_key, players_dict[dict_key])     # Adding players in order to the table number
                    else:   # Looking for color
                        for key in players_dict:    # Loop for each player
                            if players_dict[key][4] == sorted_players_dict[player_number][1][7][turn_number][0]:    # Looking for if players found
                                dict_key += key     # Adding value to variable
                        turnMSNoDict[MSNo] = (dict_key, players_dict[dict_key]), sorted_players_dict[player_number]     # Adding players in order to the table number
        print(str(turn_number+1) + ". Tur Eşleştirme Listesi:")
        print("        ", end='')
        print("Beyazlar", end='        ')
        print("Siyahlar")
        print("MNo", end=' ')
        print("BSNo", end=' ')
        print(format("LNo", "5"), end=' ')
        print("Puan", end=' ')
        print("-", end=' ')
        print("Puan", end=' ')
        print(format("LNo", "5"), end=' ')
        print("BSNo")
        print("---", end=' ')
        print("----", end=' ')
        print("-----", end=' ')
        print("----", end='   ')
        print("----", end=' ')
        print("-----", end=' ')
        print("----")
        for key in dict(sorted(turnMSNoDict.items(), key=lambda item: item[0])):    # Sorting table dict and looping for each table
            if oddevenplayers == 'odd':  # For odd player number
                if key < int((number_of_players+1)/2):  # Loop for every player except last guy
                    print(format(key, ">3d"), end=' ')
                    print(format(turnMSNoDict[key][0][1][4], ">4d"), end=' ')
                    print(format(turnMSNoDict[key][0][0], ">5d"), end=' ')
                    print(format((turnMSNoDict[key][0][1][3]), ">4"), end=' ')
                    print("-", end=' ')
                    print(format((turnMSNoDict[key][1][1][3]), ">4"), end=' ')
                    print(format(turnMSNoDict[key][1][0], ">5d"), end=' ')
                    print(format(turnMSNoDict[key][1][1][4], ">4d"))
                else:   # For the last guy
                    print(format(key, ">3d"), end=' ')
                    print(format((turnMSNoDict[key][1][4]), ">4"), end=' ')
                    print(format(turnMSNoDict[key][0], ">5"), end=' ')
                    print(format((turnMSNoDict[key][1][3]), ">4"), end='  ')
                    print("-", end=' ')
                    print("BYE")
            else:   # For even player number
                print(format(key, ">3d"), end=' ')
                print(format(turnMSNoDict[key][0][1][4], ">4d"), end=' ')
                print(format(turnMSNoDict[key][0][0], ">5d"), end=' ')
                print(format((turnMSNoDict[key][0][1][3]), ">4"), end=' ')
                print("-", end=' ')
                print(format((turnMSNoDict[key][1][1][3]), ">4"), end=' ')
                print(format(turnMSNoDict[key][1][0], ">5d"), end=' ')
                print(format(turnMSNoDict[key][1][1][4], ">4d"))
        for key in turnMSNoDict:    # Loop for every table number
            if oddevenplayers == 'odd':
                if key != ((number_of_players+1)/2):    # Loop for each table
                    match_result = int(input(str(turn_number+1) + ". turda " + str(key) + ". masada oynanan macin sonucunu giriniz (0-5):"))    # Getting match results
                    while match_result < MIN_RESULT or match_result > MAX_RESULT:   # Looking for if its between in limits
                        match_result = int(input(str(turn_number + 1) + ". turda " + str(key) + ". masada oynanan macin sonucunu giriniz (0-5):"))  # If not wnats input again
                    # Adding values for selected ending result
                    if match_result == 0:
                        turnMSNoDict[key][0][1][3] += 0.5
                        turnMSNoDict[key][0][1][7][turn_number][2] = "½"
                        turnMSNoDict[key][1][1][3] += 0.5
                        turnMSNoDict[key][1][1][7][turn_number][2] = "½"
                    elif match_result == 1:
                        turnMSNoDict[key][0][1][3] += 1
                        turnMSNoDict[key][0][1][7][turn_number][2] = 1
                        turnMSNoDict[key][1][1][7][turn_number][2] = 0
                    elif match_result == 2:
                        turnMSNoDict[key][1][1][3] += 1
                        turnMSNoDict[key][1][1][7][turn_number][2] = 1
                        turnMSNoDict[key][0][1][7][turn_number][2] = 0
                    elif match_result == 3:
                        turnMSNoDict[key][0][1][3] += 1
                        turnMSNoDict[key][0][1][7][turn_number][2] = "+"
                        turnMSNoDict[key][1][1][7][turn_number][2] = "‒"
                    elif match_result == 4:
                        turnMSNoDict[key][1][1][3] += 1
                        turnMSNoDict[key][1][1][7][turn_number][2] = "+"
                        turnMSNoDict[key][0][1][7][turn_number][2] = "‒"
                    elif match_result == 5:
                        turnMSNoDict[key][0][1][7][turn_number][2] = "‒"
                        turnMSNoDict[key][1][1][7][turn_number][2] = "‒"
            else:
                match_result = int(input(str(turn_number + 1) + ". turda " + str(key) + ". masada oynanan macin sonucunu giriniz (0-5):"))  # Getting match results
                while match_result < MIN_RESULT or match_result > MAX_RESULT:   # Looking for if its between in limits
                    match_result = int(input(str(turn_number + 1) + ". turda " + str(key) + ". masada oynanan macin sonucunu giriniz (0-5):"))  # If not wnats input again
                # Adding values for selected ending result
                if match_result == 0:
                    turnMSNoDict[key][0][1][3] += 0.5
                    turnMSNoDict[key][0][1][7][turn_number][2] = "½"
                    turnMSNoDict[key][1][1][3] += 0.5
                    turnMSNoDict[key][1][1][7][turn_number][2] = "½"
                elif match_result == 1:
                    turnMSNoDict[key][0][1][3] += 1
                    turnMSNoDict[key][0][1][7][turn_number][2] = 1
                    turnMSNoDict[key][1][1][7][turn_number][2] = 0
                elif match_result == 2:
                    turnMSNoDict[key][1][1][3] += 1
                    turnMSNoDict[key][1][1][7][turn_number][2] = 1
                    turnMSNoDict[key][0][1][7][turn_number][2] = 0
                elif match_result == 3:
                    turnMSNoDict[key][0][1][3] += 1
                    turnMSNoDict[key][0][1][7][turn_number][2] = "+"
                    turnMSNoDict[key][1][1][7][turn_number][2] = "‒"
                elif match_result == 4:
                    turnMSNoDict[key][1][1][3] += 1
                    turnMSNoDict[key][1][1][7][turn_number][2] = "+"
                    turnMSNoDict[key][0][1][7][turn_number][2] = "‒"
                elif match_result == 5:
                    turnMSNoDict[key][0][1][7][turn_number][2] = "‒"
                    turnMSNoDict[key][1][1][7][turn_number][2] = "‒"
            sorted_players_dict = sorted(players_dict.items(), key=lambda x: (-x[1][3], -x[1][1], -x[1][2], x[1][0], x[0])) # Sorting player dict
        for i in range(len(sorted_players_dict)):   # Loop for each player
            if sorted_players_dict[i][1][7][turn_number][1] == "-":     # Looking for if players found
                sorted_players_dict[i][1][3] += 1.0 # Adding +1 to that player


def endSortedChart(players_dict, number_of_turn):   # Function that creates and calculates ending charts
    SNo = 0     #  Player variable for last chart
    sorted_players_dict = sorted(players_dict.items(), key=lambda x: (-x[1][3], -x[1][1], -x[1][2], x[1][0], x[0]))  # Sorting player dict
    for i in range(len(sorted_players_dict)):   # Loop for each player
        GS = 0  # Resetting variable
        BH_list = []    # Resetting list
        SB_list = []    # Resetting list
        for turn_number in range(number_of_turn):       # Loop for each turn
            if sorted_players_dict[i][1][7][turn_number][2] == 1 or sorted_players_dict[i][1][7][turn_number][2] == "+":    # Looking for each turns ending result
                if sorted_players_dict[i][1][7][turn_number][1] != "-":     # If player didn't pass that turn unmatched
                    GS += 1     # Adding +1 to win counter
                    if sorted_players_dict[i][1][7][turn_number][2] != "+": # Looking for each turns ending result
                        index = sorted_players_dict[i][1][7][turn_number][0]     # Assigning variable for each turn
                        for search in range(len(sorted_players_dict)):  # Loop for each player
                            if index == sorted_players_dict[search][1][4]:  # Looking for if players found
                                SB_list.append(sorted_players_dict[search][1][3])   # Appending value to SB list
            elif sorted_players_dict[i][1][7][turn_number][2] == "½":   # Looking for each turns ending result
                index = sorted_players_dict[i][1][7][turn_number][0]     # Assigning variable for each turn
                for search in range(len(sorted_players_dict)):  # Loop for each player
                    if index == sorted_players_dict[search][1][4]:   # Looking for if players found
                        SB_list.append((sorted_players_dict[search][1][3])/2)   # Appending value to SB list
            if sorted_players_dict[i][1][7][turn_number][2] == "+" or sorted_players_dict[i][1][7][turn_number][1] == "-" or sorted_players_dict[i][1][7][turn_number][2] == "‒":   # Looking for each turns ending result
                total_old_points = 0    # Resetting variable
                for k in range(turn_number-1, -1, -1):  # Loop for each earlier turn that player played
                    old_points = sorted_players_dict[i][1][7][k][2]     # Looking for each earlier turns result
                    if old_points == '½':    # If player ended up with draw changing that result to point form
                        old_points = 0.5    # Draw point
                    if old_points == "+":   # If player ended up with non played match changing that result to point form
                        old_points = 1  # Opponent didn't come
                    if old_points == '‒':   # If player ended up with non played match changing that result to point form
                        old_points = 0  # Player didn't come
                    total_old_points += old_points  #Adding points to total point counter
                adding_nomatch_point = ((number_of_turn-turn_number-1)*0.5 + total_old_points)  # Calculating point that will be added to player for non played turn
                BH_list.append(adding_nomatch_point)    # Appending value to BH list
                if sorted_players_dict[i][1][7][turn_number][2] != "‒": # Looking for each turns ending result
                    SB_list.append(adding_nomatch_point)    # Appending value to SB list
            else:   # Looking for each turns ending result
                index = sorted_players_dict[i][1][7][turn_number][0]
                for search in range(len(sorted_players_dict)):  # Loop for each player
                    if index == sorted_players_dict[search][1][4]:  # Looking for if players found
                        BH_list.append(sorted_players_dict[search][1][3])   # Appending value to BH list
        sorted_players_dict[i][1][6] = GS   # Appending win count
        BH_list.sort()  # Sorting values in Bh list
        BH1_list = BH_list.copy()   # Creating a copy list
        BH1_list.pop(0)     # Popping min value from BH1 list
        BH2_list = BH1_list.copy()  # Creating a copy list
        BH2_list.pop(0)  # Popping min value from BH2 list
        BH1 = sum(BH1_list)  # Calculating tiebreaker criterias
        BH2 = sum(BH2_list)  # Calculating tiebreaker criterias
        SB = sum(SB_list)    # Calculating tiebreaker criterias
        sorted_players_dict[i][1][8].append(BH1)     # Appending tiebreaker criterias
        sorted_players_dict[i][1][8].append(BH2)     # Appending tiebreaker criterias
        sorted_players_dict[i][1][8].append(SB)     # Appending tiebreaker criterias
    sorted_players_dict = sorted(sorted_players_dict, key=lambda x: (-x[1][3], -x[1][8][0], -x[1][8][1], -x[1][8][2]))   # Sorting player dict with tiebreaker criterias
    try:    # Checking for any errors
        print()
        print("Nihai Sıralama Listesi:")
        print("SNo", end=' ')
        print("BSNo", end=' ')
        print("LNo", end="   ")
        print("Ad-Soyad", end="     ")
        print("ELO", end='  ')
        print("UKD", end='  ')
        print("Puan", end=' ')
        print("BH-1", end='  ')
        print("BH-2", end='  ')
        print(format("SB", "5"), end=' ')
        print("GS")
        print("---", end=' ')
        print("----", end=' ')
        print("-----", end=' ')
        print("------------", end=' ')
        print("----", end=' ')
        print("----", end=' ')
        print("----", end=' ')
        print("-----", end=' ')
        print("-----", end=' ')
        print("-----", end=' ')
        print("--")
        for i in range(len(sorted_players_dict)):   # Loop for each player
            SNo += 1    # Adding value for each player
            sorted_players_dict[i][1][5] = SNo  # Appending last chart's order to each player
            print(format(sorted_players_dict[i][1][5], ">3d"), end=' ')
            print(format(sorted_players_dict[i][1][4], ">4d"), end=' ')
            print(format(sorted_players_dict[i][0], ">5d"), end=' ')
            print(format(sorted_players_dict[i][1][0], "12"), end=' ')
            print(format(sorted_players_dict[i][1][1], ">4d"), end=' ')
            print(format(sorted_players_dict[i][1][2], ">4d"), end=' ')
            print(format(sorted_players_dict[i][1][3], ">4"), end=' ')
            print(format(sorted_players_dict[i][1][8][0], ">5"), end=' ')
            print(format(sorted_players_dict[i][1][8][1], ">5"), end=' ')
            print(format(sorted_players_dict[i][1][8][2], ">5"), end=' ')
            print(format(sorted_players_dict[i][1][6], ">2d"))
        sorted_players_dict = sorted(players_dict.items(), key=lambda x: (x[1][4]))     # Sorting player dict in order to first sorted player dict
        print()
        print("Çapraz Tablo:")
        print("BSNo", end=' ')
        print("SNo", end=' ')
        print("LNo", end="   ")
        print("Ad-Soyad", end="     ")
        print("ELO", end='  ')
        print("UKD", end='  ')
        for turn_number in range(number_of_turn):   # Loop for each turn
            print(str(turn_number+1) + ". Tur", end='  ')
        print("Puan", end=' ')
        print("BH-1", end='  ')
        print("BH-2", end='  ')
        print("SB", end='    ')
        print("GS")
        print("----", end=' ')
        print("---", end=' ')
        print("-----", end=' ')
        print("------------", end=' ')
        print("----", end=' ')
        print("----", end=' ')
        for turn_number in range(number_of_turn):   # Loop for each turn
            print("-------", end=' ')
        print("----", end=' ')
        print("-----", end=' ')
        print("-----", end=' ')
        print("-----", end=' ')
        print("--")
        for i in range(len(sorted_players_dict)):   # Loop for each player
            print(format(sorted_players_dict[i][1][4], ">4d"), end=' ')
            print(format(sorted_players_dict[i][1][5], ">3d"), end=' ')
            print(format(sorted_players_dict[i][0], ">5d"), end=' ')
            print(format(sorted_players_dict[i][1][0], "12"), end=' ')
            print(format(sorted_players_dict[i][1][1], ">4d"), end=' ')
            print(format(sorted_players_dict[i][1][2], ">4d"), end=' ')
            for turn_number in range(number_of_turn):       # Loop for each turn
                print(format(sorted_players_dict[i][1][7][turn_number][0], ">3"), end=' ')
                print(format(sorted_players_dict[i][1][7][turn_number][1]), end=' ')
                print(format(sorted_players_dict[i][1][7][turn_number][2]), end=' ')
            print(format(sorted_players_dict[i][1][3], ">4"), end=' ')
            print(format(sorted_players_dict[i][1][8][0], ">5"), end=' ')
            print(format(sorted_players_dict[i][1][8][1], ">5"), end=' ')
            print(format(sorted_players_dict[i][1][8][2], ">5"), end=' ')
            print(format(sorted_players_dict[i][1][6], ">2d"))
    except ValueError:  # Creating output for error
        print("HATA!")


def main():     # Main function that contains other functions
    try:    # Checking for any errors
        players_dict = {}   # Creating dictionary
        gettingValues(players_dict)     # Calling function
        number_of_players = len(players_dict)   # Finding number of players
        min_turn = math.log(number_of_players, 2)   # Calculating minimum turn value
        min_turn = math.ceil(min_turn)  # Rounding the minimum turn number
        max_turn = number_of_players - 1    # Calculating maximum turn value
        startSortedChart(players_dict)   # Calling function
        number_of_turn = int(input("Turnuvadaki tur sayisini giriniz(" + str(min_turn) + "-" + str(max_turn) + ")"))     # Getting turn number
        while number_of_turn < min_turn or number_of_turn > max_turn:      # Checking turn number for if its in limits
            number_of_turn = int(input("Turnuvadaki tur sayisini giriniz(" + str(min_turn) + "-" + str(max_turn) + ")"))     # If not wants input again
        starting_color = input("Baslangic siralamasina gore ilk oyuncunun ilk turdaki rengini giriniz (b/s):")  # Getting starting color(for odd number)
        while starting_color not in ["b", "s"]:     # Checking turn color input
            starting_color = input("Baslangic siralamasina gore ilk oyuncunun ilk turdaki rengini giriniz (b/s):")  # If its wrong wants input again
        if starting_color in ["B", "b"]:    # Attending colors
            main_color = "b"
            side_color = "s"
        if starting_color in ["S", "s"]:    # Attending colors
            main_color = "s"
            side_color = "b"
        turnList(players_dict, number_of_turn, max_turn+1, main_color, side_color)  # Calling function
        endSortedChart(players_dict, number_of_turn)     # Calling function
    except:  # Creating output for error
        print("HATA!")

main()   # Calling main function

# Yazdığım kod türkçe alfabe ile uyumlu değildir. Sort mekanizmamı nasıl türkçe ile uyumlu yapabileceğimi çok araştırdım
# ama bulamadım.