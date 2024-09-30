package com.gradescope.gradenator;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Gradenator {

	public static void main(String[] args) throws FileNotFoundException {
		// Gets filename from input
		Scanner inputScanner = new Scanner(System.in) ;
		System.out.println("File name?");
		
		// Opens file in a Scanner
		File myFile = new File(inputScanner.nextLine());
		inputScanner.close();
		Scanner myReader = new Scanner(myFile); 
		
		double gradeTotal = 0.0; 
		double percentTotal = 0.0; 
		// Loops through each line in file 
		while (myReader.hasNextLine()) {
			String line = myReader.nextLine(); 
			String[] parts = line.split(";");
			
			// Computes average of line
			double average = findAverage(parts[0].trim()); 
			
			// Converts percent to it's respective double. Example: 10% => 10.0
			double percent = Double.parseDouble(parts[2].trim().replace("%", ""));
			percentTotal += percent; 
			
			// Calculates and adds grade amount from each line
			gradeTotal += (percent / 100) * average; 

			// Outputs line
			System.out.print(parts[1].trim() + "; ");
			System.out.print(percent + "%; avg="); 
			System.out.format("%.1f\n", average);
		}
	
		myReader.close();
		
		// Outputs formatted grade total
		System.out.format("TOTAL = %.1f%% ", gradeTotal);
		System.out.print("out of " + percentTotal + "%"); 

	}
	
	public static double findAverage(String numbers) {
		// Splits numbers into array of strings
		String numArray[] = numbers.split(" "); 
		double sum = 0.0; 
		int count = 0; 
		
		// Iterates over array of numbers as strings, and converts to doubles
		for (String numStr : numArray) {
			double num = Double.parseDouble(numStr); 
			sum += num; 
			count++; 
		}
		
		// Avoids division by 0
		if (count == 0) {
			return 0; 
		}
		
		// Returns average
		return sum / count; 
	}
}
