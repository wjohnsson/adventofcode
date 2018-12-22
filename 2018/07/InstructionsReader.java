import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class InstructionsReader {

    private Map<Character, Step> steps;

    public InstructionsReader() {
        this.steps = new HashMap<>();
    }

    public void addInstruction(Character step, Character allows) {
        if (!steps.containsKey(step)) {
            steps.put(step, new Step(step));
        }
        if (!steps.containsKey(allows)) {
            steps.put(allows, new Step(allows));
        }

        steps.get(step).addEdge(steps.get(allows));
    }

    public List<Step> stepOrder() {
        Queue<Step> stepQueue = new PriorityQueue<>(new StepComparator());
        List<Step> stepList = new ArrayList<>();

        for (Step s : noPrereqs()) {
            stepQueue.add(s);
        }

        while (stepQueue.size() > 0) {
            Step s = stepQueue.poll();
            stepList.add(s);

            for (Step e : s.getEdges()) {
                e.prereqs--;

                if (e.prereqs == 0) {
                    stepQueue.add(e);
                }
            }
        }

        return stepList;
    }

    public List<Step> noPrereqs() {
        List<Step> noPrereqs = new ArrayList<>();

        for (Character key : steps.keySet()) {
            if (steps.get(key).prereqs == 0) {
                noPrereqs.add(steps.get(key));
            }
        }

        return noPrereqs;
    }

    public int timeToCompletion(int helperCount) {
        Queue<Step> stepQueue = new PriorityQueue<>(new StepComparator());
        int stepsDone = 0;
        int totalTime = 0;

        List<Worker> workers = new ArrayList<>();
        for (int i = 0; i < helperCount + 1; i++) {
            workers.add(new Worker());
        }

        for (Step s : noPrereqs()) {
            stepQueue.add(s);
        }

        while (stepsDone < steps.size()) {
            for (Worker w : workers) {
                // Check if there is work available.
                if (!w.isWorking() && !stepQueue.isEmpty()) {
                    w.assignWork(stepQueue.poll());
                }

                if (w.isWorking()) {
                    w.updateTime();
                }
            }

            // Check which workers completed a step this second.
            for (Worker w : workers) {
                if (w.jobsDone) {
                    stepsDone++;
                    for (Step s : w.getCurrentStep().getEdges()) {
                        s.prereqs--;

                        if (s.prereqs == 0) {
                            stepQueue.add(s);
                        }
                    }

                    w.jobsDone = false;
                }
            }

            totalTime++;
        }

        return totalTime;
    }

    public static InstructionsReader parseInput(String filename) {
        InstructionsReader ir = new InstructionsReader();
        String workingDir = System.getProperty("user.dir");

        try (Scanner reader = new Scanner(new File(workingDir + "/2018/07/"
                + filename))) {
            while (reader.hasNextLine()) {
                String[] input = reader.nextLine().split(" ");
                ir.addInstruction(input[1].charAt(0), input[7].charAt(0));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return ir;
    }

}