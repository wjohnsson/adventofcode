import java.util.*;

public class MarbleMania {

    static Map<Integer, Integer> elfScores(int elfCount) {
        Map<Integer, Integer> elfScores = new HashMap<>();

        for (int i = 0; i < elfCount; i++) {
            elfScores.put(i, 0);
        }

        return elfScores;
    }

    static int marbleGameHighScore(int players, int lastMarble) {
        List<Integer> marbles = new ArrayList<>();
        Map<Integer, Integer> elfScores = elfScores(players);

        int indexOfCurrent = 0;
        marbles.add(0);
        for (int i = 1; i <= lastMarble; i++) {
            int elf = i % players;

            if (i % 23 == 0) {
                int k = indexOfCurrent - 7;
               int currentScore = elfScores.get(elf);

                if (k < 0) {
                    indexOfCurrent = marbles.size() + k;
                    elfScores.put(elf, currentScore + marbles.remove(marbles.size() + k) + i);
                } else {
                    indexOfCurrent = k;
                    elfScores.put(elf, currentScore + marbles.remove(k) + i);
                }
            }
            indexOfCurrent = ((indexOfCurrent + 1) % marbles.size()) + 1;
            marbles.add(indexOfCurrent, i);


            elf++;
        }

        return Collections.max(elfScores.values());
    }

    public static void main(String[] args) {
        System.out.println(marbleGameHighScore(9, 25));
        System.out.println(marbleGameHighScore(10, 1618));
        System.out.println(marbleGameHighScore(13, 7999));
        System.out.println(marbleGameHighScore(17, 1104));
        System.out.println(marbleGameHighScore(21, 6111));
        System.out.println(marbleGameHighScore(30, 5807));
    }
}