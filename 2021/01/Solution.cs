using adventofcode.Lib;

namespace AdventOfCode.Y2021.D01;

class Solution : ISolver
{
    public object PartOne(string input) => DepthIncreases(input, 1);

    public object PartTwo(string input) => DepthIncreases(input, 3);

    private static IEnumerable<int> Depths(string input)
    {
        return input.Split('\n').Select(d => int.Parse(d));
    }

    private static int DepthIncreases(string input, int skip)
    {
        var depths = Depths(input);
        var windowSums = depths.Zip(depths.Skip(skip));

        int count = 0;
        foreach (var (a, b) in windowSums)
        {
            if (a < b) count++;
        }

        return count;
    }
}