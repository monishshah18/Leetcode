class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = collections.Counter()
        for cp in cpdomains:
            n, s = cp.split()
            count[s] += int(n)
            for i in range(len(s)):
                if s[i] == '.':
                    count[s[i+1:]] += int(n)
        return [" ".join((str(j),i)) for i,j in count.items()]