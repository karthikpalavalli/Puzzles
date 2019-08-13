class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        merged_intervals = list()

        for interval in intervals:
            if not merged_intervals or merged_intervals[-1].end < interval.start:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)

        return merged_intervals


if __name__ == "__main__":
    sol = Solution()

    intervals_input_list = [[1,3], [2,6], [8,10], [15,18]]

    intervals_obj_list = list()

    for interval_lval in intervals_input_list:
        new_int = Interval(interval_lval[0], interval_lval[1])
        intervals_obj_list.append(new_int)

    sol.merge(intervals_obj_list)
