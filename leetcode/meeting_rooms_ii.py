from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        start_times = sorted([item[0] for item in intervals])
        end_times = sorted([item[1] for item in intervals])

        idx_start = idx_end = 0
        max_rooms = 0
        count_rooms = 0

        while idx_start < len(intervals):
            if start_times[idx_start] >= end_times[idx_end]:
                count_rooms -= 1
                idx_end += 1

            count_rooms += 1
            idx_start += 1

            max_rooms = max(max_rooms, count_rooms)

        return max_rooms


if __name__ == "__main__":
    meeting_intervals = [[1,5],[8,9],[8,9]]

    sol = Solution()
    print(sol.minMeetingRooms(meeting_intervals))
