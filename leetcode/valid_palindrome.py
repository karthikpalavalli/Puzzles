import string


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         valid_palindrome = True
#         ptr1 = 0
#         ptr2 = len(s) - 1
#
#         allowed_characters = string.ascii_letters + ''.join([str(i) for i in range(0, 10)])
#
#         while ptr1 < ptr2:
#             while s[ptr1] not in allowed_characters:
#                 ptr1 += 1
#
#             while s[ptr2] not in allowed_characters:
#                 ptr2 -= 1
#
#             print(ptr1, ptr2)
#
#             if ptr1 < ptr2:
#                 if s[ptr1].lower() != s[ptr2].lower():
#                     valid_palindrome = False
#                     break
#
#                 ptr1 += 1
#                 ptr2 -= 1
#
#         return valid_palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_palindrome = True

        allowed_characters = string.ascii_letters + ''.join([str(i) for i in range(0, 10)])
        filtered_s = list(filter(lambda x: x in allowed_characters, s))

        ptr1 = 0
        ptr2 = len(filtered_s) - 1

        while ptr1 < ptr2:
            if filtered_s[ptr1].lower() != filtered_s[ptr2].lower():
                valid_palindrome = False
                break

            ptr2 -= 1
            ptr1 += 1

        return valid_palindrome


if __name__ == "__main__":
    test_string = "A man, a plan, a canal: Panama"
    sol = Solution()
    print(sol.isPalindrome(test_string))
