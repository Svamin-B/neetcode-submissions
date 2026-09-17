class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        words = {}
        answer = []
        for word in strs:
            if words.get(''.join(sorted(word)), None) is None:
                words[''.join(sorted(word))] = i
                i += 1
                answer.append([])
        
        for word in strs:
            answer[words[''.join(sorted(word))]].append(word)

        return answer