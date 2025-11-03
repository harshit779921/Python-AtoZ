class Solution:
    def isIsogram(self, s='otkyhmxzykq'):
        # Your code here
        char = ''
        for i in s.lower():
            if i not in char:
                char += i
            else:
                return False
        return True


# Test
sol = Solution()
print(sol.isIsogram())       # For default 'otkyhmxzykq'
print(sol.isIsogram('lamp')) # Another test
print(sol.isIsogram('apple')) # Should return False
              