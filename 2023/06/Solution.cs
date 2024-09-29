using adventofcode.Lib;
using System.Text.RegularExpressions;

namespace AdventOfCode.Y2023.D06;

public class Solution : ISolver
{
    public object PartOne(string input)
    {
        string[] lines = input.Split('\n');
        var times = GetIntegers(lines.First());
        var distances = GetIntegers(lines.Last());

        var races = times.Zip(distances).Select(pair => new Race { Time = pair.First, Distance = pair.Second });
        return races.Aggregate(1, (acc, val) => acc * val.NumberOfWaysToWin());
    }

    public object PartTwo(string input)
    {
        string[] lines = input.Split('\n');
        long time = GetInteger(lines.First());
        var distance = GetInteger(lines.Last());

        var race = new Race { Time = time, Distance = distance };
        return race.NumberOfWaysToWin();
    }

    private static IEnumerable<int> GetIntegers(string line) => Regex.Matches(line, @"\d+").Select(match => int.Parse(match.Value));
    private static long GetInteger(string line) => long.Parse(Regex.Replace(line, @"\D", ""));

    class Race
    {
        public long Time { get; set; }
        public long Distance { get; set; }

        public int NumberOfWaysToWin()
        {
            // The problem can be modeled as a quadratic equation
            var lowerBound = (Time - Math.Sqrt(Math.Pow(Time, 2) - 4 * Distance)) / 2;
            var upperBound = (Time + Math.Sqrt(Math.Pow(Time, 2) - 4 * Distance)) / 2;
            int numberOfSolutions = (int)(Math.Floor(upperBound) - Math.Ceiling(lowerBound)) + 1;
            if (IsInteger(lowerBound))  // We need to beat the previous record, not match it
            {
                numberOfSolutions -= 2;
            }
            return numberOfSolutions;
        }

        private static bool IsInteger(double number) => number == Math.Truncate(number);
    }
}
