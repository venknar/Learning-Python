class Solution:
    
    def twoSum(self, A, B):
        
        result = []

        if (len(A) == 0):
            return result

        tracker = {}
        index = 1;
        for i in A:
            if (i not in tracker):
                diff = B - i
                if (diff not in tracker):
                    tracker[diff] = []
                tracker[diff].append(index)
            else:
                result.append(tracker[i][0])
                result.append(index)
                break
            
            index = index + 1
                  
        return result


s = Solution()
index = s.twoSum([2,3,1,8], 5)
print(index)