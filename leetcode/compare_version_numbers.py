class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split('.')
        version2_list = version2.split('.')

        if len(version1_list) > len(version2_list):
            version2_list += ['0'] * (len(version1_list) - len(version2_list))

        elif len(version2_list) > len(version1_list):
            version1_list += ['0'] * (len(version2_list) - len(version1_list))

        for itr in range(len(version1_list)):
            if int(version1_list[itr]) > int(version2_list[itr]):
                return 1

            elif int(version2_list[itr]) > int(version1_list[itr]):
                return -1

        return 0
