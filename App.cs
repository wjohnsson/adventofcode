using adventofcode.Lib;

class App
{
    public static void Main(string[] args)
    {
        const int maxArguments = 2;
        if (args.Length < 1 || args.Length > maxArguments || args[0].Length != 4)
        {
            Console.WriteLine("Usage: dotnet run YYDD");
            Console.WriteLine("Example: dotnet run 2101 for year 2021, day 1");
            return;
        }

        string yearDay = args[0];
        string year = "20" + yearDay[..2];
        string day = yearDay[2..];

        string inputFilePath = args.Length == 2 && args[1] == "test" ? "test" : "input";
        string input = File.ReadAllText($"{year}/{day}/{inputFilePath}");

        if (input.EndsWith('\n'))
            input = input[..^1];

        string className = $"AdventOfCode.Y{year}.D{day}.Solution";
        Type? solutionType = Type.GetType(className);

        if (solutionType == null)
        {
            Console.WriteLine($"Solution class not found for year {year}, day {day}");
            return;
        }

        if (Activator.CreateInstance(solutionType) is not ISolver solution)
        {
            Console.WriteLine($"Failed to create instance of solution for year {year}, day {day}");
            return;
        }

        Console.WriteLine($"Solving Advent of Code {year}, Day {day}:");
        Console.WriteLine($"Part One: {solution.PartOne(input)}");
        Console.WriteLine($"Part Two: {solution.PartTwo(input)}");
    }
}
