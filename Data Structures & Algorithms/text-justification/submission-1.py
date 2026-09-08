class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        res = []
        formed_sentence = ""
        max_len = 0
        for idx, word in enumerate(words):
            if len(word) + max_len < maxWidth:
                formed_sentence += word + " "
                max_len = len(formed_sentence)
            elif len(word) + max_len == maxWidth:
                formed_sentence += word
                max_len = 0
                res.append(formed_sentence)
                formed_sentence = ""
            else:
                formed_sentence = formed_sentence.rstrip()
                sentence_words = formed_sentence.split()
                print(sentence_words)
                total_spaces = maxWidth - sum(len(w) for w in sentence_words)
                print(total_spaces)
                gaps = len(sentence_words) - 1
                if gaps == 0:
                    formed_sentence = sentence_words[0] + " " * total_spaces
                else:
                    spaces_per_gap = total_spaces // gaps
                    print(spaces_per_gap)
                    extra_spaces = total_spaces % gaps
                    print(extra_spaces)
                    formed_sentence = ""
                    for i in range(gaps):
                        formed_sentence += sentence_words[i]
                        formed_sentence += " " * (
                            spaces_per_gap + (1 if i < extra_spaces else 0)
                        )
                    formed_sentence += sentence_words[-1]
                res.append(formed_sentence)
                formed_sentence = word + " "
                max_len = len(formed_sentence)
        formed_sentence = formed_sentence.rstrip()
        if formed_sentence:
            formed_sentence += " " * (maxWidth - len(formed_sentence))
            res.append(formed_sentence)
        return res