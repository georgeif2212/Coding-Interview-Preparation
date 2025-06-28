from collections import defaultdict
def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        # Sort the string to create a key
        key = ''.join(sorted(s)) 
        print(f"String: {s}, Key: {key}")
        ans[key].append(s)
    
    return list(ans.values())



groupedAnagrams=groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(groupedAnagrams)  # Expected output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]