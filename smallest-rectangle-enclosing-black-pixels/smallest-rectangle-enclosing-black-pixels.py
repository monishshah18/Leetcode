class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        top = self.search(0,x,lambda mid: '1' in image[mid])
        bottom = self.search(x+1, len(image), lambda mid: '1'not in image[mid])
        left = self.search(0,y,lambda mid: any(image[k][mid]=='1' for k in range(top,bottom)))
        right = self.search(y+1, len(image[0]), lambda mid: all(image[k][mid]=='0' for k in range(top,bottom)))
        return (right-left)*(bottom-top)
    
    def search(self,i,j,check):
        while i != j:
            mid = (i+j)//2
            if check(mid):
                j = mid
            else:
                i = mid + 1
        return i