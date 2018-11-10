class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        valid_emails = set()

        for email in emails:
            local_name, domain = email.split('@')

            local_name = local_name.split('+')[0]
            local_name = "".join(local_name.split('.'))

            valid_emails.add(local_name + domain)

        return len(valid_emails)


if __name__ == "__main__":
    sol = Solution()
    sol.numUniqueEmails(["test.email+alex@leetcode.com",
                         "test.e.mail+bob.cathy@leetcode.com",
                         "testemail+david@lee.tcode.com"])