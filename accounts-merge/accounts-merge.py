class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited_accounts = [False] * len(accounts)
        email_account_map = defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_account_map[email].append(i)
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbour in email_account_map[email]:
                    dfs(neighbour, emails)
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
        