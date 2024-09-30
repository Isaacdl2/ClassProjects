package com.gradescope.anagrams;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Anagrams {

	public static HashSet<String> getWordList(String wordList) throws FileNotFoundException {
		File wordsFile = new File(wordList); 
		Scanner wordReader = new Scanner(wordsFile);
		
		HashSet<String> result = new HashSet<String>(); 
		
		// Adds all words from file into result HashSet 
		while (wordReader.hasNextLine()) {
			result.add(wordReader.nextLine()) ;
		}
		
		wordReader.close(); 
		return result; 
	}
	
	public static ArrayList<Character> getChars(String word) {
		ArrayList<Character> result = new ArrayList<>();
	
		// Adds each character in word to the ArrayList
	    for (char c : word.toCharArray()) {
	        result.add(c);
	    }
	    return result;
	}
	
	public static void getCombinations(ArrayList<Character> allChars, String current, HashSet<String> validWords, HashSet<String> solutions) {
	    
		// Check if the current combination is a valid word
	    if (validWords.contains(current) && !current.isEmpty()) {
	        solutions.add(current);
	    }
	    
	    // Loop through the characters and get combinations
	    for (int i = 0; i < allChars.size(); i++) {
	
	        char currentChar = allChars.get(i);
	        ArrayList<Character> remainingChars = new ArrayList<>(allChars);
	        remainingChars.remove(i); 
	        getCombinations(remainingChars, current + currentChar, validWords, solutions);
	    }
	}
	
	public static void getAnagrams(int length, ArrayList<String> orderedSolution, String remaining, ArrayList<String> result, int maxAnas, int depth, ArrayList<ArrayList<String>> allResults) {
	    
		// Base case
	    if (remaining.isEmpty()) {
	        if (depth <= maxAnas || maxAnas == -1) {
	            allResults.add(new ArrayList<>(result)); 
	        }
	        return; 
	    }

	    // Loop through each word in orderedSolution
	    for (String word : orderedSolution) {
	    	
	        // Check if the word can be made from the remaining letters
	        if (canMakeWordWithRemainingLetters(word, remaining)) {
	            result.add(word);

	            // Updates remaining letters by removing the chosen word
	            String newRemaining = updateRemaining(remaining, word);

	            // Recurse with newRemaining
	            getAnagrams(length, orderedSolution, newRemaining, result, maxAnas, depth + 1, allResults);

	            // Backtracks by removing the last added word
	            result.remove(result.size() - 1);
	        }
	    }
	}
	
	public static boolean canMakeWordWithRemainingLetters(String word, String remaining) {
	    
	    // Convert remaining to a mutable list of characters
	    ArrayList<Character> remainingChars = new ArrayList<>();
	    for (char c : remaining.toCharArray()) {
	        remainingChars.add(c);
	    }

	    // Loop through each character in the input word
	    for (char currChar : word.toCharArray()) {
	    	
	        // Check if the character is in the remaining characters
	        if (!remainingChars.contains(currChar)) {
	            return false; 
	        }
	        
	        // Remove the character from the list
	        remainingChars.remove((Character) currChar);
	    }
	    
	    return true;
	}
	
	public static String updateRemaining(String remaining, String word) {
	    String result = remaining;

	    // Loops through every character in input word
	    for (char currChar : word.toCharArray()) {
	    	
	    	// Removes first instance of character
	        result = result.replaceFirst(Character.toString(currChar), "");
	    }

	    return result;
	}

	
	public static void main(String[] args) throws FileNotFoundException {
		
	    String wordList = args[0];
	    String word = args[1];
	    int maxAnas = Integer.valueOf(args[2]);
	    
	    // Set to -1 for no limit
	    if (maxAnas == 0) {
	    	maxAnas = -1; 
	    }
	
	    System.out.println("Phrase to scramble: " + word);
	    
	    HashSet<String> validWords = getWordList(wordList);
	    HashSet<String> solutions = new HashSet<String>();
	    ArrayList<Character> allChars = getChars(word);
	    
	    getCombinations(allChars, "", validWords, solutions);
	    ArrayList<String> orderedSolution = new ArrayList<String>(solutions);
	    Collections.sort(orderedSolution);
	    
	    System.out.println("\nAll words found in " + word + ":");
	    System.out.println(orderedSolution);
	    
	    ArrayList<String> result = new ArrayList<String>();
	    System.out.println("\nAnagrams for " + word + ":");
	    ArrayList<ArrayList<String>> allResults = new ArrayList<ArrayList<String>>();
	    getAnagrams(word.length(), orderedSolution, word, result, maxAnas, 0, allResults);
	    
	    for (int i = 0; i < allResults.size(); i++) {
	    	System.out.println(allResults.get(i));
	    }
	}
}