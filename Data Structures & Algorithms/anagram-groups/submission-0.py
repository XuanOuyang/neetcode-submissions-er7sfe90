class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        # key stop : value unsorted word
        # if sorted value == key then they are both put into div 1
        for i in range(len(strs)):
            srtd = str(sorted(strs[i]))
           
            if srtd not in mydict:
                mydict[srtd] = [strs[i]]
            else:
                mydict[srtd].append(strs[i])

        result = []
        for g in mydict.values():
            result.append(g)
        return result