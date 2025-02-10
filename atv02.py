class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.pedidos = []  

    def fazer_pedido(self, produto, preco, estoque):
        pedido = Pedido(produto, preco, estoque, self)  
        self.pedidos.append(pedido)  

    def listar_pedidos(self):
        if not self.pedidos:
            return "Este cliente não fez nenhum pedido."
        return "\n".join(str(pedido) for pedido in self.pedidos)  

    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.telefone}"

class Pedido:
    def __init__(self, produto, preco, estoque, cliente):
        self.produto = produto
        self.preco = preco
        self.estoque = estoque
        self.cliente = cliente  

    def __str__(self):
        return f"Produto: {self.produto}, Preço: {self.preco}, Estoque: {self.estoque}, Cliente: {self.cliente.nome}"


cliente1 = Cliente("João Silva", "1234-5678")


cliente1.fazer_pedido("Produto A", 100.0, 10)
cliente1.fazer_pedido("Produto B", 50.0, 5)
cliente1.fazer_pedido("Produto C", 150.0, 2)


print(cliente1)
print("Pedidos feitos por João:")
print(cliente1.listar_pedidos())
