from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hashmap = Counter(hand)
        startSize = len(hand)
        hand.sort()
        for card in hand:
            if hashmap[card] != 0:
                for i in range(groupSize):
                    if not hashmap[card+i]:
                        return False
                    elif hashmap[card+i] > 0:
                        startSize-=1
                        hashmap[card+i]-=1
        return True if startSize == 0 else Fasle
                    

                