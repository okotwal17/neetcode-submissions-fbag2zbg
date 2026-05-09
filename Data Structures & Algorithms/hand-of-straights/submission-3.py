from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hashmap = Counter(hand)
        hand.sort()
        for card in hand:
            if hashmap[card]:
                for i in range(card, card + groupSize):
                    if not hashmap[i]:
                        return False
                    hashmap[i] -= 1
        return True
                    

                