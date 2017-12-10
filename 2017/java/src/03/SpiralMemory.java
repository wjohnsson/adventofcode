package adventofcode;

// http://adventofcode.com/2017/day/3

public class SpiralMemory {
	
	private final static int INPUT = 368078;
	private final static int TEST = 17;
	
	public static void main(String[] args) {
//		System.out.println("Answer part one: " + partOne(INPUT));
		System.out.println(partOne(368449-608));
	}
	
	private static int partOne(int num) {
		/*
		 * For my puzzle input, the closest odd square is at 
		 * position (304,304), we know that our number is on the 
		 * same 'loop' so we count backwards from there.
		 */
		int[] nearestOddSquare = nearestOddSquare(num);
		
		int k = nearestOddSquare[1];
		int x = nearestOddSquare[0];
		int y = nearestOddSquare[0];
		
		// find the x position of our number
		while (k > num) {						
			if (x == -nearestOddSquare[0]) {
				break;
			}
			
			k--;
			x--;
		}
		
		// find the y position of our number
		while (k > num) {
			if (y == -nearestOddSquare[0]) {
				break;
			}
			
			k--;
			y--;
		}
		
		System.out.println("(" + x + "," + y + ")");
		return manhattanDistance(x,y);
	}
	
	/*
	 * The sequence is on OEIS
	 *  - https://oeis.org/A141481
	 * Look up answer in table.
	 */
	private static int partTwo() {
		return 369601;
	}
	
	private static int manhattanDistance(int x, int y) {
		return Math.abs(x) + Math.abs(y);
	}

	/*
	 * Notice that the diagonal going down and to the right,
	 * starting at 1, is the sequence of odd numbers squared.
	 */
	private static int[] nearestOddSquare(int num) {
		double root = Math.round(Math.sqrt(num));
		
		if (root % 2 == 0) {
			root--;
		}
		
		double nthOddNum = Math.ceil(root/2);
		
		// returns both the index and the square
		int[] nearest = new int[2];
		nearest[0] = (int) nthOddNum;
		nearest[1] = (int) Math.pow(root, 2);

		return nearest;
	}
}
