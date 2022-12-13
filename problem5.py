from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word= False
        self.chars={}

    def insert(self, char):
        ## Add a child node in this Trie
        self.chars[char]= TrieNode()

    def __str__(self) -> str:
        return 'is word: {}, chars: {}'.format(self.is_word,self.chars)

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        out = []
        if self.is_word and suffix !='':
            out.append(suffix)
        for char in self.chars:
            out+=self.chars[char].suffixes(suffix+char)
        return out

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root= TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.chars:
                current_node.insert(char)
            current_node=current_node.chars[char]
        current_node.is_word=True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.chars:
                return None
            current_node= current_node.chars[char]
        return current_node



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(prefixNode.suffixes())
        else:
            print(prefix + " not found")
    else:
        print('')
# Normal case
print("Case 1 :Expected :",["ger","onometry"])
f("trig")

#Not found
print("Case 2 :Expected : ayx not found")
f("ayx")

#Dont have any suffix
print("Case 3 :Expected : []")
f("trigger")

#Empty Trie
tre2 = Trie()
print("Case 4 :Expected : aaa not found")
fNode = tre2.find("aaa")
if fNode:
    print("Failed")
else:
    print("aaa not found")

#Add same word
print("Case 5 :Expected :",['ello'])
tre2.insert("hello")
fNode2= tre2.find("h")
if fNode2:
    print("Before: ",fNode2.suffixes())
else:
    print("Failed")
tre2.insert("hello")
fNode2= tre2.find("h")
if fNode2:
    print("After: ",fNode2.suffixes())
else:
    print("Failed")