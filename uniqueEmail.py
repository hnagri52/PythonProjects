class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0
        actual = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            actual.add((local, domain))
        return len(actual)
