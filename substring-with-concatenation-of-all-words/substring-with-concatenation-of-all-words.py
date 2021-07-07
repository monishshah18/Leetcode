class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        window_size = 0
        res = []
        word_len = len(words[0])
        for word in words:
            window_size += len(word)
        for i in range(0, len(s)-window_size+1):
            sub_str = s[i:i+window_size]
            word_dict = Counter(words)
            for j in range(0,len(words)):
                individual_words = sub_str[word_len*j: word_len*(j+1)]
                if individual_words not in word_dict:
                    break
                else:
                    word_dict[individual_words] -= 1
            if self.valid_str(word_dict):
                res.append(i)
        return res
    
    def valid_str(self, word_dict):
        for word in word_dict:
            if word_dict[word]!=0:
                return False
        return True
            
            
        