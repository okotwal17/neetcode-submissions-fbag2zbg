class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False
        for elem in triplets:
            if elem[0] > target[0] or elem[1] > target[1] or elem[2] > target[2]:
                continue
            if elem == target:
                return True
            if elem[0] == target[0]:
                first = True
            if elem[1] == target[1]:
                second = True
            if elem[2] == target[2]:
                third = True
        return first and second and third
            
        