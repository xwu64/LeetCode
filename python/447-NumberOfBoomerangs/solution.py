from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        result = 0

        for i in range(len(points)):
            d = defaultdict(int)
            for j in range(len(points)):
                if i==j:
                    continue
                distance = (points[i][0]-points[j][0]) ** 2 + (points[i][1]-points[j][1]) ** 2
                d[distance]+=1

            for each in d:
                    if d[each] < 2:
                        continue
                    result = result + d[each]*(d[each]-1)

        return result


