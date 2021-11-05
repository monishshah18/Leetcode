class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dicts = defaultdict(list)
        for k, v in zip(keyName, keyTime):
            hour,minute = map(int, v.split(':'))
            time = hour*60 + minute
            dicts[k].append(time)
        names = []
        for name, time_list in dicts.items():
            time_list.sort()
            dq = collections.deque()
            for time in time_list:
                dq.append(time)
                if dq[-1] - dq[0] > 60:
                    dq.popleft()
                if len(dq) >= 3:
                    names.append(name)
                    break
        return sorted(names)