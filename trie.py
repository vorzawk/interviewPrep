class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = None

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        return '*' in cur

