using adventofcode.Lib;

namespace AdventOfCode.Y2025.D07;

partial class Laboratories : ISolver
{
    public object PartOne(string input)
    {
        var lines = input.Lines();
        bool[] beams = new bool[lines[0].Length];

        beams[lines[0].IndexOf('S')] = true;
        int splitCounter = 0;
        foreach (var line in lines[1..])
        {
            for (int i = 0; i < beams.Length; i++)
            {
                bool split = line[i] == '^' && beams[i];
                if (split)
                {
                    beams[i - 1] = true;
                    beams[i] = false;
                    beams[i + 1] = true;
                    splitCounter++;
                }
            }
        }
        return splitCounter;
    }

    public object? PartTwo(string input)
    {
        var lines = input.Lines().ToList();
        int startBeamPos = lines[0].IndexOf('S');
        return PossibleTimelines(lines, startBeamPos, 1, []);
    }

    /// <summary>
    /// Solve with recursion and dynamic programming (memoization):
    ///   - beams overlap in different timelines
    ///   - cache the already known number of possible timelines for a given beam at a given time
    ///   - check the cache before traversing the same branch again
    /// </summary>
    static long PossibleTimelines(List<string> lines, int beamPos, int t, Dictionary<(int, int), long> cache)
    {
        if (t == lines.Count) return 1;  // end reached

        var key = (beamPos, t);
        if (cache.TryGetValue(key, out long cachedResult))
        {
            return cachedResult;
        }

        long result;
        bool split = lines[t][beamPos] == '^';
        if (split)
        {
            result = PossibleTimelines(lines, beamPos - 1, t + 1, cache) + PossibleTimelines(lines, beamPos + 1, t + 1, cache);
        }
        else
        {
            result = PossibleTimelines(lines, beamPos, t + 1, cache);
        }

        cache[key] = result;
        return result;
    }
}