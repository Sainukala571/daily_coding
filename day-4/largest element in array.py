    class Solution:
    def largest(self, arr):
        # code here
        largest=arr[0]
        n= len(arr)
        for i in range(1,n):
            if arr[i]>largest:
                largest=arr[i]
        return largest
