class Solution:
    def trap(self, height: List[int]) -> int:
        pref, post = [], []
        curr = -1
        for i in height:
            if curr == -1:
                pref.append(curr)
                if i > 0:
                    curr = i                       
            else:
                pref.append(curr)
                if i >= curr:
                    curr = i
        curr = -1
        for i in range(len(height)-1, -1, -1):
            if curr == -1:
                post.append(curr)
                if height[i] > 0:
                    curr = height[i]    
            else:
                post.append(curr)
                if height[i] >= curr:
                    curr = height[i]
        
        storage = 0
        n = len(height) - 1
        for i in range(len(height)):
            if pref[i] > -1 and post[n-i] > -1:
                if min(pref[i], post[n-i]) - height[i] > 0:
                    storage += min(pref[i], post[n-i]) - height[i]
        return storage
        