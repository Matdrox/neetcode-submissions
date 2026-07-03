class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = {}

        for word in strs:
            word_sorted = ''.join(sorted(word))
            print(word_sorted)

            if word_sorted in strs_sorted:
                print(f"Found {word}")
            else:
                strs_sorted[word_sorted] = []

            strs_sorted[word_sorted].append(word)

        res = list(strs_sorted.values())
        print(res)
        return res