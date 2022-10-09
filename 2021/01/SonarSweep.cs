namespace AdventOfCode.Y2021.D01;

class SonarSweep : ISolver
{
    public object PartOne(string input)
    {
        IEnumerable<int> depths = input.Split('\n').Select(d => Int32.Parse(d));

        var increases = depths.Select((a, b) => a < b)
                              .Count(increased => increased);

        return increases;
    }
}