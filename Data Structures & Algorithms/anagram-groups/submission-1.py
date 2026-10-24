class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        walk through the list of strings and find whether their sorted form exists in the hash map. If yes then append to the list of other anagrams. Otherwise make a new element of the sorted form in the hash map and append the word to it
        
        """
        words = {}
        answer = []
        for i in range(len(strs)):
            ordered = "".join(sorted(strs[i]))
            if ordered in words:
                words[ordered].append(strs[i])
            else:
                words[ordered] = [strs[i]]

        for key, vals in words.items():
            answer.append(vals)

        return answer
