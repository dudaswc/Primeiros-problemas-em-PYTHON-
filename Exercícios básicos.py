1- Faça um programa que leia o nome e duas notas de um aluno, calcule e apresente seu nome e a sua média aritmética, no seguinte modelo: Fulano obteve a média XX.
nome=input("nome")

nota1=float(input("nota1"))
nota2=float(input("nota2"))
nota=(nota1+nota2)/2
print(nome, "obteve a média:", nota)


2- Faça um programa que leia 2 valores reais, calcule e imprima:
- a soma dos números;
- o dobro da soma dos números.

valor1=float(input("valor1"))
valor2=float(input("valor2"))
soma=valor1+valor2
dobro=(valor1+valor2)*2
print("soma:", soma)
print("dobro:", dobro)


3- O restaurante “Tudo Gostoso” cobra R$ 30.00 pelo quilo de refeição. Escreva um
programa que lê o peso do prato cheio de um cliente (em quilos) e imprima o valor a
pagar.
* Considere que o peso do prato é 0.1 Kg.

kg= float(input("kg"))
pkg=30
total=float(pkg-0.8)*kg
print("o total a pagar é:", total)


4- Antes do racionamento de energia ser decretado, quase ninguém falava em quilowatts, mas agora, todos a incorporaram a seu vocabulário. Sabendo que cada quilowatt de energia custa um centésimo do salário mínimo, escreva um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta em uma residência, calcule e imprima o valor pago pela residência em questão.

salario=float(input("salario"))
valorkw=salario/100
gasto=float(input("gasto"))
total=gasto*valorkw
print("total a pagar:", total)


5- Uma fábrica produz dois tipos de clips, plástico ou metal, sendo que a caixa de cada tipo é vendida por 5 e 10 reais, respectivamente. Faça um algoritmo em que o usuário forneça a quantidade de caixas vendidas de clips de plástico e de metal e informe qual será o valor arrecadado com cada um dos tipos e o valor total arrecadado.

metal=10
plastico=5
vendasm= int(input("informe a quantidade de metal vendido"))
vendasp=int(input("informe a quantidade de plastico vendido"))
totalm=vendasm*metal
totalp=vendasp*plastico
total=totalm+totalp
print(totalm)
print(totalp)
print(total)
