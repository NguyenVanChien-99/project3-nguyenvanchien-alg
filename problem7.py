
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root= RouteTrieNode(root_handler)

    def insert(self, parts_of_path,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root

        for part in parts_of_path:
            if part not in current.parts:
                current.insert(part)
            current= current.parts[part]
        current.handler=handler

    def find(self,parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current= self.root
        
        for part in parts:
            if part not in current.parts:
                return None
            current= current.parts[part]

        return current.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.parts ={}
        self.handler=handler

    def insert(self, part):
        self.parts[part]= RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler,default_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routers= RouteTrie(root_handler)
        self.default_handler=default_handler
        self.root_path="/"

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path== self.root_path:
            return
        self.routers.insert(self.split_path(path),handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        parts = []
        if path != self.root_path:
            parts= self.split_path(path)
        handler = self.routers.find(parts)
        if handler is None:
            return self.default_handler
        return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[len(path)-1]=="/":
            path=path[1:len(path)-1]
        else:
            path=path[1:]
        return path.split("/")


# Here are some test cases and expected outputs you can use to test your implementation

#normal case
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/category", "category handler")  # add a route
router.add_handler("/product/1", "product handler")  # add a route

# some lookups with the expected output
print("pass" if router.lookup("/")=="root handler" else "Failed") # should print 'root handler'
print("pass" if router.lookup("/home")=="not found handler" else "Failed") # should print 'not found handler' or None if you did not implement one
print("pass" if router.lookup("/home/about")=="about handler" else "Failed") # should print 'about handler'
print("pass" if router.lookup("/home/about/")=="about handler" else "Failed") # should print 'about handler' or None if you did not handle trailing slashes
print("pass" if router.lookup("/home/about/me")=="not found handler" else "Failed") # should print 'not found handler' or None if you did not implement one
print("pass" if router.lookup("/home/category")=="category handler" else "Failed") # should print 'category handler'
print("pass" if router.lookup("/product/1")=="product handler" else "Failed") # should print 'product handler'

#Add same path
router.add_handler("/product/1", "different handler") 
print("pass" if router.lookup("/product/1")=="different handler" else "Failed") # should print 'different handler'

#Empty router
router2= Router("root handler 2","Default handler 2")
print("pass" if router2.lookup("/home")=="Default handler 2" else "Failed") # should print 'different handler'