class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        changed.sort()
        output = []
        for i in changed:
            if i*2 in changed[changed.index(i)+1:]:
                changed.pop(changed.index(i*2))
                output.append(i)
            else:
                return []
        return output