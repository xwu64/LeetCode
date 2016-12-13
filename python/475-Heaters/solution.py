class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        houses.sort()
        heaters.sort()

        radius = 0

        i = j = 0

        while i<len(houses):
            if j==0 and houses[i] < heaters[j]:
                radius = max(radius, abs(houses[i]-heaters[j]))
                i+=1

            elif houses[i] >= heaters[j] and j+1<len(heaters) and houses[i] <= heaters[j+1]:
                radius = max(radius, min(abs(houses[i]-heaters[j]), abs(houses[i]-heaters[j+1])))
                i+=1

            elif j+1>=len(heaters):
                radius = max(radius, abs(houses[i]-heaters[j]))
                i+=1


            else:
                j+=1

        return radius


