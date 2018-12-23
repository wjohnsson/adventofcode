public class Main07 {

    private static void partOne(InstructionsReader ir) {
        for (Step s : ir.stepOrder()) {
            System.out.print(s);
        }
    }

    private static void partTwo(InstructionsReader ir) {
        System.out.print(ir.timeToCompletion(5));
    }

    public static void main(String[] args) {
        InstructionsReader ir = InstructionsReader.
                parseInput("instructions.txt");

        System.out.println("Answer part one: ");
        partOne(ir);

        // You shouldn't need to create a new instance of InstructionReader
        // after running part two...
        InstructionsReader ir2 = InstructionsReader.
                parseInput("instructions.txt");
        System.out.println("\nAnswer part two: ");
        partTwo(ir2);
    }
}
