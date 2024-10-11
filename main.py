class Node:
    def __init__(self,name):
        self.name = name
        self.locked = None
        self.desc = {}

class Tree:
    def __init__(self,names,m):
        self.m = m
        self.nodes = []
        self.index = {}
        for i, name in enumerate(names):
            self.nodes.append(Node(name))
            self.index[name] = i
    
    def hasLockedAnc(self,i):
        while i >= 0:
            if self.nodes[i].locked:
                return True
            i = (i-1)//self.m
        return False

    def lock(self,name,id):
        i = self.index[name]
        node = self.nodes[i]
        if node.desc or self.hasLockedAnc(i):
            return False
        node.locked = id
        parent = (i-1)//self.m
        while parent >= 0:
            desc = self.nodes[parent].desc
            if id not in desc:
                desc[id] = set()
            desc[id].add(i)
            parent = (parent-1)//self.m
        return True
    
    def unlock(self,name,id):
        i = self.index[name]
        node = self.nodes[i]
        if node.locked != id:
            return False
        node.locked = None
        parent = (i-1)//self.m
        while parent >= 0:
            desc = self.nodes[parent].desc
            desc[id].remove(i)
            if not desc[id]:
                del desc[id]
            parent = (parent-1)//self.m
        return True

    def upgrade(self,name,id):
        i = self.index[name]
        node = self.nodes[i]
        if self.hasLockedAnc(i) or id not in node.desc or len(node.desc) > 1:
            return False
        for desc in node.desc[id]:
            self.unlock(self.nodes[desc].name,id)
        return True

for _ in range(int(input())):
    n, m, t = map(int,input().split())
    a = input().split()
    tree = Tree(a,m)
    for _ in range(t):
        op = input().split()
        k, name, id = int(op[0]), op[1], int(op[2])
        if k == 1:
            print(tree.lock(name,id))
        elif k == 2:
            print(tree.unlock(name,id))
        else:
            print(tree.upgrade(name,id))
