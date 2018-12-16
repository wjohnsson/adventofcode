import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class AlchemicalReduction {

    public int partOne() {
        String workingDir = System.getProperty("user.dir");
        File file = new File(workingDir + "/2018/05/units.txt");

        int answer = -1;
        try (Scanner scanner = new Scanner(file)) {
            answer = removeReactions(scanner.nextLine()).length();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return answer;
    }

    private String removeReactions(String units) {
        StringBuilder sb = new StringBuilder(units);

        int i = 0;
        while (i < sb.length() - 1) {
            Character c1 = sb.charAt(i);
            Character c2 = sb.charAt(i + 1);

            if (willReact(c1, c2)) {
                sb.deleteCharAt(i);
                sb.deleteCharAt(i);

                // Move back since there might be a reaction on the
                // previous unit now.
                if (i == 0) {
                    i = -1; // special case.
                } else {
                    i -= 2;
                }
            }

            i++;
        }

        return sb.toString();
    }

    private boolean willReact(Character c1, Character c2) {
        boolean willReact = false;
        Character c1Upper = Character.toUpperCase(c1);
        Character c1Lower = Character.toLowerCase(c1);

        if (Character.isLowerCase(c1) && c1Upper.equals(c2)) {
            willReact = true;
        } else if (Character.isUpperCase(c1) && c1Lower.equals(c2)) {
            willReact = true;
        }

        return willReact;
    }
}