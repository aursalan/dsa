class TrieNode:
    def __init__(self, isEnd = False):
        self.children = {} 
        self.isEnd = isEnd

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        current = self.root

        if word[0] not in current.children:

            for i in word:

                current.children[str(i)] = TrieNode()
                current = current.children[str(i)]
            
            current.isEnd = True
        
        else:

            for i in word:

                if str(i) in current.children:
                    current = current.children[str(i)]
                
                else:

                    current.children[str(i)] = TrieNode()
                    current = current.children[str(i)]
                
            current.isEnd = True
            

    def search(self, word: str) -> bool:
        
        current = self.root
        
        for i in word:

            if i not in current.children:
                return False 
            current = current.children[i]
                
        return current.isEnd
                
        
    def startsWith(self, prefix: str) -> bool:
        
        current = self.root

        for i in prefix:
            if i not in current.children:
                return False

            current = current.children[i]

        return True