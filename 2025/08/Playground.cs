using System.Data;
using adventofcode.Lib;

namespace AdventOfCode.Y2025.D08;

partial class Laboratories : ISolver
{
    public object PartOne(string input)
    {
        const int numberOfBoxesToConnect = 1000;
        List<Point> points = GetPoints(input);
        List<Edge> edges = GetEdgesInCompleteGraph(points);

        var uf = new UnionFind(points);
        var shortestEdges = edges.OrderBy(e => e.Distance)
                                 .GetEnumerator();
        int edgesProcessed = 0;
        while (edgesProcessed < numberOfBoxesToConnect)
        {
            shortestEdges.MoveNext();
            var (a, b, _) = shortestEdges.Current;
            edgesProcessed++;

            // Add the edge if points are not already in the same connected component
            if (uf.Find(a) != uf.Find(b))
            {
                uf.Union(a, b);
            }
        }

        return uf.SizesOfComponents()
                 .OrderDescending()
                 .Take(3)
                 .Product();
    }

    public object? PartTwo(string input)
    {
        List<Point> points = GetPoints(input);
        List<Edge> edges = GetEdgesInCompleteGraph(points);

        var uf = new UnionFind(points);
        var shortestEdges = edges.OrderBy(e => e.Distance)
                                 .GetEnumerator();

        int edgeCount = 0;
        (Point, Point) lastPoints = (new Point(0, 0, 0), new Point(0, 0, 0));
        // Create a minimum spanning tree
        while (edgeCount < points.Count - 1)
        {
            shortestEdges.MoveNext();
            var (a, b, _) = shortestEdges.Current;

            // Add the edge if points are not already in the same connected component
            if (uf.Find(a) != uf.Find(b))
            {
                uf.Union(a, b);
                lastPoints = (points[a], points[b]);
                edgeCount++;
            }
        }

        return lastPoints.Item1.X * lastPoints.Item2.X;
    }

    private static List<Point> GetPoints(string input)
    {
        return [.. input.Lines().Select(line => {
            var cs = line.Split(',')
                         .Select(coordinate => int.Parse(coordinate))
                         .ToArray();
            return new Point(cs[0], cs[1], cs[2]);
        })];
    }

    private static List<Edge> GetEdgesInCompleteGraph(List<Point> points)
    {
        List<Edge> edges = [];
        for (int a = 0; a < points.Count; a++)
        {
            for (int b = a + 1; b < points.Count; b++)
            {
                // Use the position in the list as the ID of the nodes
                edges.Add(new Edge(a, b, points[a].DistanceTo(points[b])));
            }
        }
        return edges;
    }

    class UnionFind(IEnumerable<Point> points)
    {
        private readonly List<int> Parents = [.. Enumerable.Range(0, points.Count())];
        private readonly List<int> Sizes = [.. Enumerable.Repeat(1, points.Count())];

        public void Union(int a, int b)
        {
            // Find the roots of both components
            var rootA = Find(a);
            var rootB = Find(b);

            // If they're in different components, merge them
            if (rootA != rootB)
            {
                Sizes[rootB] += Sizes[rootA];
                Parents[rootA] = rootB;
            }
        }

        /// <summary>
        /// Which connected component does the node with the given ID belong to?
        /// </summary>
        /// <returns>The ID of the root node of the connected component</returns>
        public int Find(int a)
        {
            if (Parents[a] != a)
            {
                return Find(Parents[a]);
            }
            return a;
        }

        public IEnumerable<int> SizesOfComponents()
        {
            Dictionary<int, int> sizeOfRoots = [];
            for (int i = 0; i < Parents.Count; i++)
            {
                var root = Find(i);
                if (!sizeOfRoots.ContainsKey(root))
                {
                    sizeOfRoots[root] = Sizes[root];
                }
            }
            return sizeOfRoots.Select(kvp => kvp.Value);
        }
    }

    record Point(long X, long Y, long Z)
    {
        public double DistanceTo(Point other) => 
            Math.Sqrt(
                Math.Pow(X - other.X, 2) +
                Math.Pow(Y - other.Y, 2) +
                Math.Pow(Z - other.Z, 2)
            );
    };

    /// <param name="A">ID of node A</param>
    /// <param name="B">ID of node B</param>
    record Edge(int A, int B, double Distance);
}
