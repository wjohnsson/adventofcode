using adventofcode.Lib;
using System.CommandLine;

class App
{
    public static async Task<int> Main(string[] args)
    {
        var yearDayArgument = new Argument<string>("yearday")
        {
            Description = "Year and day in YYDD format (e.g., 2101 for year 2021, day 1)"
        };

        var inputArgument = new Argument<string>("input")
        {
            Description = "Path to the input file (optional, defaults to 'input')",
            DefaultValueFactory = _ => "input",
            Arity = ArgumentArity.ZeroOrOne
        };

        var rootCommand = new RootCommand("Advent of Code solution runner");
        rootCommand.Arguments.Add(yearDayArgument);
        rootCommand.Arguments.Add(inputArgument);

        rootCommand.SetAction(parseResult =>
        {
            string? yearDay = parseResult.GetValue(yearDayArgument);
            string? inputFilePath = parseResult.GetValue(inputArgument);

            if (yearDay == null || yearDay.Length != 4 || !int.TryParse(yearDay, out _))
            {
                Console.WriteLine("Error: yearday must be a 4-digit number in YYDD format");
                Console.WriteLine("Example: 2101 for year 2021, day 1");
                return 1;
            }

            string year = "20" + yearDay[..2];
            string day = yearDay[2..];

            string input = File.ReadAllText($"{year}/{day}/{inputFilePath}").TrimEnd();

            string targetNamespace = $"AdventOfCode.Y{year}.D{day}";

            // Find all types that implement ISolver in the target namespace
            Type? solutionType = AppDomain.CurrentDomain.GetAssemblies()
                .SelectMany(assembly => assembly.GetTypes())
                .FirstOrDefault(type =>
                    type.Namespace == targetNamespace &&
                    typeof(ISolver).IsAssignableFrom(type) &&
                    !type.IsInterface &&
                    !type.IsAbstract);

            if (solutionType == null)
            {
                Console.WriteLine($"Solution class not found for year {year}, day {day}");
                Console.WriteLine($"(Looking for a class implementing ISolver in namespace {targetNamespace})");
                return 1;
            }

            if (Activator.CreateInstance(solutionType) is not ISolver solution)
            {
                Console.WriteLine($"Failed to create instance of solution for year {year}, day {day}");
                return 1;
            }

            Console.WriteLine($"Solving Advent of Code {year}, Day {day}:");
            Console.WriteLine($"Part One: {solution.PartOne(input)}");
            Console.WriteLine($"Part Two: {solution.PartTwo(input)}");
            return 0;
        });

        return await rootCommand.Parse(args).InvokeAsync();
    }
}
