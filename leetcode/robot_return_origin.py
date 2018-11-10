from collections import Counter

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_count = Counter(moves)

        if moves_count['U'] == moves_count['D'] and moves_count['L'] == moves_count['R']:
            return 'true'

        return 'false'
