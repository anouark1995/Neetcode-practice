class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = m+n-1
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[pointer] = nums1[m-1]
                m-=1
            else:
                nums1[pointer] = nums2[n-1]
                n-=1
            pointer-=1
        while n>0:
            nums1[pointer] = nums2[n-1]
            n, pointer = n-1, pointer-1
        return nums1

    

                

sol = Solution()
print(sol.merge([10,20,20,40,0,0], 4, [1,2], 2))
print(sol.merge([10,0,0],1,[1,50], 2))