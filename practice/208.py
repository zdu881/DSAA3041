"""\
Problem: 208. Implement Trie (Prefix Tree)
Source: https://leetcode.com/problems/implement-trie-prefix-tree/
Difficulty: Medium
Tags: Design, Trie, String

Description (rephrased):
Design a Trie (prefix tree) for storing lowercase English words.

Implement the following operations:
- Trie(): initialize the data structure.
- insert(word): insert a word into the trie.
- search(word): return True if the exact word exists in the trie.
- startsWith(prefix): return True if there exists any inserted word
  that starts with the given prefix.

Example (sequence):
- insert("apple")
- search("apple") -> True
- search("app") -> False
- startsWith("app") -> True
- insert("app")
- search("app") -> True

Constraints (from the platform statement, summarized):
- 1 <= len(word), len(prefix) <= 2000
- word/prefix contain only lowercase English letters
- Up to 3 * 10^4 calls total

Approach:
Use a TrieNode with:
- children: dict[char, TrieNode]
- is_end: bool

Time Complexity: O(L) per operation, where L is the input length
Space Complexity: O(total characters inserted)
"""


class _TrieNode:
    """Trie 的节点。

    - children: dict，key 是字符，value 是下一个节点
    - is_end:  是否有某个单词在这里结束
    """

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        """初始化 Trie。

        Trie 的核心是“根节点 root”。
        root 本身不代表任何字符，只是所有单词的起点。
        """
        self.root = _TrieNode()

    def insert(self, word: str) -> None:
        """把一个单词插入到 Trie 中。"""
        node = self.root
        for ch in word:
            # 如果这条边不存在，就新建一个子节点
            if ch not in node.children:
                node.children[ch] = _TrieNode()
            node = node.children[ch]
        # 走到单词最后一个字符对应的节点，做结束标记
        node.is_end = True

    def search(self, word: str) -> bool:
        """查询：Trie 中是否存在“完整的单词”word。"""
        node = self._find_node(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        """查询：Trie 中是否存在以 prefix 为前缀的单词。"""
        return self._find_node(prefix) is not None

    def _find_node(self, s: str):
        """沿着字符串 s 的路径往下走，返回最后的节点。

        - 如果中途某个字符不存在对应的子节点，返回 None。
        - 如果能走完，返回最后停下的那个节点。
        """
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


if __name__ == "__main__":
    # 简单自测：作为脚本运行时才会执行，不影响 LeetCode 提交。
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    print("OK")
