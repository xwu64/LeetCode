class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        dec = ['1','2','3','4','5','6','7','8','9','0']
        try:
            if len(IP) >= 7 and len(IP) <= 15:
                segments = IP.split('.')

                if len(segments) == 4:
                    for each in segments:
                        if len(each) <=0 or len(each) > 3:
                            return "Neither"

                        for i in each:
                            if not i in dec:
                                return "Neither"

                        if int(each) < 0 or int(each) > 255:
                            return "Neither"

                        if len(each) > 1:
                            if each[0] == '0':
                                return "Neither"
                    return "IPv4"

            hex = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','A','B','C','D','E','F']
            if len(IP) >= 15 and len(IP) <=39:
                segments = IP.split(':')

                if len(segments) == 8:
                    for each in segments:
                        if len(each) <=0 or len(each) > 4:
                            return "Neither"

                        for i in each:
                            if not i in hex:
                                return "Neither"

                    return "IPv6"
        except :
            return "Neither"

        return "Neither"
