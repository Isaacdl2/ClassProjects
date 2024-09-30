'''
    File: pokemon.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program query's the user to enter a valid pokemon stat 
        type, and prints out the pokemon type(s) with the highest average 
        corresponding stat type. 
'''

# -----------------------------------------------------------------------------

'''
    This function takes a file in a specific format (see below) of pokemon 
        and their stats and maps the data in a 2d dictionary. 

    Parameters: A file of pokemon containing the specific format: 
        Format: #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,
        Speed, Generation,Legendary 

    Returns: A 2d dictionary. The top layer being each pokemon type, and
        the the second layer being every pokemon of that type with 
        all it's stats as the value. 
'''
def create_pokemon_database(pokemon_file):
    pokemon_data = open(pokemon_file, "r")
    next(pokemon_data)
    pokemon_data_2d = {}

    for line in pokemon_data: 
        temp_list = line.strip().split(",")
        pokemon_name = temp_list[1]
        pokemon_type = temp_list[2].lower() 
        pokemon_stats = temp_list[4:]
    
        if pokemon_type in pokemon_data_2d:
            pokemon_data_2d[pokemon_type][pokemon_name] = pokemon_stats
        else:
            # Creates new key, value on the first level of pokemon_data_2d.
            pokemon_data_2d[pokemon_type] = {pokemon_name : pokemon_stats}
 
    return pokemon_data_2d 

'''
This function computes the higest average inputted stat in the database. 

Parameters: A 2d dictionary: database of pokemon types and pokemon and a 
    string: stat to find the highest average of in the database. 

Returns: A string in the format: Type: Highest_average.
'''
def highest_average(database, stat): 
    stats = ["total", "hp", "attack", "defense", "specialattack",
              "specialdefense", "speed"] 
    # Finds index of stat the user inputted in user_query().
    index = int(stats.index(stat))
    highest_average_types = []
    highest_average = 0

    for type in database:
        total = 0 
        count = 0
        
        # Calculates average for the inputted stat of each type in database.
        for stats in database[type].values(): 
            total += int(stats[index])
            count += 1
        average = total / count

        if average > highest_average:
            highest_average = average
            highest_average_types = [type]
        elif average == highest_average:
            highest_average_types.append(type)

    for item in sorted(highest_average_types):
        # Capitaizes first letter and prints in format.
        print(item[0].upper() + item[1:] + ": " + str(highest_average))

'''
    This function query's the user to enter a pokemon stat and prints
        the pokemon 
        type with the highest average of the inputted stat. 
    
    Parameters: A 2d dictionary: database of pokemon. 

    Returns: None.
'''
def user_query(database): 
    query = True
    stats = ["total", "hp", "attack", "defense", "specialattack",
              "specialdefense", "speed"] 

    while (query == True): 
        query_input = input()
        query_input = query_input.lower()

        # If user dosn't type anything the query ends. 
        if (query_input == ""): 
            query = False 

        # Verifies that the input is a valid stat. (Not case sensitive). 
        elif (query_input in stats):
            highest_average(database, query_input)
            
        
def main():
    pokemon_file = input()
    user_query(create_pokemon_database(pokemon_file))   

main()
        


