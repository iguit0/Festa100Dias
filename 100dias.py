# -*- coding: UTF-8 -*-

"""

*** OBSERVAÇÕES ***

* Integrantes do grupo:

	- Mateus Lopes (3897)
	- Igor Alves (3902)
	- Hugo Rodrigues (3653)

* O projeto proposto foi implementado utilizando um objeto da classe Condition()
* Todos os métodos utilizados na implementação são detalhados na documentação do projeto

"""

import threading #Biblioteca padrão do Python utilizada para implementação de programas concorrentes
import random
import time

#Classe utilizada para realizar os acessos à conta no banco
class Banco:
	#Método construtor da classe Banco
	def __init__(self):
		self.saldo = 0
		self.threadCondition = threading.Condition() #Declaração de um objeto Condition()

	#Método que realiza saques
	def sacar(self, valorSaque):
		self.threadCondition.acquire() #Chamada do método acquire() do objeto Condition()
		while self.saldo < valorSaque: #Verificação do saldo para saque
			print "Operação: Saque    | Valor:", valorSaque, " | Saldo:", self.saldo, " ERRO x000: Saldo Indisponível"
			self.threadCondition.wait() #Chamada do método wait() do objeto Condition()
		self.saldo -= valorSaque #Assim que o saldo for suficiente realiza o saque
		print "Operação: Saque    | Valor:", valorSaque, " | Saldo:", self.saldo
		self.threadCondition.notify() #Chamada do método notify() do objeto Condition()
		self.threadCondition.release() #Chamada do método release() do objeto Condition()

	#Método que realiza depósitos
	def depositar(self, valorDeposito):
		self.threadCondition.acquire() #Chamada do método acquire() do objeto Condition()
		self.saldo += valorDeposito #Realiza o depósito
		print "Operação: Depósito | Valor:", valorDeposito, " | Saldo:", self.saldo
		self.threadCondition.notify() #Chamada do método notify() do objeto Condition()
		self.threadCondition.release() #Chamada do método release() do objeto Condition()

#Classe utilizada para realizar saques. A classe estende a classe Thread
class Saque(threading.Thread):
	#Método construtor da classe Saque.
	def __init__(self, b, valor):
		threading.Thread.__init__(self) #O método define a classe como uma thread
		self.operacaoBanco = b #Definição de um objeto Banco()
		self.valorSaque = valor

	def run(self):
		self.operacaoBanco.sacar(self.valorSaque) #Chamada do método sacar() do objeto Banco()

#Classe utilizada para realizar depósitos. A classe estente a classe Thread
class Deposito(threading.Thread):
	#Método construtor da classe Deposito.
	def __init__(self, b, valor):
		threading.Thread.__init__(self) #O método define a classe como uma thread
		self.operacaoBanco = b #Definição de um objeto Banco()
		self.valorDeposito = valor

	def run(self):
		self.operacaoBanco.depositar(self.valorDeposito) #Chamada do método depositar() do objeto Banco()

b = Banco() #Declaração de um objeto Banco()

"""

Contadores que controlam a declaração de 20 threads de cada "tipo".
Foram utilizados 6 tipos diferentes:

	- Depósito de 100
	- Depósito de 200
	- Depósito de 300
	- Saque de 100
	- Saque de 200
	- Saque de 300

"""

cont1, cont2, cont3, cont4, cont5, cont6 = 1, 1, 1, 1, 1, 1

while cont1 < 20 or cont2 < 20 or cont3 < 20 or cont4 < 20 or cont5 < 20 or cont6 < 20:
	random.seed() #"Semente" que controla o sorteio de números pseudo aleatórios
	x = random.randrange(1, 6) #Número aleatório pertencente ao intervalo [1, 6]

	#Conforme o número sorteado um dos tipos de threads é definido
	#O método start() de cada thread é chamado a cada 2 segundos

	if x == 1 and cont1 <= 20:
		d = Deposito(b, 100)
		time.sleep(2)
		d.start()
		cont1 += 1

	if x == 2 and cont2 <= 20:
		d = Deposito(b, 200)
		time.sleep(2)
		d.start()
		cont2 += 1

	if x == 3 and cont3 <= 20:
		d = Deposito(b, 300)
		time.sleep(2)
		d.start()
		cont3 += 1

	if x == 4 and cont4 <= 20:
		s = Saque(b, 100)
		time.sleep(2)
		s.start()
		cont4 += 1

	if x == 5 and cont5 <= 20:
		s = Saque(b, 200)
		time.sleep(2)
		s.start()
		cont5 += 1

	if x == 6 and cont6 <= 20:
		s = Saque(b, 300)
		time.sleep(2)
		s.start()
		cont6 += 1

print "Prontos para a festa?"