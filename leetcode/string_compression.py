class Solution():
    def compress(self, chars):
        anchor_pointer = 0
        write_pointer = 0
        current_count = 0

        chars.append("0")

        for index, ch in enumerate(chars):
            if ch == chars[anchor_pointer]:
                current_count += 1

            else:
                if current_count > 1:
                    chars[write_pointer] = chars[anchor_pointer]
                    write_pointer += 1

                    for digit_str in str(index - anchor_pointer):
                        chars[write_pointer] = digit_str
                        write_pointer += 1

                elif current_count == 1:
                    chars[write_pointer] = chars[anchor_pointer]
                    write_pointer += 1

                anchor_pointer = index
                current_count = 1

        return write_pointer


if __name__ == "__main__":
    sol = Solution()
    test_arr = ["a", "a", "b", "b", "c", "c", "c"]
    # test_arr = ["a", "b", "c"]
    sol.compress(test_arr)
    print(test_arr)
