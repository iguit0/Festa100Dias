<h1 align="center">Festa100Dias :tada::money_with_wings::bank: </h1>

Mecanismos de controle de concorrência foram desenvolvidos originalmente para a solução de problemas
de sistemas operacionais. Contudo, na contemporaneidade, diversos domínios de problemas incluem mais
de uma entidade que co-existem e executam atividades simultaneamente, como estações em uma rede de
comunicações ou moléculas em uma solução. Logo, este trabalho pretende implementar uma solução para
um problema de controle de concorrência entre processos utilizando a linguagem de programação Python. O
problema consiste em diferentes tipos de clientes realizando acessos simultâneos a uma conta poupança.

## Objetivo :pushpin:

O presente trabalho tem como objetivo implementar um programa concorrente, utilizando a linguagem
de programação Python, que faça o controle de concorrência entre diversos processos que são disparados
simultaneamente. O programa implementado utilizara objetos da classe **Condition()** encontrada na biblioteca
threading, padrão do Python.

## Problema :mag:

O contexto do problema proposto envolve a organização de uma festa de 100 dias para a formatura de
uma turma da universidade. Para ter controle sobre o dinheiro envolvido na organização da festa, um dos
integrantes teve a ideia de abrir uma conta poupança em um banco.
A conta aberta pela comissão organizadora é compartilhada por várias pessoas (consideradas como processos
na implementação do trabalho). Cada pessoa pode depositar ou sacar fundos dessa conta. O saldo
atual da conta é a soma de todos os depósitos até o momento menos a soma de todos os saques até o momento.
O saldo da conta, em situação nenhuma, não pode ser negativo. Os depósitos e os saques são realizados
por ordem de chegada.
Uma vez que o saldo da conta não é suficiente para realizar um saque em um valor X, a pessoa (ou
processo) deverá esperar em uma fila (em ordem [FIFO](https://pt.wikipedia.org/wiki/FIFO)) até que um depósito
num valor suficiente para que o saque seja efetuado seja realizado. Considere um processo A que esteja esperando
para sacar 200 reais, um processo B que esteja esperando para sacar 100 reais e o saldo atual da conta de 0 reais.
Mesmo com um processo C depositando 100 reais e o saldo atual da conta sendo atualizado para 100 reais, o processo A
tem prioridade de saque maior do que o processo B. Logo, até que o processo A realize seu saque, o processo B
permanecerá em espera.
Para o problema foram definidos seis tipos de clientes:
- Um cliente que saca 100 reais;
- Um cliente que saca 200 reais;
- Um cliente que saca 300 reais;
- Um cliente que deposita 100 reais;
- Um cliente que deposita 200 reais;
- Um cliente que deposita 300 reais.
Para uma melhor visualização da execução do problema, na implementação serão criados vinte clientes
de cada tipo que chegarão ao banco para realizar suas tarefas em ordem aleatória a cada 2 segundos.

## Resultados :chart_with_upwards_trend::clipboard:

Ao implementar o problema proposto, os resultados foram positivos. Foi possível, com a
utilização da classe **Condition()**, fazer a sincronização entre os processos e exibir sempre mensagens na tela
para uma melhor visualização do que está sendo executado em cada momento.

## Referências :books:

- https://docs.python.org/3.5/library/threading.html?highlight=threading#condition-objects;
- https://docs.python.org/2/library/threading.html#condition-objects;
- Python Cookbook [David Beazley & Brian K. Jones][O’REILLY].
