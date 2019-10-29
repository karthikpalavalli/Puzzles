class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str_list = list(str(num))

        if not num_str_list:
            return 0

        max_ch = num_str_list[0]
        max_index = 0
        for index, ch in enumerate(num_str_list):
            if ch > max_ch:
                max_ch = ch
                max_index = index

        temp = num_str_list[0]
        num_str_list[0] = num_str_list[max_index]
        num_str_list[max_index] = temp

        return int("".join(num_str_list))