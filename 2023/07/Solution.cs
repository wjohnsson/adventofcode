using adventofcode.Lib;

namespace AdventOfCode.Y2023.D07;

public class Solution : ISolver
{
    public object PartOne(string input)
    {
        var lines = input.Split("\n");
        var hands = lines.Select(line => 
        {
            var parts = line.Split(' ');
            return new Hand(parts[0], int.Parse(parts[1]));
        });
        return Ranked(hands).Sum(hand => hand.Winnings);
    }

    public object PartTwo(string input)
    {
        var lines = input.Split("\n");
        var hands = lines.Select(line =>
        {
            var parts = line.Split(' ');
            return new Hand(parts[0], int.Parse(parts[1])) { JokerRule = true };
        });
        return Ranked(hands).Sum(hand => hand.Winnings);
    }

    private static List<Hand> Ranked(IEnumerable<Hand> hands)
    {
        var sortedHands = hands.OrderBy(hand => hand).ToList();
        for (int i = 0; i < sortedHands.Count; i++)
        {
            Hand hand = sortedHands[i];
            hand.Rank = i + 1;
            hand.Winnings = hand.Rank * hand.Bid;
        }
        return sortedHands;
    }

    class Hand : IComparable<Hand>
    {
        public string Cards { get; set; }
        public int Bid { get; set; }
        public int Rank { get; set; }
        public bool JokerRule { get; set; }
        public int Winnings { get; set; }
        public HandType HandType
        {
            get
            {
                if (_handType.HasValue) return _handType.Value;
                _handType = Classify();
                return _handType.Value;
            }
        }

        private HandType? _handType;
        private readonly Dictionary<char, int> _cardCounts;

        public Hand(string cards, int bid)
        {
            Cards = cards;
            Bid = bid;
            _cardCounts = Cards.GroupBy(card => card).ToDictionary(group => group.Key, group => group.Count());
        }

        private HandType Classify()
        {
            if (JokerRule)
            {
                ImproveHandWithJokers();
            }

            if (IsFiveOfAKind()) return HandType.FIVE_OF_A_KIND;
            if (HasFourOfAKind()) return HandType.FOUR_OF_A_KIND;
            if (IsFullHouse()) return HandType.FULL_HOUSE;
            if (HasThreeOfAKind()) return HandType.THREE_OF_A_KIND;
            if (HasTwoPairs()) return HandType.TWO_PAIR;
            if (HasPair()) return HandType.ONE_PAIR;
            return HandType.HIGH_CARD;
        }

        private void ImproveHandWithJokers()
        {
            if (_cardCounts.TryGetValue('J', out int jokerCount))
            {
                _cardCounts.Remove('J');
                var nonJokers = _cardCounts.Where(card => card.Key != 'J');

                if (!nonJokers.Any())
                {
                    _cardCounts['A'] = 5;
                }

                var largestNonJokerCount = nonJokers.MaxBy(card => card.Value);
                _cardCounts[largestNonJokerCount.Key] += jokerCount;
            }
        }

        public bool IsFiveOfAKind() => _cardCounts.Count == 1;

        public bool HasFourOfAKind() => _cardCounts.Values.Any(count => count >= 4);

        public bool IsFullHouse() => _cardCounts.Values.Any(count => count == 3) && _cardCounts.Count == 2;

        public bool HasThreeOfAKind() => _cardCounts.Values.Any(count => count >= 3);

        public bool HasTwoPairs() => _cardCounts.Values.Count(count => count >= 2) >= 2;

        public bool HasPair() => _cardCounts.Values.Any(count => count >= 2);

        /// <returns>Weakest label first</returns>
        private List<char> LabelOrder()
        {
            if (JokerRule) return ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'];
            return ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'];
        }
        
        public int CompareTo(Hand? other)
        {
            if (other == null) return 1;
            if (HandType != other.HandType)
            {
                return HandType.CompareTo(other.HandType);
            }
            foreach (var (cardInThisHand, cardInOtherHand) in this.Cards.Zip(other.Cards))
            {
                if (cardInThisHand != cardInOtherHand)
                {
                    return LabelOrder().IndexOf(cardInThisHand).CompareTo(LabelOrder().IndexOf(cardInOtherHand));
                }
            }
            return 0;
        }

        public override string ToString() => $"{Cards} {_handType}";
    }

    enum HandType
    {
        FIVE_OF_A_KIND = 6,
        FOUR_OF_A_KIND = 5,
        FULL_HOUSE = 4,
        THREE_OF_A_KIND = 3,
        TWO_PAIR = 2,
        ONE_PAIR = 1,
        HIGH_CARD = 0
    }
}
