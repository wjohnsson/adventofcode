using adventofcode.Lib;

namespace AdventOfCode.Y2025.D04;

class PrintingDepartment : ISolver
{
    public object PartOne(string input)
    {
        char[][] grid = [.. input.Lines().Select(line => line.ToCharArray())];
        return TotalRollsRemoved(grid, oneIteration: true);
    }

    public object? PartTwo(string input)
    {
        char[][] grid = [.. input.Lines().Select(line => line.ToCharArray())];
        return TotalRollsRemoved(grid);
    }

    static long TotalRollsRemoved(char[][] grid, bool oneIteration = false)
    {
        int totalRollsRemoved = 0;
        bool rollsRemoved;
        do
        {
            rollsRemoved = false;
            for (int y = 0; y < grid.Length; y++)  // for each line
            {
                for (int x = 0; x < grid[y].Length; x++)   // for each point on line
                {
                    if (grid[y][x] != '@') continue;  // skip empty spots

                    byte adjacentRolls = AdjacentCount(grid, y, x);
                    bool removable = adjacentRolls < 4;
                    if (removable)
                    {
                        /*
                        * It's safe to remove rolls "too early" because the order we remove them in doesn't matter
                        * we will always reach the stable state eventually.
                        *
                        * Only when asking "how many rolls are there after x iterations?",
                        * like in part 1, does order matter.
                        */
                        if (!oneIteration) grid[y][x] = '.';
                        totalRollsRemoved++;
                        rollsRemoved = true;
                    }
                }
            }
        } while (rollsRemoved && !oneIteration);
        return totalRollsRemoved;
    }

    static byte AdjacentCount(char[][] grid, int y, int x)
    {
        byte adjacent = 0;
        // for each 8 adjacent points
        for (int i = -1; i <= 1; i++)
        {
            for (int j = -1; j <= 1; j++)
            {
                bool isMiddle = i == 0 && j == 0;  // skip the roll itself
                if (isMiddle || OutOfBounds(grid, y + i, x + j)) continue;
                if (grid[y + i][x + j] == '@') adjacent++;
            }
        }
        return adjacent;
    }

    static bool OutOfBounds(char[][] grid, int y, int x) =>
        y < 0 || y >= grid.Length ||
        x < 0 || x >= grid[y].Length;
}