'''
    File: bball.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program will take an input file of a list of basketball
    teams with their name, conference, wins, and losses. The program
    prints out the converence(s) with the highest average win ratio in
    alphabeticall order with their win ratio. 
'''

# -----------------------------------------------------------------------------

# This class instantiates a team object that represents a basketball team. 
class Team:

    '''
    This __init__ function initializes the team object. It intializes the 
    following attributes:
        name of team and assigns to _name attribute. 
        conference of the team and assigns to _conf attribute.
        win ratio of team and assigns to _win_ratio attribute. 

    Parameters: A line read from a file that must be correctly formatted. 
        FORMAT: State (Conference) W L
        FORMAT: State (XX) (Conference) W L

    Returns: None.
    '''
    def __init__(self, line):
        # Count amount of parenthesis to handle teams that have state
        # abbreviation before conference. Ex) Albany (NY) (America East) 
        parenthesis_count = 0
        for char in line:
            if char == "(":
                parenthesis_count += 1

        # Each part of line is indexed accordingly to retrieve the team name,
        # conference, and win/loss ratio. It starts at the begining of the 
        # line and once each substring is retrieved, it is removed from the 
        # string to make finding the next substring easier.
        if parenthesis_count == 1:
            self._name = line[0:line.index("(")].strip()
            line = line[line.index("("):].strip()
        elif parenthesis_count == 2:
            self._name = line[0:line.index(")")+1].strip()
            line = line[line.index(")")+1:].strip()

        self._conf = line[1:line.index(")")].strip()
        line = line[line.index(")")+1:].strip()

        # Ratio = Wins / (Wins + Losses)
        line = line.split()
        self._win_ratio = float(line[0]) / (float(line[0]) + float(line[1]))
 
    '''
    This getter function retrieves the _name attribute of the Team class.
    
    Parameters: None.

    Returns: _name attribute of the class as a string.
    '''
    def name(self):
        return self._name
    
    '''
    This getter function retrieves the _conf attribute of the Team class.
    
    Parameters: None.

    Returns: _conf attribute of the class as a string.
    '''
    def conf(self):
        return self._conf
    
    '''
    This getter function retrieves the _win_ratio attribute of the Team class.
    
    Parameters: None.

    Returns: _win_ratio attribute of the class as a float.
    '''
    def win_ratio(self):
        return self._win_ratio
    
    '''
    This  function prints a string representation of the team object.
    
    Parameters: None.

    Returns: A string representation in the format: Team name : Win ratio. 
    '''
    def __str__(self): 
        return "{} : {}".format(self._name, str(self._win_ratio))

# This class instantiates a Conference object representing a collection 
# of teams. 
class Conference: 
    
    '''
    This __init__ function initializes the Conference object. It initalizes
    the following attributes: 
        Name of conferences assigned to _conf attribute. 
        An empty list of conferences assigned to _teams attribute. 
    
    Parameters: A string representing name of conference. 

    Returns: None.
    '''
    def __init__(self, conf): 
        self._conf = conf
        self._teams = []

    '''
    This function determins if a team is the _teams list attribute of a 
    Conference object.

    Parameters: String representing name on conference.

    Returns: True if team is in _teams, false otherwise. 
    '''
    def __contains__(self, team): 
        return team in self._teams
        
    '''
    This function adds a team object to the _teams attribute of the 
    Conference object. 

    Parmeters: A team object.

    Returns: None.
    '''
    def add(self, team):
        self._teams.append(team)

    '''
    This function calculates the average win ration of all the team 
    objects in a Conference object.

    Parameters: None. 

    Returns: Float representing average win ratio of all the teams. 
    '''
    def win_ratio_avg(self):
        num_teams = 0
        avg_total = 0

        for team in self._teams:
            avg_total += team.win_ratio()
            num_teams += 1
        return avg_total / num_teams
    
    def get_conference_name(self):
        return self._conf

    def __str__(self):
        return "{} : {}".format(self._conf, str(self.win_ratio_avg()))
    
# This class instantiates a ConferenceSet object representing
# a collection of Conference objects. 
class ConferenceSet:
    
    '''
    This function initalizes a ConferenceSet object with the 
    _conferences attribute, an empty list to hold Conference objects.

    Parameters: None.

    Returns: None.
    '''
    def __init__(self):
        self._conferences = []

    '''
    This function adds a team to it's respective Conference object in
    the ConferenceSet object.

    Parameters: A team object. 

    Returns: None.
    '''
    def add(self, team):
        found = False

        for conf in self._conferences:
            if conf.get_conference_name() == team.conf():
                conf.add(team)
                found = True
        if not found:
            new_conf = Conference(team.conf())
            new_conf.add(team)
            self._conferences.append(new_conf)

    '''
    This function returns a list of the Conference(s) objects with the highest
    average win ratio. 

    Parameters: None.

    Returns: List of Conference objects.
    '''
    def best(self):
        highest_list = []
        highest = 0

        for conference in self._conferences: 
            if conference.win_ratio_avg() > highest:
                highest = conference.win_ratio_avg()
        for conference in self._conferences:
            if conference.win_ratio_avg() == highest:
                highest_list.append(conference)
                
        return highest_list

    
def main():
    file = open(input(), "r")
    conferences = ConferenceSet()

    for line in file:
        if line[0] != "#":
            team = Team(line)
            conferences.add(team)

    
    best_names = []
    for conference in conferences.best():
        best_names.append(conference.get_conference_name())
        best_avg = conference.win_ratio_avg()
    for name in sorted(best_names):
        print(name + " : " + str(best_avg))

main()
