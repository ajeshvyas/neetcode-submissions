class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        res = []

        for query in queries:
            li = query[0]
            ri = query[1] + 1
            total_count = 0
            for ele in range(li, ri):
                word = words[ele]
                if word[0] not in vowels:
                    continue
                if word[-1] not in vowels:
                    continue
                total_count += 1
            res.append(total_count)
            total_count = 0
        return res