using System.Text;
using adventofcode.Lib;

namespace AdventOfCode.Y2025.D09;

partial class MovieTheater : ISolver
{
    public object PartOne(string input)
    {
        var points = GetPoints(input);
        
        long maxArea = 0;
        for (int i = 0; i < points.Count; i++)
        {
            for (int j = i + 1; j < points.Count; j++)
            {
                Rect r = new() { Corner1 = points[i], Corner2 = points[j] };
                long area = r.Area;
                if (area > maxArea) maxArea = area;
            }
        }
        return maxArea;
    }

    public object? PartTwo(string input)
    {
        var points = GetPoints(input);
        int minX = points.Min(p => p.X), maxX = points.Max(p => p.X);
        int minY = points.Min(p => p.Y), maxY = points.Max(p => p.Y);
        int midX = minX + (maxX - minX) / 2;

        // From looking at the polygon formed by the points we see that the input forms two semi circles
        // with a rectangular "slice" in the middle. The points that form the
        // inside corner of this slice are very likely to be part of the biggest rectangle.

        // Eyballing the input we find the points with big jumps in X.
        // 1932,50278
        // 94664,50278 !
        // 94664,48472 !
        // 1636,48472

        var topSlicePoint = (X: 94664, Y: 48472);
        var bottomSlicePoint = (X: 94664, Y: 50278);

        var secondQuadrantAboveSlice = points.Where(p => p.X <= midX && p.Y <= topSlicePoint.Y);
        var top = FindLargestRect(
            points,
            secondQuadrantAboveSlice,
            topSlicePoint);

        var thirdQuadrantBelowSlice = points.Where(p => p.X <= midX && p.Y >= bottomSlicePoint.Y);
        var bottom = FindLargestRect(
            points,
            thirdQuadrantBelowSlice,
            bottomSlicePoint);

        SavePolygonAsSvg(points, top, "-top");
        SavePolygonAsSvg(points, bottom, "-bottom");
        var bestRect = new [] { top, bottom }.MaxBy(r => r.Area);
        SavePolygonAsSvg(points, bestRect, "-best");
        return bestRect!.Area;
    }

    private static Rect FindLargestRect(IReadOnlyList<(int X, int Y)> allPoints, IEnumerable<(int X, int Y)> candidates, (int X, int Y) slicePoint)
    {
        Rect best = new();
        foreach (var p in candidates)
        {
            var r = new Rect { Corner1 = p, Corner2 = slicePoint };

            // if any points are inside the rect (except on the edge) the rect is invalid.
            // Assumes each subsequent point change both in x and y (only the "slice" points violate this rule)
            if (allPoints.Any(r.Contains)) continue;

            if (best is null || r.Area > best.Area)
                best = r;
        }
        return best;
    }

    private static List<(int X, int Y)> GetPoints(string input) => input.Split('\n')
                                                                        .Where(l => !string.IsNullOrWhiteSpace(l))
                                                                        .Select(l => l.Split(','))
                                                                        .Select(points => (X: int.Parse(points[0]), Y: int.Parse(points[1])))
                                                                        .ToList();

    private record Rect
    {
        public (int X, int Y) Corner1;
        public (int X, int Y) Corner2;
        public int Width => Math.Abs(Corner1.X - Corner2.X);
        public int Height => Math.Abs(Corner1.Y - Corner2.Y);
        public int MinX => Math.Min(Corner1.X, Corner2.X);
        public int MinY => Math.Min(Corner1.Y, Corner2.Y);
        public int MaxX => Math.Max(Corner1.X, Corner2.X);
        public int MaxY => Math.Max(Corner1.Y, Corner2.Y);
        public long Area => ((long)Width + 1) * ((long)Height + 1);
        public bool Contains((int x, int y) p) => p.x > MinX && p.x < MaxX && p.y > MinY && p.y < MaxY;
    }

    private static void SavePolygonAsSvg(List<(int X, int Y)> points, Rect? rect = null, string suffix = "")
    {
        long minX = points.Min(points => points.X), maxX = points.Max(points => points.Y);
        long minY = points.Min(points => points.Y), maxY = points.Max(points => points.Y);

        long pad = 500;

        var sb = new StringBuilder();
        sb.AppendLine($"<svg xmlns='http://www.w3.org/2000/svg' " +
                      $"viewBox='{minX - pad} {minY - pad} {maxX - minX + 2 * pad} {maxY - minY + 2 * pad}' " +
                      $"width='1200'>");
        sb.AppendLine(@"
<defs>
  <marker
    id='dot'
    viewBox='0 0 10 10'
    refX='5'
    refY='5'
    markerWidth='5'
    markerHeight='5'>
    <circle cx='5' cy='5' r='5' fill='red' />
  </marker>
</defs>
");

        var pts = string.Join(" ", points.Select(p => $"{p.X},{p.Y}"));
        sb.AppendLine($"<polygon points='{pts}' fill='lightblue' />");  // just the fill
        if (rect != null)
        {
            sb.AppendLine($"<rect x='{rect.MinX}' y='{rect.MinY}' width='{rect.Width}' height='{rect.Height}' fill='cadetblue' />");
        }
        sb.AppendLine($"<polygon points='{pts}' fill='none' stroke='green' stroke-width='70' marker-start='url(#dot)' marker-mid='url(#dot)' marker-end='url(#dot)' />");

        sb.AppendLine("</svg>");
        string path = $"movietheater-grid{suffix}.svg";
        string dir = $"AdventOfCodeY2025D09-{DateTime.Now:yyyy-MM-dd}";
        if (!Directory.Exists(dir)) Directory.CreateDirectory(dir);
        File.WriteAllText(Path.Join(dir, path), sb.ToString());
    }
}