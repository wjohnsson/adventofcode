import java.awt.Point;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String workingDir = System.getProperty("user.dir");
        List<Point> points = ChronalCoordinates.parseCoords(workingDir + "/2018/06/coords.txt");

        System.out.println("Answer part one: " + ChronalCoordinates.sizeOfLargestNonInfiniteArea(points));
        System.out.println("\nPart two test " + ChronalCoordinates.sizeOfRegionWithMaxTotalDistance(ChronalCoordinates.totalDistanceMatrix(points), 10000));
    }
}
