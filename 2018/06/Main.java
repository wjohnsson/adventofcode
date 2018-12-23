import java.awt.Point;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String workingDir = System.getProperty("user.dir");
        List<Point> points = ChronalCoordinates.parseCoords(workingDir + "/2018/06/test.txt");

        System.out.println("Size of bounding box: " + ChronalCoordinates.boundingBox(points));
        System.out.println(ChronalCoordinates.sizeOfLargestNonInfiniteArea(points));
    }
}
