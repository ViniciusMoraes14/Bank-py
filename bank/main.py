from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

c1 = Cliente('Vini',20)
c2 = Cliente('Maria',18)
c3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254106, 0)
conta2 = ContaPoupanca(2222, 987323, 1300)
conta3 = ContaCorrente(3333, 432131, 8000)

c1.inserir_conta(conta1)
c2.inserir_conta(conta2)
c3.inserir_conta(conta3)

c1.conta.sacar(20)
c2.conta.sacar(150)
c3.conta.sacar(800)


