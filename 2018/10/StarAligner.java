import java.awt.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class StarAligner {

    static class MovingLight {

        private Point p;
        private int dx;
        private int dy;

        public MovingLight(Point p, int dx, int dy) {
            this.p = p;
            this.dx = dx;
            this.dy = dy;
        }

        public void move() {
            p.x += dx;
            p.y += dy;
        }

        @Override
        public String toString() {
            return p + ", dx: " + dx + ", dy: " + dy;
        }
    }

    static List<MovingLight> parseInput(String path) {
        List<MovingLight> mls = new ArrayList<>();

        try (Scanner reader = new Scanner(new File(path))) {
            while (reader.hasNextLine()) {
                Scanner lineReader = new Scanner(reader.nextLine().replaceAll("[^\\d -]", ""));
                while (lineReader.hasNextInt()) {
                    MovingLight ml = new MovingLight(
                            new Point(lineReader.nextInt(), lineReader.nextInt()),
                            lineReader.nextInt(),
                            lineReader.nextInt());
                    mls.add(ml);
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return  mls;
    }

    private static int manHattanDistance(MovingLight src, MovingLight dest) {
        int dx = Math.abs(dest.p.x - src.p.x);
        int dy = Math.abs(dest.p.y - src.p.y);

        return dx + dy;
    }

    public static Rectangle boundingBox(List<MovingLight> mls) {
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;

        for (MovingLight ml : mls) {
            if (ml.p.x < minX) {
                minX = ml.p.x;
            }

            if (ml.p.x > maxX) {
                maxX = ml.p.x;
            }

            if (ml.p.y < minY) {
                minY = ml.p.y;
            }

            if (ml.p.y > maxY) {
                maxY = ml.p.y;
            }
        }

        return new Rectangle(minX, minY, maxX - minX + 1, maxY - minY + 1);
    }

    private static boolean printLightsWhenClose(List<MovingLight> mls, int maxDistance) {
        // Check manhattan distance to all other points relative to this point.
        MovingLight relativeTo = mls.get(0);

        // Check if lights are close, if not, there's no need to print em.
        for (MovingLight ml : mls) {
            if (manHattanDistance(ml, relativeTo) > maxDistance) {
                return false;
            }
        }

        Rectangle bb = boundingBox(mls);

        // Print every point in bounding box.
        for (int y = 0; y < bb.height; y++) {
            for (int x = 0; x < bb.width; x++) {
                boolean alreadyPrinted = false;

                for (MovingLight ml : mls) {
                    Point dest = new Point(x + bb.x, y + bb.y);
                    if (dest.x == ml.p.x && dest.y == ml.p.y) {

                        // There may be mulitple lights in same point.
                        if (!alreadyPrinted) {
                            System.out.print("#");
                            alreadyPrinted = true;
                        }
                    }
                }

                if (!alreadyPrinted) {
                    System.out.print(".");
                }
            }
            System.out.println();
        }
        return true;
    }

    public static void main(String[] args) {
        List<MovingLight> mls = parseInput("/home/wilson/prog/adventofcode/2018/10/lights.txt");

        int time = 0;
        // Just interrupt when it's done printing.
        while (true) {
            for (MovingLight ml : mls) {
                ml.move();
            }

            time++;

            if (printLightsWhenClose(mls, 70)) {
                System.out.println("\ntime: " + time + "\n\n");
            }
        }
    }
}
