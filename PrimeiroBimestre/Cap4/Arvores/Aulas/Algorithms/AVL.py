


class AVL():
    def __init__(self):
        self.root = None
        self.height = 1
        self.insertNode = None



    def insert(self, node, value):
        if node is None:
            return node(value)
        
        if self.getBalance(node) <= 1:
            if value < node.value:
                node.left = self.insert(node.left, value)
            else:
                node.right = self.insert(node.right, value)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        balance = self.getBalance(node)
        






    def getBalance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def seach(self, value):
        x = self.root
        while x is not None and x.value != value:
            if value < x.value:
                x = x.left
            else:
                x = x.right
        return x
    
    def leftRotation(self, node):

        # condições inicias
        nodeB = node.right
        # nodeB = node.right significa que nodeB está apontando para o filho direito de node
        bLeft = nodeB.left
        # node.right = nodeB.left significa que o node está recebendo o apontamento do filho esquerdo de nodeB

        # inicio da rotação
        nodeB.left = node # a esquerda do meu nó B vai apontar para o nó que está sendo rotacionado
        node.right = bLeft # a direita do meu nó que está sendo rotacionado vai apontar para o filho esquerdo de B

        return nodeB
    
    def rightRotation(self, node):

        # condições iniciais
        nodeA = node.left
        aRight = nodeA.right

        # inicio da rotação
        nodeA.right = node
        node.left = aRight

        return nodeA
    

if __name__ == "__main__":
    avl = AVL()







