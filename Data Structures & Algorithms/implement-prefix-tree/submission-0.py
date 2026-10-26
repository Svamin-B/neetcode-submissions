class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    """
    need a children dict
    need a end flag

    startswith walks down from root to last character of input and if at any point, it doesn't exist, we return false

    search walk down from root to last character of input and checks if last node.end = True. If yes then return true else false

    insert starts from root, checks if character already exists, if yes, go to it and repeat. Else insert into dict. Don't forget to label end
    """
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root

        for c in word:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                current_node.children[c] = Node()
                current_node = current_node.children[c]
        
        current_node.end = True

    def search(self, word: str) -> bool:
        current_node = self.root

        for c in word:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return False
        
        if current_node.end == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root

        for c in prefix:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return False
        return True
        