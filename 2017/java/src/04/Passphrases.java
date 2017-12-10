package passphrases;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// http://adventofcode.com/2017/day/4

public class Passphrases {
	public static void main(String[] args) {
		File phrases = new File("D:\\Programmering\\eclipse workspace\\adventofcode\\src\\passphrases\\phrases.txt");
		
		try {
			System.out.println("Answer part one: " + partOne(phrases));
			System.out.println("Answer part two: " + partTwo(phrases));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
//		System.out.println(hasNoAnagrams("oiii ioii iioi iiio"));
	}
	
	private static int partOne(File f) throws FileNotFoundException {
		int validPhrases = 0;
		Scanner reader = new Scanner(f);

		while(reader.hasNextLine()) {
			if (wordsAppearOnce(reader.nextLine())) {
				validPhrases++;
			}
		}
		
		reader.close();
		return validPhrases;
	}
	
	private static int partTwo(File f) throws FileNotFoundException {
		int validPhrases = 0;
		Scanner reader = new Scanner(f);

		while(reader.hasNextLine()) {
			if (hasNoAnagrams(reader.nextLine())) {
				validPhrases++;
			}
		}
		
		reader.close();
		return validPhrases;
	}
	
	private static boolean hasNoAnagrams(String line) {
		List<String> previousWords = new ArrayList<String>();
		
		for (String word : line.split(" ")) {
			for (String w : previousWords) {
				if (isAnagram(word, w)) {
					return false;
				}
			}
			previousWords.add(word);
		}
		
		return true;
	}
	
	private static boolean isAnagram(String w1, String w2) {
		if (w1.length() != w2.length()) {
			return false;
		}
		
		List<Character> w1Chars = toCharList(w1.toCharArray());
		List<Character> w2Chars = toCharList(w2.toCharArray());
		
		
		for (char c : w1Chars) {
			if (w2Chars.contains(c)) {
				w2Chars.remove(w2Chars.indexOf(c));
			}
		}
		
		return w2Chars.isEmpty();
	}
	
	private static List<Character> toCharList(char[] chars) {
		List<Character> charList = new ArrayList<Character>();
		
		for (int i = 0; i < chars.length; i++) {
			charList.add(chars[i]);
		}
		
		return charList;
	}
	
	private static boolean wordsAppearOnce(String line) {
		List<String> previousWords = new ArrayList<String>();
		
		for (String word : line.split(" ")) {
			if (previousWords.contains(word)) {
				return false;
			}
			
			previousWords.add(word);
		}
		
		return true;
	}
	
}
