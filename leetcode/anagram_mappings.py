class Solution(object):

    def generate_index_dict(self, list_x):
        index_dict = dict()

        for index, value in enumerate(list_x):
            index_dict[value] = index

        return index_dict

    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        index_dict_B = self.generate_index_dict(B)
        mapping_list = list()

        for val in A:
            mapping_list.append(index_dict_B[val])

        return mapping_list