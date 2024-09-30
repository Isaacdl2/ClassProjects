package com.gradescope.airportinfo;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List; 
import java.util.Scanner;

public class AirportInfo {
	
	public static HashMap<String, Integer> getAirportCount(String file_name) throws FileNotFoundException {
		File inpFile = new File(file_name); 
		Scanner inpReader = new Scanner(inpFile);
		HashMap<String, Integer> airportCount = new HashMap<String, Integer>();
		
		// Skips the header line 
		inpReader.nextLine(); 
		while (inpReader.hasNextLine()) {
			String[] parts = inpReader.nextLine().split(",");
			
			// Adds/ increments flight from source airport
			if (airportCount.containsKey(parts[2])) airportCount.put(parts[2], airportCount.get(parts[2]) + 1); 
			else airportCount.put(parts[2], 1);
		
			// Adds/ increments flight to destination airport
			if (airportCount.containsKey(parts[4])) airportCount.put(parts[4], airportCount.get(parts[4]) + 1); 
			else airportCount.put(parts[4], 1);
		}
		inpReader.close(); 
		return airportCount; 
	}

	public static HashMap<String, String> getDestinations(String file_name) throws FileNotFoundException { 
		File inpFile = new File(file_name); 
		Scanner inpReader = new Scanner(inpFile);
		HashMap<String, String> destinations = new HashMap<String, String>();
		
		// Skips the header line 
		inpReader.nextLine(); 
		while (inpReader.hasNextLine()) {
			String[] parts = inpReader.nextLine().split(",");
			
			// Adds another destination if source airport already exists
			if (destinations.containsKey(parts[2])) destinations.put(parts[2], destinations.get(parts[2]) + " " + parts[4]); 
			
			// Adds new source and destination airport 
			else destinations.put(parts[2], parts[4]);
			
		}
		
		inpReader.close(); 
		return destinations; 
	}
	
	public static String getMax(HashMap<String, Integer> airportCount)  {
		
		// Sorts through flightCount and collects all airports with the highest flight count
		int maxFlights = 0; 
		List<String> airportsWithMaxFlights = new ArrayList<>(); 
		
		for (String airport : airportCount.keySet()) {
			int flights = airportCount.get(airport); 
			
			if (flights > maxFlights) {
				maxFlights = flights; 
				airportsWithMaxFlights.clear(); 
				airportsWithMaxFlights.add(airport); 
			}
			else if (flights == maxFlights) airportsWithMaxFlights.add(airport); 
		}
		
		// Sorts the airportsWithMaxFlights array alphabetically
		Collections.sort(airportsWithMaxFlights);
		
		// Sets up string that will be returned 
		String result = "MAX FLIGHTS " + maxFlights + " : ";
		for (String airport : airportsWithMaxFlights) result += airport + " ";
		
		return result; 
	}
	
	public static String getDepartures(HashMap<String, String> destinations) {
		List<String> sortedKeys = new ArrayList<>(destinations.keySet()); 
		
		// Sorts the source airports alphabetically in an array
		Collections.sort(sortedKeys);
		
		// Sets up the return string
		String result = "";
		for (String airport : sortedKeys) {
			result += airport + " flies to " + destinations.get(airport) + "\n"; 
		}
		
		return result; 
	}
	
	public static String getLimits(int limit, HashMap<String, Integer> airportCount) {
		List<String> airportsAboveLimit = new ArrayList<>(); 
		
		// Loops through each key in airportCount parameter HashMap
		for (String airport : airportCount.keySet()) {
			int flights = airportCount.get(airport); 
			
			// Adds to new array of airports above the limit parameter
			if (flights > limit) { 
				airportsAboveLimit.add(airport); 
			}
		}
		
		// Sorts the airportsAboveLimit array alphabetically
		Collections.sort(airportsAboveLimit);
		
		// Sets up string that will be returned 
		String result = ""; 
		for (String airport : airportsAboveLimit) result += airport + " - " + airportCount.get(airport) + "\n";
		
		return result; 
	
	}
	
	public static void main(String[] args) throws FileNotFoundException {
		
		HashMap<String, String> destinations = getDestinations(args[0]);
        HashMap<String, Integer> airportCount = getAirportCount(args[0]);
        
		if (args[1].equals("MAX")) {
			System.out.println(getMax(airportCount));
        }
        
        if (args[1].equals("DEPARTURES")) {
            System.out.println(getDepartures(destinations));
        }
        
        if (args[1].equals("LIMIT")) {
            System.out.println(getLimits(Integer.valueOf(args[2]), airportCount));
        }
	}
}
