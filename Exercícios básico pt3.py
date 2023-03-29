1- Imagine que você é responsável por criar um programa para gerenciar as informações de um cadastro de clientes de uma loja virtual. 
Escreva um programa que leia os dados dos clientes (nome, e-mail e telefone) e os armazene em variáveis.
● O programa deve solicitar ao usuário que insira as informações do cliente e, em seguida, exibir os dados do cliente cadastrado na tela.

nome=input("Insira seu nome: ")
email=input("Insira seu e-mail: ")
telefone=int(input("Insira seu telefone: "))
print("Nome:", nome)
print("E-mail:", email)
print("Telefone:", telefone)

2-A loja de eletrônicos "TecnoPlus" está realizando uma promoção em que o cliente que se cadastrar no site da loja ganha um cupom de desconto de 10% 
para a primeira compra. Para se cadastrar, o cliente precisa informar seu nome completo e seu e-mail.
Escreva um código em Python que:
● Solicite ao usuário que informe seu nome completo e seu e-mail.
● Imprima na tela a mensagem: "Parabéns, <nome do usuário>! Seu cadastro foi realizado com sucesso e você ganhou um cupom de desconto de 10% para a sua primeira compra na TecnoPlus."
● Solicite ao usuário que informe o valor total de sua compra.
● Calcule o valor do desconto que o usuário terá direito.
● Imprima na tela a mensagem: "O valor total da sua compra é R$ <valor da compra>. Com o cupom de desconto, você terá um desconto de R$ <valor do desconto>, e o valor final a ser pago será de R$ <valor final>."

nome=input("Insira seu nome: ")
email=input("Insira seu e-mail: ")
print("Parabéns,", nome, "!", "Seu cadastro foi realizado com sucesso e você ganhou um cupom de desconto de 10% para a sua primeira compra na TecnoPlus.")
valor=float(input("Insira o valor da sua compra: "))
desconto=valor*0.1
final=valor-desconto
print("O valor total da sua compra é R$", valor,".", "Com o cupom de desconto, você terá um desconto de R$", desconto, "e o valor final a ser pago será de R$", final)

3-Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.
● Considere que o ano sempre tem 365 dias e que o mês sempre tem 30 dias.

idade=int(input("Insira sua idade:"))
meses=int(input("Agora insira quantos meses:"))
dias=int(input("E insira quantos dias:"))
anos_em_dias=idade*365
meses_em_dias=meses*30
idade_em_dias=anos_em_dias+meses_em_dias+dias
print("Sua idade em dias é:", idade_em_dias)
            
4-Faça um programa que obtenha o valor da hora trabalhada, a quantidade de horas trabalhadas na semana e o percentual de descontos com impostos,
para realizar o cálculo do salário do funcionário de uma empresa. Considerando que o mês comercial, para a realização do cálculo, é composto por 4.5 semanas.
Calcule e apresente:
a) o salário bruto (salário sem desconto);
b) o valor do desconto;
c) o salário líquido (salário bruto menos o desconto).

valor_hora=float(input("Insira o valor da hora trabalhada: "))
semana1=float(input("Insira a quantidade de horas trabalhadas na primeira semana: "))
semana2=float(input("Insira a quantidade de horas trabalhadas na segunda semana: "))
semana3=float(input("Insira a quantidade de horas trabalhadas na terceira semana: "))
semana4=float(input("Insira a quantidade de horas trabalhadas na quarta semana: "))
resto=float(input("Insira a quantidade de horas trabalhadas no restante do mês: "))

salario=(semana1+semana2+semana3+semana4+resto)*valor_hora
imposto=float(input("Insira o desconto do imposto: "))
desconto=(salario*imposto)/100
total=salario-desconto

print("Salário bruto":, salario, "reais")
print("Valor do desconto":, desconto, "reais")
print("Salário líquido":, total, "reais")
