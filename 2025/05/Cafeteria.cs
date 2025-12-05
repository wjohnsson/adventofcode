using adventofcode.Lib;
using System.Text.RegularExpressions;

namespace AdventOfCode.Y2025.D05;

partial class Cafeteria : ISolver
{
    public object PartOne(string input)
    {
        var parts = input.Parts();
        var ranges = Ranges(parts[0]);
        var nums = parts[1].Lines().Select(long.Parse);

        return nums.Count(n => ranges.Any(r => r.Contains(n)));
    }
    public object? PartTwo(string input)
    {
        var parts = input.Parts();
        LinkedList<Range> joinedRanges = new();
        foreach (var r in Ranges(parts[0]))
        {
            Range.Add(joinedRanges, r);
        }
        return joinedRanges.Sum(r => r.Size);
    }

    static IEnumerable<Range> Ranges(string part) =>
        part.Lines().Select(line =>
        {
            var match = RangeDigitsRegex().Match(line);
            return new Range(
                long.Parse(match.Groups[1].Value),
                long.Parse(match.Groups[2].Value)
            );
        });


    record Range(long Start, long End)
    {
        public bool Contains(long value) => value >= Start && value <= End;

        // ±1 because we are working with integer ranges 
        public bool CanMerge(Range other) => Start <= other.End + 1 && End >= other.Start - 1;

        public static Range Merge(Range r1, Range r2) => 
            new(Math.Min(r1.Start, r2.Start), Math.Max(r1.End, r2.End));

        public long Size => End - Start + 1;

        /// <param name="ranges">A list of ascending, non-overlapping ranges</param>
        public static void Add(LinkedList<Range> ranges, Range newRange)
        {
            var current = ranges.First;
            while (current != null)
            {
                var currentRange = current.Value;
                if (newRange.End < currentRange.Start)
                {
                    // No need to look further, we found a spot somewhere along the chain
                    // where the new range belongs
                    break;
                }

                var next = current.Next;
                if (currentRange.CanMerge(newRange))
                {
                    newRange = Merge(currentRange, newRange);
                    ranges.Remove(current);
                }
                current = next;
            }

            if (current == null) ranges.AddLast(newRange);  // we reached the end or there was no range
            else ranges.AddBefore(current, newRange);
        }
    }

    [GeneratedRegex(@"(\d+)-(\d+)")]
    private static partial Regex RangeDigitsRegex();
}