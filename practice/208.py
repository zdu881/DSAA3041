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


class Trie:
	def __init__(self):
		# TODO: initialize your data structure here
		pass

	def insert(self, word: str) -> None:
		# TODO: insert the word into the trie
		pass

	def search(self, word: str) -> bool:
		# TODO: return True iff word exists
		return False

	def startsWith(self, prefix: str) -> bool:
		# TODO: return True iff any inserted word has this prefix
		return False
