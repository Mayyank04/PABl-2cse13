class Solution:
    def minMaxArray(self,arr):
        min=arr[0]
        max=arr[0]
        for num in arr:
            if num < min:
                min=num
            if num>max:
                max=num
        return [min,max]
        
        
        
        
        
obj=Solution()
arr=[1,2,3,4,3,2,4,81,3,9]
result=obj.minMaxArray(arr)
print("Min", result[0])
print("Min", result[1])