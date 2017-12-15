package adventofcode;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// http://adventofcode.com/2017/day/5

public class TwistyTrampolines {
	
	private static final String INPUTFILE_PATH = "D:\\Programmering\\eclipse workspace\\adventofcode\\src\\adventofcode\\input.txt"; 
	
	public static void main(String[] args) {
		File f = new File(INPUTFILE_PATH);
		
		System.out.println("Answer part one: " + partOne(f));
		System.out.println("Answer part two: " + partTwo(f));
	}
	
	/*
	 * Part one and part two are so similar on this day's
	 * challenge i could use the same method for both
	 */
	private static int partOne(File f) {
		return jumpTrampoline(f, '1');
	}
	
	private static int partTwo(File f) {
		return jumpTrampoline(f, '2');
	}
	
	private static int jumpTrampoline(File f, char part) {
		int steps = 0;
		boolean inMaze = true;
		List<Integer> offsets = initOffsets(f);
		
		int i = 0;
		int j = 0;
		while (inMaze) {
			j = i;
			
			try {
				i += offsets.get(i);
				
				// extra rule if part 2
				if (part == '2' && offsets.get(j) >= 3) {
					offsets.set(j, offsets.get(j) - 1);
				} else {
					offsets.set(j, offsets.get(j) + 1);
				}
				steps++;
			} catch (IndexOutOfBoundsException e) {
				inMaze = false;
			}
		}
		
		return steps;
	}
	
	private static List<Integer> initOffsets(File f) {
		List<Integer> offsets = new ArrayList<Integer>();
		Scanner reader = null;
		try {
			reader = new Scanner(f);
		} catch (FileNotFoundException e) {e.printStackTrace();}
		
		while (reader.hasNextLine()) {
			offsets.add(Integer.parseInt(reader.nextLine()));
		}
		
		reader.close();
		return offsets;
	}

}
