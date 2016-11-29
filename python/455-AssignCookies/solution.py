class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        g.reverse()
        s.sort()
        s.reverse()

        i=j=0
        result = 0
        while 1:
           if i >= len(g) or j >= len(s):
               return result

           if g[i] > s[j]:
               i+=1
           else:
               i+=1
               j+=1
               result+=1
