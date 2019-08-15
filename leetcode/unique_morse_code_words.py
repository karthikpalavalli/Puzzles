from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformation_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                               "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                               "-.--", "--.."]
        transformed_word_set = set()

        for word in words:
            morse_code = str()
            for letter in word:
                morse_code += transformation_list[ord(letter) - ord('a')]
            transformed_word_set.add(morse_code)

        return len(transformed_word_set)