class Node:
    def __init__(self):
        self.child =  defaultdict(Node)
        self.content = ""
class FileSystem:

    def __init__(self):
        self.root = Node()
    
    def find(self, path):
        curr = self.root
        if len(path)==1:
            return self.root
        for word in path.split("/")[1:]:
            curr = curr.child[word]
        return curr

    def ls(self, path: str) -> List[str]:
        curr = self.find(path)
        if curr.content:
            return [path.split("/")[-1]]
        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath)
        curr.content += content 

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.find(filePath)
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)