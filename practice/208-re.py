class TreNode :
    def __init__(self):
        self.Children = {}
        self.isend : bool = False


class Trie:
    def __init__(self):
        """初始化 Trie。

        Trie 的核心是“根节点 root”。
        root 本身不代表任何字符，只是所有单词的起点。
        """
        self.root = TreNode()

    def insert(self,word:str)-> None:
        node = self.root
        for ch in word:
            if ch not in node.Children:
                node.Children[ch]= TreNode()
            node = node.Children[ch]
        node.isend= True
    def findnode(self,word:str)->TreNode:
        node = self.root
        for ch in word:
            if node not in node.Children :
                return None
            node = node.Children[ch]
        return node

    def start_with(self, word:str) -> bool:
        return self.findnode(word) is not None
    def search(self,word:str)->bool:
        res = self.findnode(word)
        return res is not None and res.isend == True
        