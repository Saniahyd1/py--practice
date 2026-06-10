class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        if sort_s == sort_t:
            return True
        return False
s = input("Enter the first string: ")
t = input("Enter the second string: ")
solution = Solution()
print(solution.isAnagram(s, t))