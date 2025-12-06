using System.Data;
using System.Text.RegularExpressions;
using adventofcode.Lib;

namespace AdventOfCode.Y2025.D06;

partial class TrashCompactor : ISolver
{
    public object PartOne(string input)
    {
        var lines = input.Lines().ToList();

        var numberRegex = NumberRegex();
        var numberLines = lines[..^1];
        var grid = numberLines
            .Select(line => numberRegex.Matches(line)
                .Select(m => long.Parse(m.Value))
                .ToList())
            .ToList();

        var operators = GetOperators(lines[^1]);

        var problems = operators.Index()
            .Select(op => new Problem(
                grid.Select(row => row[op.Index]),  // get the numbers in the same column as this operator
                op.Item
            ));

        return problems.Sum(p => p.Evaluate());
    }

    public object? PartTwo(string input)
    {
        var lines = input.Lines().ToList();

        var blocks = GetBlocks(lines[..^1]);
        var operators = GetOperators(lines[^1]);

        var problems = operators
            .Index()
            .Select(op => new Problem(blocks[op.Index], op.Item));

        return problems.Sum(p => p.Evaluate());
    }

    private static IEnumerable<Func<long, long, long>> GetOperators(string line) =>
        OperatorRegex().Matches(line)
                       .Select(m => m.Value[0])
                       .Select(Problem.CharToOperator);


    /// <returns>"blocks" - lists of numbers that should be processed by the same operator</returns>
    private static List<List<long>> GetBlocks(List<string> numberLines)
    {
        List<List<long>> blocks = [];
        List<long> block = [];
        for (int col = 0; col < numberLines[0].Length; col++)
        {
            List<char> digits = [];
            foreach (var line in numberLines)
            {
                char c = line[col];
                if (char.IsNumber(c)) digits.Add(c);
            }

            bool startNextBlock = digits.Count == 0;
            if (startNextBlock)
            {
                blocks.Add(block);
                block = [];
            }
            else
            {
                long value = long.Parse(string.Join("", digits));
                block.Add(value);
            }
        }
        blocks.Add(block);
        return blocks;
    }

    record Problem(IEnumerable<long> Nums, Func<long, long, long> Operator)
    {
        public long Evaluate() => Nums.Aggregate(Operator);

        public static Func<long, long, long> CharToOperator(char c) => c switch
        {
            '+' => (a, b) => a + b,
            '*' => (a, b) => a * b,
            _ => throw new ArgumentException($"Unknown operator: {c}")
        };
    }

    [GeneratedRegex(@"\d+")]
    private static partial Regex NumberRegex();

    [GeneratedRegex(@"\+|\*")]
    private static partial Regex OperatorRegex();
}