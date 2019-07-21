class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        arrLength = len(quality)
        tempPay = []
        sumWage = 2147483647
        payout = sumWage
        for i in range(arrLength):
            wageRate = float(wage[i])/float(quality[i])
            
            
            print ('case ' + str(i))
            tempK = 0
            tempOut = sumWage
            tempPay[:] = []
            
            for j in range(arrLength):
                if quality[j] * wageRate >= wage[j]:
                    tempK = tempK + 1
                    tempPay.append(quality[j] * wageRate)
            
            print ('wage Rate: ' + str(wageRate))
            print ('qualified: ' + str(tempK))
            print (tempPay)
            
            if tempK >= K:
                tempPay.sort()
                tempOut = sum(tempPay[:K])
            
            print ('current result: ' + str(tempOut))
            
            if tempOut < payout:
                payout = tempOut
                
            print ('current payout: ' + str(payout))
        
        return payout



quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
K = 3

test = Solution()
x = test.mincostToHireWorkers(quality, wage, K)
print (x)