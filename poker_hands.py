# -*- coding: utf-8 -*-
import collections
import random
import re
import sys


class POKERHANDS:
    SUIT = ['S', 'H', 'D', 'C']
    RANK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    HANDS = ['4C', 'FH', '3C', '2P', '1P']
    ONEPAIR = 2
    THREECARDS = 3
    FOURCARDS = 4
    DATA = {
        'rank': []
    }

    def generate_card(self):
        card = ''
        for idx in range(5):
            card += random.choice(self.SUIT) + random.choice(self.RANK)
        return card

    def calculate_rank(self, ranks):
        self.DATA['rank'] = []
        for item, count in collections.Counter(ranks).items():
            if count > 1:
                self.DATA['rank'].append(count)

    def calculate_hand(self, data):
        rank = data['rank']
        length = len(data['rank'])

        if length == 1 and rank[0] == self.FOURCARDS:
            return self.HANDS[0]
        elif length == 2 and self.ONEPAIR in rank and self.THREECARDS in rank:
            return self.HANDS[1]
        elif length == 1 and rank[0] == self.THREECARDS:
            return self.HANDS[2]
        elif length == 2 and rank.count(2) == self.ONEPAIR:
            return self.HANDS[3]
        elif length == 1 and rank[0] == self.ONEPAIR:
            return self.HANDS[4]
        else:
            return '--'

    def run(self, cards):
        suits = re.findall(r'(S|H|D|C)+', cards)
        ranks = re.findall(r'(A|J|Q|K|2|3|4|5|6|7|8|9|10)+', cards)

        suit_len = len(suits)
        rank_len = len(ranks)
        amount = len(''.join(suits)) + len(''.join(ranks))
        if suit_len == 5 and rank_len == 5 and len(cards) == amount:
            print(suits)
            print(ranks)
            self.calculate_rank(ranks)
            result = self.calculate_hand(self.DATA)
        else:
            result = 'Suit or Rank not correct format'
        return result


def main():
    argv = sys.argv
    if len(argv) > 1:
        hand = POKERHANDS()
        if argv[1] == '-r':
            generate = 5
            if len(argv) > 2:
                if argv[2].isdigit():
                    generate = int(argv[2])
            for idx in range(generate):
                card = hand.generate_card()
                print('card: {0}' . format(card))
                result = hand.run(card)
                print('-> {0}' . format(result))
        elif argv[1] == '-p':
            if len(argv) > 2 and argv[2]:
                print('card: {0}' . format(argv[2]))
                result = hand.run(argv[2])
                print('-> {0}' . format(result))
            else:
                print('Please enter card!')
                print('python poker_hand.py -p <card>')
        elif argv[1] == '-h' or argv[1] == '--help':
            print('--Help')
            print('--execute with one card')
            print('python poker_hand.py -p <card>')
            print('--execute with auto generate card')
            print('python poker_hand.py -r <length>')
            print('default <length> is 5')
        else:
            print('python poker_hand.py -h|--help for more infomations')
    else:
        print('python poker_hand.py -h|--help for more infomations')


if __name__ == '__main__':
    main()
