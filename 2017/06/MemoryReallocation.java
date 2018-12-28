package adventofcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// http://adventofcode.com/2017/day/6

public class MemoryReallocation {
	
	public static final String INPUT = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11";
	public static final String TEST = "0 2 7 0";
	public static int indexOfDuplicate = 0;
	
	public static void main(String[] args) {
		int answerPartOne = partOne(INPUT); 
		
		System.out.println("Part one: " + answerPartOne);
		System.out.print("Part two: " + (answerPartOne - indexOfDuplicate));
	}
	
	public static int partOne(String initialMemory) {
		int[] memBlocks = stringToIntArray(initialMemory.split("\t"));
		List<int[]> states = new ArrayList<int[]>();
		int cycles = 0;
		
		while (true) {
			memBlocks = memBlocks.clone();
			int i = indexOfGreatest(memBlocks);
			int[] itemsAt = distribute(memBlocks[i], memBlocks.length);

			// we take all blocks from the bank with the most amount
			memBlocks[i] = 0;
			// and then distribute them
			for (int offset = 0; offset < memBlocks.length; offset++) {
				// realIndex is achieves the cycling property of the memory using modulo
				int realIndex = (i + 1 + offset) % memBlocks.length;

				// distribute the blocks as evenly as possible
				memBlocks[realIndex] += itemsAt[offset];
			}
			
			if (containsArray(states, memBlocks)) {
				break;
			} else {
				states.add(memBlocks);
			}
			cycles++;
		}
		
		return cycles;
	}
	
	public static boolean containsArray(List<int[]> arrays, int[] nums) {
		for (int[] a : arrays) {
			if (Arrays.equals(a, nums)) {
				indexOfDuplicate = arrays.indexOf(a);
				return true;
			}
		}
		
		return false;
	}
	
	// distribute n items over k elements
	public static int[] distribute(int n, int k) {
		int[] itemsAt = new int[k];
		
		int j = n;
		int i = 0;
		while (j > 0) {
			itemsAt[i]++;
			j--;
			
			i++;
			if (i > k-1) {
				i = 0;
			}
		}
		
		return itemsAt;
	}
	
	public static int[] stringToIntArray (String[] nums) {
		int[] intArray = new int[nums.length];
		
		for (int i = 0; i < nums.length; i++) {
			intArray[i] = Integer.parseInt(nums[i]);
		}
		
		return intArray;
	}
	
	public static int indexOfGreatest(int[] values) {
		int indexOfGreatest = 0;
		
		for (int i = 0; i < values.length; i++) {
			if (values[indexOfGreatest] < values[i]) {
				indexOfGreatest = i;
			}
		}
		
		return indexOfGreatest;
	}
}
