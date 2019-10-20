from typing import List
from operator import itemgetter


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_meetings = sorted(intervals, key=itemgetter(0))

        can_attend = True

        for idx in range(1, len(sorted_meetings)):
            if sorted_meetings[idx][0] < sorted_meetings[idx - 1][1]:
                can_attend = False
                break

        return can_attend
