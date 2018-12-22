import java.util.ArrayList;
import java.util.List;

public class Step {

    private Character label;
    private int time;
    private List<Step> edges;
    public int prereqs;

    public Step(Character label) {
        this.label = label;

        // Time to complete step is position in alphabet + 60 seconds.
        this.time = (int) ((char) label) - 64 + 0;

        this.edges = new ArrayList<>();
        this.prereqs = 0;
    }

    public void addEdge(Step s) {
        edges.add(s);
        s.prereqs++;
    }

    public List<Step> getEdges() {
        return edges;
    }

    public int getTime() {
        return time;
    }

    @Override
    public String toString() {
        return label.toString();
    }
}
