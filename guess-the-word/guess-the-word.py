# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def pair_sum(w1,w2):
            return sum(i==j for i,j in zip(w1,w2))
        def most_overlap_word():
            counts = [[0 for _ in range(26)] for _ in range(6)]
            for word in candidates:
                for i,c in enumerate(word):
                    counts[i][ord(c)-ord('a')] += 1
            best_score = 0
            for word in candidates:
                score = 0
                for i,c in enumerate(word):
                    score += counts[i][ord(c)-ord('a')]
                if score > best_score:
                    best_score = score
                    best_word = word
            return best_word
                
        candidates = wordlist[:]
        while candidates:
            s = most_overlap_word()
            matches = master.guess(s)
            if matches == 6:
                return
            candidates = [w for w in candidates if pair_sum(s,w)==matches]
            