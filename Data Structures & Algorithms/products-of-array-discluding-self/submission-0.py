import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1]
        zeros = []

        INT_MIN = -2**31       # -2,147,483,648
        INT_MAX = 2**31 - 1    #  2,147,483,647

        for ind,i in enumerate(nums):
            if i!= 0:
                p = prods[-1]
                if INT_MIN<=p*i<=INT_MAX:
                    prods[-1] = p*i
                else:
                    prods.append(i)
            else:
                zeros.append(ind)
        res = []
        if len(zeros)>1:
            return [0 for _ in nums]
        if len(prods) == 1 and len(zeros)==0:
            res = [prods[0]//i for i in nums]
        if len(zeros) == 1:
            res = [0 for i in nums]
            res[zeros[0]] = math.prod(prods)
        
        if len(zeros)==0 and len(prods)>1:
            res = [(prods[0]//i) * prods[1] for i in nums]


        return res