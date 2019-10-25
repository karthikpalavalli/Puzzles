class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        new_number = str()

        number_map = dict()
        number_map["0"] = "0"
        number_map["1"] = "1"
        number_map["6"] = "9"
        number_map["8"] = "8"
        number_map["9"] = "6"

        for digit in reversed(num):
            if digit not in number_map.keys():
                return False

            new_number += number_map[digit]

        if new_number == num:
            return True

        return False
