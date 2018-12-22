import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    private static void partOne() {
        InstructionsReader ar = new InstructionsReader();

        String workingDir = System.getProperty("user.dir");

        try (Scanner reader = new Scanner(new File(workingDir + "/2018/07/instructions.txt"))) {
            while (reader.hasNextLine()) {
                String[] input = reader.nextLine().split(" ");
                ar.addInstruction(input[1].charAt(0), input[7].charAt(0));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        for (Step s : ar.stepOrder()) {
            System.out.print(s);
        }
    }

    public static void main(String[] args) {
        partOne();
    }
}
