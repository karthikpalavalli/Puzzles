class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        input_str = s

        max_chars_seen_len = 0

        if len(input_str) == 1:
            return 1

        for i in range(len(input_str)):
            hashmap_seen = [0 for it in range(128)]
            hashmap_seen[ord(input_str[i])] = 1
            len_temp = 0

            for j in range(i + 1, len(input_str)):
                if hashmap_seen[ord(input_str[j])]:
                    len_temp = j - i
                    break
                if j == len(input_str) - 1:
                    len_temp = j - i + 1
                    break
                hashmap_seen[ord(input_str[j])] = 1

            if len_temp > max_chars_seen_len:
                max_chars_seen_len = len_temp

        return max_chars_seen_len