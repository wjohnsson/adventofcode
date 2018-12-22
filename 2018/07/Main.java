public class Main {

    private static void partOne(InstructionsReader ir) {
        for (Step s : ir.stepOrder()) {
            System.out.print(s);
        }
    }

    private static void partTwo(InstructionsReader ir) {
        System.out.print(ir.timeToCompletion(1));
    }

    public static void main(String[] args) {
        InstructionsReader ir = InstructionsReader.
                parseInput("test.txt");

        System.out.println("Answer part one: ");
        partOne(ir);

        InstructionsReader ir2 = InstructionsReader.
                parseInput("instructions.txt");
        System.out.println("\nAnswer part two: ");
        partTwo(ir2);
    }
}
