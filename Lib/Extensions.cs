using System.Numerics;

namespace adventofcode.Lib
{
    public static class Extensions
    {
        public static IEnumerable<T> Repeated<T>(this IEnumerable<T> sequence)
        {
            while (true)
                foreach (var item in sequence)
                    yield return item;
        }

        public static T GreatestCommonDivisor<T>(T a, T b) where T : INumber<T>
        {
            while (b != T.Zero)
            {
                var temp = b;
                b = a % b;
                a = temp;
            }

            return a;
        }

        public static T LeastCommonMultiple<T>(T a, T b) where T : INumber<T>
            => a / GreatestCommonDivisor(a, b) * b;

        public static T LeastCommonMultiple<T>(this IEnumerable<T> values) where T : INumber<T>
            => values.Aggregate(LeastCommonMultiple);
    }
}