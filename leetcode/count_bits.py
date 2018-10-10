class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        number_of_high_bits = []

        for i in range(num):
            curr_num = i
            count = 0

            while curr_num:
                curr_num = curr_num & (curr_num-1)
                count += 1

            number_of_high_bits.append(count)

        return number_of_high_bits