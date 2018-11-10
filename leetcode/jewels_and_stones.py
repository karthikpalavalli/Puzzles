class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        is_jewel = [1 for s in S if s in J]
        return sum(is_jewel)