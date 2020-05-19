"""day14_implement_trie_(prefix_tree).py
    Created by Aaron at 14-May-20"""
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for x in word:
            node = node.children[x]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]
        return True

    # app2
    # def search(self, word: str, is_word=True) -> bool:
    #     """
    #     Returns if the word is in the trie.
    #     """
    #     node=self.root
    #     for x in word:
    #         if node not in node.children:
    #             return False
    #         node=node.children[x]
    #     return node.is_word if is_word else True

    # def startsWith(self, prefix: str) -> bool:
    #    """
    #    Returns if there is any word in the trie that starts with the given prefix.
    #    """
    #    return self.search(prefix, False)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

run=Trie()
a,b=["Trie","insert","search","search","startsWith","insert","search"],[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
result=[]
node=run.root
for x in range(1, len(a)):
    result.append(eval('run.{}(\'{}\')'.format(a[x], b[x][0])))
print(result)
# app1 use startWith and search with same method
# app2 more compact, use startWith in search with additional parameter