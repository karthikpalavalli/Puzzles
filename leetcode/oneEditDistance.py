class Solution:

    def isOneEditDistance(self, s, t):

        shorter_string = s
        longer_string = t

        if len(s) > len(t):
            shorter_string = list(t)
            longer_string = list(s)

        if len(longer_string) - len(shorter_string) > 1:
            return False

        already_modified = False
        one_edit_distance = True

        for i in range(len(shorter_string)):
            if shorter_string[i] != longer_string[i]:
                if already_modified:
                    one_edit_distance = False
                    break

                elif len(shorter_string) < len(longer_string):
                    del longer_string[i]
                    already_modified = True
                    i -= 1

                else:
                    already_modified = True

        return one_edit_distance
