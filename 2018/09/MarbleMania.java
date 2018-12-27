import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class MarbleMania {

    static Map<Integer, Integer> initElfScores(int elfCount) {
        Map<Integer, Integer> elfScores = new HashMap<>();
        for (int i = 0; i < elfCount; i++) {
            elfScores.put(i, 0);
        }
        return elfScores;
    }

    static Marble firstMarble() {
        Marble first = new Marble(0, null, null);
        first.next = first;
        first.prev = first;
        return first;
    }

    static int marbleGameHighScore(int players, int lastMarble) {
        Marble currentMarble = firstMarble();
        Map<Integer, Integer> elfScores = initElfScores(players);

        for (int m = 1; m <= lastMarble; m++) {
            int elf = m % players;
            if (m % 23 == 0) {
                // Remove the marble 7 steps counter-clockwise from the
                // currentMarble.
                for (int i = 0; i < 7; i++) {
                    currentMarble = currentMarble.prev;
                }
                currentMarble.prev.next = currentMarble.next;
                currentMarble.next.prev = currentMarble.prev;

                // Update score.
                int currentScore = elfScores.get(elf);
                int scored = currentMarble.value + m;
                elfScores.put(elf, currentScore + scored);

                currentMarble = currentMarble.next;
            } else {
                // Insert the new marble into the list.
                Marble nextMarble = new Marble(m, currentMarble.next.next, currentMarble.next);
                nextMarble.prev.next = nextMarble;
                nextMarble.next.prev = nextMarble;
                currentMarble = nextMarble;
            }

            elf++;
        }

        return Collections.max(elfScores.values());
    }

    public static void main(String[] args) {
        System.out.println("Answer part one: " + marbleGameHighScore(410, 72059));
    }
}