class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def checkSubsequence(word_str):
            curr_pos = -1
            for i in word_str:
                if indexes[i]:
                    pos = bisect.bisect_right(indexes[i], curr_pos)
                    if pos == len(indexes[i]):
                        return False
                    curr_pos = indexes[i][pos]
                else:
                    return False
            return True
        
        indexes = defaultdict(list)
        for i,j in enumerate(s):
            indexes[j].append(i)
        hashmap = {}
        count = 0
        
        for word in words:
            if word not in hashmap:
                if checkSubsequence(word):
                    count += 1
                    hashmap[word] = True
                else:
                    hashmap[word] = False
            else:
                if hashmap[word]:
                    count += 1
        return count
        