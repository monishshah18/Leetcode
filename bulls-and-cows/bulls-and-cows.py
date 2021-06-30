class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cow,bull = 0,0
        hash_table = dict()
        for i,j in zip(secret,guess):
            if i==j:
                bull += 1
            else:
                if i not in hash_table:
                    hash_table[i] = 1
                else:
                    if hash_table[i] < 0:
                        cow += 1
                    hash_table[i] += 1
                if j not in hash_table:
                    hash_table[j] = -1
                else:
                    if hash_table[j] > 0:
                        cow += 1
                    hash_table[j] -= 1
        return str(bull)+'A'+str(cow)+'B'
        