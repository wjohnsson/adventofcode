using adventofcode.Lib;

namespace AdventOfCode.Y2025.D03;

class Lobby : ISolver
{
    public object PartOne(string input)
    {
        return input.Lines()
                    .Sum(line => Joltage(2, line));  // refactored after solving part 2
    }

    public object? PartTwo(string input)
    {
        return input.Lines()
                    .Sum(line => Joltage(12, line));
    }

    /// <param name="n">The number of batteries to turn on</param>
    private static long Joltage(int n, string block)
    {
        int[] batteries = [.. block.Select(c => (int)char.GetNumericValue(c))];
        int[] on = new int[n];

        int left = 0;
        for (int i = 0; i < n; i++)
        {
            int right = block.Length - n + i;
            var (max, indexOfMax) = MaxBetween(left, right, batteries);
            left = indexOfMax + 1;
            on[i] = max;
        }
        return on.Select((val, i) => val * (long)Math.Pow(10, n - 1 - i)).Sum();
    }

    static (int max, int indexOfMax) MaxBetween(int left, int right, int[] batteries)
    {
        var slice = batteries.AsSpan()[left..(right + 1)];
        int max = int.MinValue;
        int indexOfMax = 0;

        for (int i = 0; i < slice.Length; i++)
        {
            if (slice[i] > max)
            {
                max = slice[i];
                indexOfMax = left + i;
            }
        }
        return (max, indexOfMax);
    }
}