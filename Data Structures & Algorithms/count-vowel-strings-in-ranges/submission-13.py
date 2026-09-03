class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # vowels = set("aeiou")
        # res = []

        # for query in queries:
        #     li = query[0]
        #     ri = query[1] + 1
        #     total_count = 0
        #     for ele in range(li, ri):
        #         word = words[ele]
        #         if word[0] not in vowels:
        #             continue
        #         if word[-1] not in vowels:
        #             continue
        #         total_count += 1
        #     res.append(total_count)
        #     total_count = 0
        # return res

        vowels = set("aeiou")
        map_vowel = [0]

        for word in words:
            if word[0] not in vowels or word[-1] not in vowels:
                map_vowel.append(map_vowel[-1])
            else:
                map_vowel.append(map_vowel[-1] + 1)

        res = []

        for li, ri in queries:
            res.append(map_vowel[ri + 1] - map_vowel[li])

        return res