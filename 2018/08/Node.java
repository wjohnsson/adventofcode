import java.util.List;

public class Node {

    private List<Node> children;
    private List<Integer> metadata;
    private int value;

    public Node(List<Node> children, List<Integer> metadata) {
        this.children = children;
        this.metadata = metadata;

        value = 0;
        if (children.isEmpty()) {
            value += metadata.stream().mapToInt(Integer::intValue).sum();
        } else {
            for (int m : metadata) {
                try {
                    value += children.get(m - 1).getValue();
                } catch (IndexOutOfBoundsException e) {}
            }
        }
    }

    public List<Integer> getMetadata() {
        return metadata;
    }

    public List<Node> getChildren() {
        return children;
    }

    public int getValue() {
        return value;
    }
}
