# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBalancedBST(self, left, right):
        if left > right:
            return None
        if left == right:
            node = TreeNode(val = self.nums[left])
            if self.root == None:
                self.root = node
            return node
        
        
        mid = left + ((right-left)//2)
        node = TreeNode(val = self.nums[mid])
        if self.root == None:
            self.root = node
            
        
        node.left = self.createBalancedBST(left, mid-1)
        node.right = self.createBalancedBST(mid+1, right)
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        self.root = None
        self.createBalancedBST(0, len(self.nums)-1)
        return self.root
        