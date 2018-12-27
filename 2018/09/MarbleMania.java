import java.util.HashMap;
import java.util.Map;

public class MarbleMania {

    static class Marble {

        public Long value;
        public Marble next;
        public Marble prev;

        public Marble(Long value, Marble next, Marble prev) {
            this.value = value;
            this.next = next;
            this.prev = prev;
        }

    }

    static Map<Integer, Long> initElfScores(int elfCount) {
        Map<Integer, Long> elfScores = new HashMap<>();
        for (int i = 0; i < elfCount; i++) {
            elfScores.put(i, 0L);
        }
        return elfScores;
    }

    static Marble firstMarble() {
        Marble first = new Marble(0L, null, null);
        first.next = first;
        first.prev = first;
        return first;
    }

    static Long marbleGameHighScore(int players, int lastMarble) {
        Marble currentMarble = firstMarble();
        Map<Integer, Long> elfScores = initElfScores(players);

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
                Long currentScore = elfScores.get(elf);
                Long scored = currentMarble.value + m;
                elfScores.put(elf, currentScore + scored);

                currentMarble = currentMarble.next;
            } else {
                // Insert the new marble into the list.
                Marble nextMarble = new Marble(new Long(m), currentMarble.next.next, currentMarble.next);
                nextMarble.prev.next = nextMarble;
                nextMarble.next.prev = nextMarble;
                currentMarble = nextMarble;
            }

            elf++;
        }

        Long maxScore = 0L;
        for (Long score : elfScores.values()) {
            if (score > maxScore) {
                maxScore = score;
            }
        }
        return maxScore;
    }

    public static void main(String[] args) {
        System.out.println("Answer part one: " + marbleGameHighScore(410, 72059));
        System.out.println("Answer part two: " + marbleGameHighScore(410, 72059 * 100));
    }
}