class Solution:
    def defangIPaddr(self, address) -> str:
        defanged_ip = str()

        for ch in address:
            if ch == '.':
                defanged_ip += "[.]"
                continue

            defanged_ip += ch

        return defanged_ip
