using adventofcode.Lib;
using System.Text.RegularExpressions;

namespace AdventOfCode.Y2023.D08;

public class Solution : ISolver
{
    public object PartOne(string input)
    {
        Graph graph = ConstructGraph(input);

        Visitor visitor = new(graph.GetNode("AAA"));
        TraverseUntilEnd(graph, [visitor]);

        return visitor.StepsToEnd ?? 0;
    }

    public object PartTwo(string input)
    {
        Graph graph = ConstructGraph(input);

        List<Visitor> visitors = graph.Nodes.Values.Where(node => node.IsStart).Select(node => new Visitor(node)).ToList();
        TraverseUntilEnd(graph, visitors);

        return visitors.Select(visitor => visitor.StepsToEnd ?? 1).LeastCommonMultiple();
    }

    private static void TraverseUntilEnd(Graph graph, List<Visitor> visitors)
    {
        int steps = 1;
        while (visitors.Any(visitor => !visitor.StepsToEnd.HasValue))
        {
            graph.Instructions.MoveNext();
            char instruction = graph.Instructions.Current;
            foreach (var visitor in visitors.Where(v => !v.StepsToEnd.HasValue))
            {
                Node nextNode = instruction == 'L' ? visitor.Node.Left : visitor.Node.Right;
                visitor.Node = nextNode;
                if (visitor.Node.IsEnd)
                {
                    visitor.StepsToEnd = steps;
                }
            }
            steps++;
        }
    }

    private static Graph ConstructGraph(string input)
    {
        var lines = input.Split("\n").Where(line => line.Trim().Length != 0).ToList();
        Graph graph = new()
        {
            Instructions = lines.First().Trim().Repeated().GetEnumerator()
        };
        foreach (var line in lines[1..])
        {
            var matches = Regex.Matches(line, @"\w+").Select(match => match.Value).ToArray();
            graph.AddNode(matches[0], matches[1], matches[2]);
        }
        return graph;
    }

    class Graph
    {
        public Dictionary<string, Node> Nodes { get; set; }
        public required IEnumerator<char> Instructions { get; set; }
        public Graph() => Nodes = [];

        public Node GetNode(string label)
        {
            if (Nodes.TryGetValue(label, out Node? node))
            {
                return node;
            }

            var newNode = new Node(label);
            Nodes.Add(label, newNode);
            return newNode;
        }

        public void AddNode(string label, string leftLabel, string rightLabel)
        {
            Node node = GetNode(label);
            Node leftNode = GetNode(leftLabel);
            Node rightNode = GetNode(rightLabel);

            node.Left = leftNode;
            node.Right = rightNode;
        }
    }

    class Node
    {
        public string Label { get; set; }
        public Node Left { get; set; }
        public Node Right { get; set; }
        public bool IsEnd { get; }
        public bool IsStart { get; }

        public Node(string label)
        {
            Label = label;
            Left = this;
            Right = this;

            IsStart = Label.EndsWith('A');
            IsEnd = Label.EndsWith('Z');
        }

        public override string ToString() => $"Label={Label}, L={Left.Label}, R={Right.Label}";
    }

    class Visitor
    {
        public Node Node { get; set; }
        public Node StartNode { get; set; }
        public long? StepsToEnd { get; set; }
        
        public Visitor(Node node)
        {
            Node = StartNode = node;
        }
    }
}
