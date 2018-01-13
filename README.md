# POKER HANDS
This is a very simple tool check poker hand.

Poker hands and the descriptions of them:

Hands | Description | String to output
--- | --- | ---
*Four cards* | `4 cards out of 5 has the same Rank.` | **4C**
*Full House* | `5 cards include One pair and Three cards. ` | **FH**
*Three cards* | `3 cards out of 5 have the same Rank.` | **3C**
*Two pairs* | `5 cards include 2 pairs.` | **2P**
*One pair* | `2 cards out of 5 have the same rank.` | **1P**
#### Example:
##### run with auto generate card
```
python poker_hands.py -r
```
**>>> output**
```
C3HJH7CQHQ
['C', 'H', 'H', 'C', 'H']
['3', 'J', '7', 'Q', 'Q']
--> 1P
CQD2H8H3CJ
['C', 'D', 'H', 'H', 'C']
['Q', '2', '8', '3', 'J']
--> --
S3C5DQHJC7
['S', 'C', 'D', 'H', 'C']
['3', '5', 'Q', 'J', '7']
--> --
DAS8DQHKH8
['D', 'S', 'D', 'H', 'H']
['A', '8', 'Q', 'K', '8']
--> 1P
DJS8HJD5HK
['D', 'S', 'H', 'D', 'H']
['J', '8', 'J', '5', 'K']
--> 1P
```
##### run with one parameter (card)
```
python poker_hands.py -p D4C4C8D8S4
```
***>>> output***
```
D4C4C8D8S4
['D', 'C', 'C', 'D', 'S']
['4', '4', '8', '8', '4']
--> FH
```
#### Usage:
```
- run with auto generate card
poker_hands.py [-r] [length]
- run with one parameter (card)
poker_hands.py [-p] [card]

arguments:
  -h, --help        show more infomation
  -r                generate card, default length is 5
  -p                parameter one card
```
Only tested on Python 3.6.
