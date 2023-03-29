1- Ler dois números inteiros, diferentes de zero, representando o dividendo e o divisor. Calcular e imprimir o quociente e o resto da divisão.

dividendo= int(input("Dividendo: "))
divisor= int(input("Divisor: "))
quociente=dividendo//divisor
resto=dividendo%divisor
print("Quociente: ", quociente)
print("Resto: ", resto)

2- Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
D= R+S/2, onde R= (A+B)² e S= (B+C)²

A=int(input("Digite o número A: "))
B=int(input("Digite o número B: "))
C=int(input("Digite o número C: "))
R=(A+B)**2
S=(B+C)**2
D=(R+S)/2
print("O valor da expressão é: ", D)

3- Uma professora precisa calcular a média de um aluno. O aluno realizou 3 provas, sendo que a primeira prova tem peso 1, a segunda tem peso 2 
e a terceira prova tem peso 3. Escreva um programa que leia o nome do aluno e as notas, calcule e apresente a média ponderada do aluno.

nome=input("Nome do aluno: ")
nota1=float(input("Digite a nota 1: "))
nota2=float(input("Digite a nota 2: "))
nota3=float(input("Digite a nota 3: "))
final=((nota1*1)+(nota2*2)+(nota3*3))/6
print("Média final:", final)

4-Uma doceira levou pães de mel para vender em uma feira de gastronomia. Escreva um algoritmo que calcule o lucro obtido pela doceira na feira, 
baseando-se na quantidade vendida e nos preços de custo e de venda da unidade, considerando que o valor gasto pela doceira com o aluguel do stand foi de R$ 500.00.

gasto=float(input("Qual foi o gasto?"))
stand=500
custo=gasto+stand
quantidade=int(input("Qual foi a quantidade vendida?"))
unidade=int(input("Qual foi o valor por unidade?"))
lucro=(quantidade*unidade)-custo
print("O lucro foi de: ", lucro, "reais")

5- Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas em um mês e o valor que ele recebeu por hora. 
Imprima o número e o salário que o funcionário receberá no final do mês.

numero=input("Digite o número do funcionário: ")
horas=float(input("Digite o número de horas trabalhadas:"))
valor=float(input("Digite o valor ganho por hora: "))
salario=horas*valor
print("Número:", numero)
print("Salário:", salario)

6-João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. 
Faça um programa que leia o valor do salário, o valor de cada uma das contas, calcule e mostre o valor que João pagou em cada conta e quanto restará do salário do João.

salario=float(input("Insira o salário: "))
conta1=float(input("Insira o valor da conta 1: "))
conta2=float(input("Insira o valor da conta 2: "))
total_conta1=conta1+(conta1*0.02)
total_conta2=conta2+(conta2*0.02)
resto=salario-(total_conta1+total_conta2)
print("Valor conta 1: ", total_conta1, "reais")
print("Valor conta 2:", total_conta2, "reais")
print("Sobrará para João:", resto, "reais")
