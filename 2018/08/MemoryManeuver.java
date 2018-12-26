import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class MemoryManeuver {

    static Queue<Integer> numQueue(String filename) {
        String workingDir = System.getProperty("user.dir");

        Queue<Integer> nums = new LinkedList<>();
        try (Scanner reader = new Scanner(new File(workingDir + "/2018/08/"
                + filename))) {
            while (reader.hasNextInt()) {
                nums.offer(reader.nextInt());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return nums;
    }

    static Node createTree(Queue<Integer> nums) {
        int childrenCount = nums.poll();
        int metadataCount = nums.poll();

        List<Node> children = new ArrayList<>();
        for (int i = 0; i < childrenCount; i++) {
            children.add(createTree(nums));
        }

        List<Integer> metadata = new ArrayList<>();
        for (int i = 0; i < metadataCount; i++) {
            metadata.add(nums.poll());
        }

        return new Node(children, metadata);
    }

    static int metadataSum(Node n) {
        int metadataSum = 0;

        metadataSum += n.getMetadata().stream().mapToInt(Integer::intValue).sum();
        for (Node c : n.getChildren()) {
            metadataSum += metadataSum(c);
        }

        return metadataSum;
    }

    public static void main(String[] args) {
        Queue<Integer> nums = numQueue("license.txt");

        Node root = createTree(nums);
        System.out.println("Answer part one: " + metadataSum(root));
        System.out.println("Answer part two: " + root.getValue());
    }
}
