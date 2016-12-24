class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        def validNext(str1, str2):
            flag = True
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    if flag is True:
                        flag = False
                    else:
                        return False
            return True

        result = 0
        now = [start]

        while 1:
            if end in now:
                return result

            if len(bank) == 0:
                return -1

            next = []
            for each in now:
                for item in bank:
                    if validNext(each, item):
                        next.append(item)
            now = set(next)

            for each in now:
                bank.remove(each)

            if len(now) == 0:
                return -1

            result +=1
