class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node()
        self.right=Node()

        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
    
    def insert_atbeg(self,node):
        first=self.left.next
        node.prev=self.left
        node.next=first
        self.left.next=node
        first.prev=node
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert_atbeg(node)
        return node.value

        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.insert_atbeg(node)
        if len(self.cache)>self.capacity:
            last_node=self.right.prev
            self.remove(last_node)
            del self.cache[last_node.key]
        
        
