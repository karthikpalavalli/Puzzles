class Solution:
    def toGoatLatin(self, S: str) -> str:
        words_list = S.split()
        result_word_list = list()

        for idx, word in enumerate(words_list):
            new_word = str()
            if word[0].lower() in "aeiou":
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"

            new_word += "a" * (idx + 1)
            result_word_list.append(new_word)

        return " ".join(result_word_list)
