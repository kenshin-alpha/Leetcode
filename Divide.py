def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        count = 0
        endstr = str(dividend)
        sorstr = str(divisor)
        if(endstr[0] == "-" and sorstr[0] != "-"):
            endstr = int(endstr[1:])
            sorstr = int(sorstr)
            while(endstr>=sorstr):
                endstr = endstr - sorstr
                count = count + 1
            return "-" + str(count)
        if(endstr[0] != "-" and sorstr[0] == "-"):
            endstr = int(endstr)
            sorstr = int(sorstr[1:])
            while(endstr>=sorstr):
                endstr = int(endstr) - sorstr
                count = count + 1
            return "-" + str(count)         
        if(endstr[0] == "-" and sorstr[0] == "-"):
            endstr = int(endstr[1:])
            sorstr = int(sorstr[1:])
            while(endstr>=sorstr):
                endstr = endstr - sorstr
                count = count + 1
            return str(count)
        if(endstr[0] != "-" and sorstr[0] != "-"):
            while(dividend>=divisor):
                dividend = dividend - divisor
                count = count + 1
            return count
        
print(divide(-2147483648,-1))