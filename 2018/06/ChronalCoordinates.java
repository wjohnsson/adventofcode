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
        if (points.size() < 5) {
            return -1;
        }
        Point[][] closestPoints = closestPoints(points, boundingBox(points));
        return largestArea(removeEdgePoints(closestPoints));
    }

    private static Point[][] removeEdgePoints(Point[][] closestPoints) {
        Point[][] removed = new Point[closestPoints.length][closestPoints[0].length];

        Set<Point> edgePoints = new HashSet<>();

        // Check top and bottom row.
        for (int x = 0; x < closestPoints.length; x++) {
            edgePoints.add(closestPoints[x][0]);
            edgePoints.add(closestPoints[x][closestPoints[0].length - 1]);
        }

        // Check edge columns.
        for (int y = 0; y < closestPoints[0].length; y++) {
            edgePoints.add(closestPoints[0][y]);
            edgePoints.add(closestPoints[closestPoints.length - 1][y]);
        }

        // Remove edge points.
        for (int y = 0; y < closestPoints[0].length; y++) {
            for (int x = 0; x < closestPoints.length; x++) {
                if (edgePoints.contains(closestPoints[x][y])) {
                    removed[x][y] = null;
                } else {
                    removed[x][y] = closestPoints[x][y];
                }
            }
        }

        return removed;
    }

    private static int largestArea(Point[][] pointMatrix) {
        Map<Point, Integer> pointCount = new HashMap<>();
        for (int y = 0; y < pointMatrix[0].length; y++) {
            for (int x = 0; x < pointMatrix.length; x++) {
                Point p = pointMatrix[x][y];
                if (!pointCount.containsKey(p)) {
                    pointCount.put(p, 0);
                }
                int i = pointCount.get(p) + 1;
                pointCount.put(p, i);
            }
        }

        int largest = Integer.MIN_VALUE;
        for (Map.Entry e : pointCount.entrySet()) {
            int i = (int) e.getValue();
            if (e.getKey() != null && i > largest) {
                largest = i;
            }
        }

        return largest;
    }

    private static Point[][] closestPoints(List<Point> points, Rectangle bounds) {
        Point[][] closestPoints = new Point[bounds.width][bounds.height];

        for (int x = 0; x < bounds.width; x++) {
            for (int y = 0; y < bounds.height; y++) {
                Point dest = new Point(x + bounds.x, y + bounds.y);
                int shortestManhattanDist = Integer.MAX_VALUE;

                for (Point p : points) {
                    int md = manHattanDistance(p, dest);

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

        for (int y = 0; y < closestPoints[0].length; y++) {
            for (int x = 0; x < closestPoints.length; x++) {
                Point p = closestPoints[x][y];

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

    private static void printDistanceMatrix(int[][] totalDistanceMatrix) {
        for (int y = 0; y < totalDistanceMatrix[0].length; y++) {
            for (int x = 0; x < totalDistanceMatrix.length; x++) {
                System.out.print(totalDistanceMatrix[x][y] + " ");
            }
            System.out.println();
        }
    }

    public static int[][] totalDistanceMatrix(List<Point> points) {
        Rectangle bb = boundingBox(points);
        int[][] totalDistanceMatrix = new int[bb.height][bb.width];

        for (int y = 0; y < totalDistanceMatrix[0].length; y++) {
            for (int x = 0; x < totalDistanceMatrix.length; x++) {
                Point dest = new Point(x + bb.x, y + bb.y);
                int totalDistance = 0;

                for (Point p : points) {
                    totalDistance += manHattanDistance(p, dest);
                }

                totalDistanceMatrix[x][y] = totalDistance;
            }
        }

        printDistanceMatrix(totalDistanceMatrix);
        return totalDistanceMatrix;
    }

    public static int sizeOfRegionWithMaxTotalDistance(int[][] totalDistanceMatrix, int maxDistance) {
        // Use a Point matrix in order to reuse function from part one.
        Point[][] pointMatrix = new Point[totalDistanceMatrix.length][totalDistanceMatrix[0].length];

        Point p = new Point(0,0);
        for (int y = 0; y < pointMatrix[0].length; y++) {
            for (int x = 0; x < pointMatrix.length; x++) {
                if (totalDistanceMatrix[x][y] < maxDistance) {
                    pointMatrix[x][y] = p;
                }
            }
        }

        return largestArea(pointMatrix);
    }
}
