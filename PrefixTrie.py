"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_dict: Dict[str, Trie] = dict()
        self.has_end = False
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        c = word[0]
        if c not in self.trie_dict:
            self.trie_dict[c] = Trie()
        if len(word) == 1:
            self.trie_dict[c].has_end = True
        else:
            self.trie_dict[c].insert(word[1:])
        
    def startsWithTrie(self, prefix: str) -> bool:
        if len(prefix) == 1:
            return self.trie_dict.get(prefix[0], None)
        else:
            return self.trie_dict.get(prefix[0]).startsWithTrie(prefix[1:]) if prefix[0] in self.trie_dict else None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trieStartsWith = self.startsWithTrie(word)
        return trieStartsWith and trieStartsWith.has_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trieStartsWith = self.startsWithTrie(prefix)
        return trieStartsWith


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
