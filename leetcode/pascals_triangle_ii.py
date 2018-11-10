class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        elements_list = list()
        elements_list.append(1)

        if rowIndex == 0:
            return elements_list

        else:
            for val in range(rowIndex):
                elements_list.append(elements_list[val] * (rowIndex - val) / (val + 1))

            return elements_list
