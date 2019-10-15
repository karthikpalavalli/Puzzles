from typing import List
from operator import itemgetter


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=itemgetter(0))

        count_meeting_rooms = 1
        max_overlap = 1

        if len(sorted_intervals) == 0:
            return 0

        for idx in range(1, len(sorted_intervals)):
            if sorted_intervals[idx][0] < sorted_intervals[idx - 1][1]:
                count_meeting_rooms += 1

            else:
                max_overlap = max(max_overlap, count_meeting_rooms)
                count_meeting_rooms = 0

        max_overlap = max(max_overlap, count_meeting_rooms)

        return max_overlap