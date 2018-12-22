import java.util.*;

public class InstructionsReader {

    // Step Q must be finished before step O can begin.
    // Step Z must be finished before step G can begin.
    // Step W must be finished before step V can begin.
    // Step C must be finished before step X can begin.
    // Step O must be finished before step E can begin.
    // Step K must be finished before step N can begin.
    // Step P must be finished before step I can begin.

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

}