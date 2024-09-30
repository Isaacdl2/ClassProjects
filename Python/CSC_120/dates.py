'''
    File: dates.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program takes an input file of events. Events that start
    with R are filtered out an of the file regardless of the format the date 
    it is and printed out with their respective dates.  
'''
# -----------------------------------------------------------------------------

class Date:
    '''
    This function initalized a Date type object. 

    Parameters: self, a string date, a list event

    Returns: None
    '''
    def __init__(self, date, event):
        self._date = date
        self._events = []


    '''
    This function adds an element to the event attribute of class Date.

    Parameters: self, event

    Returns: None
    '''
    # Function that adds an event to the list of events attribute.
    def add_event(self, event):
        self._events.append(event)

    '''
    This function prints a string representation of the Date object. 

    Parameters: self

    Returns: None
    '''
    # Prints the date attribute of the date object.
    def __str__(self):
        return self._date
    
    '''
    This function converts the date attribute of the Date class and converts 
    it in canonical form. 

    Parameters: self

    Returns: String representation of date in canonical form. 
    '''
    def canonical(self): 
        month_name_to_number = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
         "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, 
         "Oct": 10, "Nov": 11, "Dec": 12}

        if "/" in self._date:
            month_day_year = self._date.split("/")
            month = int(month_day_year[0])
            day = int(month_day_year[1])
            year = int(month_day_year[2])
        elif "-" in self._date:
            year_month_day = self._date.split("-")
            year = int(year_month_day[0])
            month = int(year_month_day[1]) 
            day = int(year_month_day[2])
        else:
            month_day_year = self._date.split()
            month = month_name_to_number[month_day_year[0]]
            day = int(month_day_year[1])
            year = int(month_day_year[2])
        return str(year) + "-" + str(month) + "-" + str(day)

class DateSet:
    '''
    This function initialized a DataSet type object with a dictionary 
    attribute.

    Parameters: self

    Returns: None
    '''
    def __init__(self):
        self._date_objects = {}

    '''
    This function adds a date, event value to the dictionary attribute
    of the class. 

    Parameters: self, a string date, a string event. 

    Returns: None
    '''
    def add_date(self, date, event):
        if date in self._date_objects:
            self._date_objects[date].add_event(event)
        else:
            # Creates a Date object and adds an event to the events list 
            # attribute and adds the string date and date object to dictionary.
            new_date = Date(date, event)
            new_date.add_event(event)
            self._date_objects[date] = new_date
    '''
    This function returns a string representation of the DataSet object by
    printing ou the keys and values. 

    Parameters: self

    Returns: String representation of the object. 
    '''
    def __str__(self):
        result = ""
        events = {}

        # Loops through each key, value pair in dictionary and converts
        # to correct format. 
        for date, date_obj in self._date_objects.items():
            canonical_string = date_obj.canonical()
            
            for event in date_obj._events:
                if canonical_string in events:
                    events[canonical_string].append(event)
                else:
                    events[canonical_string] = [event]
                
        for key, value in events.items():
            event_list = sorted(value)
            for event in event_list:
                result += key + ": " + event + "\n"
        return result
    
def main():
    # Initalized DataSet
    date_set = DateSet()
    dates_to_read = []
    file_name = input()

    # Finds all the dates that start with R and saves into list.
    date_file = open(file_name, "r")
    for line in date_file:
        line = line.strip()
        if line[0] == "R":
            dates_to_read.append(line[2:])
    date_file.close()

    # Loops through the dates that start with R
    for r_date in dates_to_read:
        # Creates date obj for each date.
        date_obj = Date(r_date, "")

        # Loops through each line in the file.
        date_file = open(file_name, "r")
        for line in date_file:
            # If line starts with I and date is in number format:
            if line[0] == "I":
                if line[2] in "0123456789":
                    line_parts = line.strip().split(" ", 2)
                    date = line_parts[1].strip(":")
                    event = line_parts[2].strip(" :")
                else:
                    # I line starts with I and date does not
                    # start with a number. (A letter)
                    line = line.strip()
                    line_parts = line.split(" ", 4)
                    date = line_parts[1] + " " + line_parts[2] 
                    date = date + " " + line_parts[3].strip(":")
                    event = line_parts[4].strip(": \t")
                    # Creates second date object to compare this date 
                    # with date in list of the R dates
                date_obj2 = Date(date, event)

                
                if date_obj2.canonical() == date_obj.canonical():
                    date_set.add_date(date, event)
            if line[0] != "R" and line[0] != "I":
                print("Error - Illegal operation.")
                
    print(date_set)

main()
