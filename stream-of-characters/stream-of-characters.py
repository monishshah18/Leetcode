class StreamChecker:
    def rollingHash(self, Hash, p_power, c, mod=1e9+7):
        return ((Hash + ord(c) * p_power) % mod, (p_power*31) % mod)

    def __init__(self, words: List[str]):
        self.suffix_hash, self.word_hash, self.query_stream = set(), set(), deque()
        for w in words:
            Hash, p_pow = 0,1
            for c in w[::-1]:
                Hash, p_pow = self.rollingHash(Hash, p_pow, c)
                self.suffix_hash.add(Hash)
            self.word_hash.add(Hash)

    def query(self, letter: str) -> bool:
        self.query_stream.appendleft(letter)
        Hash, p_pow = 0, 1
        for c in self.query_stream:
            Hash, p_pow = self.rollingHash(Hash, p_pow, c)
            if Hash not in self.suffix_hash:
                return False
            elif Hash in self.word_hash:
                return True
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)