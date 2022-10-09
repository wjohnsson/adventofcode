using AdventOfCode.Y2021.D01;

class App
{
    public static void Main()
    {
        string year = "2021";
        string day = "01";
        string input = File.ReadAllText($"{year}/{day}/input");

        if (input.EndsWith('\n'))
            input = input[..^1];

        var solution = new SonarSweep();
        Console.WriteLine(solution.PartOne(input));
    }
}
