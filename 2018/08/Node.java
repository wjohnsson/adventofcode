import java.util.List;

public class Node {

    private List<Node> children;
    private List<Integer> metadata;

    public Node(List<Node> children, List<Integer> metadata) {
        this.children = children;
        this.metadata = metadata;
    }

    public List<Integer> getMetadata() {
        return metadata;
    }

    public List<Node> getChildren() {
        return children;
    }
}
