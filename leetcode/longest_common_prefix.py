class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        number_of_strs = len(strs)

        if number_of_strs == 0:
            return ""

        elif number_of_strs == 1:
            return strs[0]

        else:
            predicted_common_prefix = strs[0]

            for i in range(1, len(strs)):
                while True:
                    if not predicted_common_prefix:
                        return ""

                    if predicted_common_prefix != strs[i][:len(predicted_common_prefix)]:
                        predicted_common_prefix = predicted_common_prefix[:-1]

                    else:
                        break

            return predicted_common_prefix


if __name__ == "__main__":
    test_strings = ["flower", "flow", "flight"]
    lcp = Solution()
    predicted_lcp = lcp.longestCommonPrefix(test_strings)
    print(predicted_lcp)