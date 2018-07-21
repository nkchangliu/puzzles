def path_sum(root, sum):
   if not root:
       return False
   if root.val == sum:
       return True
   return path_sum(root.left, sum - root.val) or path_sum(root.right, sum - root.val)
