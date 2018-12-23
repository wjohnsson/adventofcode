import java.awt.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.List;

public class ChronalCoordinates {
    public static List<Point> parseCoords(String path) {
        List<Point> points =  new ArrayList<>();

        try (Scanner reader = new Scanner(new File(path))) {
            while (reader.hasNextLine()) {
                String[] coords = reader.nextLine().trim().split(", ");
                int x = Integer.parseInt(coords[0]);
                int y = Integer.parseInt(coords[1]);

                points.add(new Point(x, y));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return points;
    }

    public static int sizeOfLargestNonInfiniteArea(List<Point> points) {
        if (points.size() <= 5) {
            return -1;
        }

        Point[][] closestPoints = closestPoints(points, boundingBox(points));
        printPointMatrix(points, closestPoints);

        return 0;
    }

    private static Point[][] closestPoints(List<Point> points, Rectangle bounds) {
        Point[][] closestPoints = new Point[bounds.width][bounds.height];

        for (int x = 0; x < bounds.width; x++) {
            for (int y = 0; y < bounds.height; y++) {
                Point dest = new Point(x + bounds.x, y + bounds.y);
                int shortestManhattanDist = Integer.MAX_VALUE;

                for (Point p : points) {
                    Point src = new Point(p.x + bounds.x, p.y + bounds.y);
                    int md = manHattanDistance(src, dest);

                    if (md == shortestManhattanDist) {
                        closestPoints[x][y] = null;
                    }

                    if (md < shortestManhattanDist) {
                        shortestManhattanDist = md;
                        closestPoints[x][y] = p;
                    }
                }
            }
        }

        return closestPoints;
    }

    private static int manHattanDistance(Point src, Point dest) {
        int dx = Math.abs(dest.x - src.x);
        int dy = Math.abs(dest.y - src.y);

        return dx + dy;
    }

    public static Rectangle boundingBox(List<Point> points) {
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;

        for (Point p : points) {
            if (p.x < minX) {
                minX = p.x;
            }

            if (p.x > maxX) {
                maxX = p.x;
            }

            if (p.y < minY) {
                minY = p.y;
            }

            if (p.y > maxY) {
                maxY = p.y;
            }
        }

        return new Rectangle(minX, minY, maxX - minX + 1, maxY - minY + 1);
    }

    private static void printPointMatrix(List<Point> points, Point[][] closestPoints) {
        Map<Point, Character> pointCharacterMap = new HashMap<>();

        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toLowerCase();
        for (int i = 0; i < points.size(); i++) {
            pointCharacterMap.put(points.get(i), alphabet.charAt(i));
        }

        System.out.println("Length of pointCharacterMap: " + pointCharacterMap.size());
        for (int row = 0; row < closestPoints.length; row++) {
            for (int col = 0; col < closestPoints[row].length; col++) {
                Point p = closestPoints[row][col];

                char c = '.';
                if (p != null) {
                    c = pointCharacterMap.get(p);
                }

                System.out.print(c);
            }
            System.out.println();
        }
        System.out.println();
    }
}
