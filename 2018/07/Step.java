import java.util.ArrayList;
import java.util.List;

public class Step {

    private Character label;
    private List<Step> edges;
    public int prereqs;

    public Step(Character label) {
        this.label = label;
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

    @Override
    public String toString() {
        return label.toString();
    }
}
