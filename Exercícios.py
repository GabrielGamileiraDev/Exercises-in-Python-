#01 question

nome = "Maria Silva"
email = "maria_silva@gmail.com"
idade = 30
print(nome)
print(email)
print(idade)

#02 question

idade = int(input("Insira sua idade:"))
resultado = int(idade*12)
print("Sua idade em meses é de:", resultado, ".")


#03 question

nome = str(input("Insira seu nome:"))
endereco = str(input("Insira seu endereço:"))
telefone = int(input("Insira seu número de telefone:"))
cidade = str(input("Insira o nome da sua cidade:"))

print("Olá,", nome, ". Seu endereço é:", endereco, "Seu número de telefone é:", telefone, "Residente de:", cidade)


#04 question

raio = int(input("Digite o raio de um círculo ->"))
pi = float(3.14)
perimetro = 2*pi*raio
print("O perimetro do seu círculo é aproximadamente:", perimetro)


#05 question
aluno01 = str(input("Digite o nome do aluno:"))
media1 = int(input("Digite sua primeira nota"))
media2= int(input("Digite sua segunda nota"))
nota_final = (media1+media2)/2

aluno02 = str(input("Digite a nota do 2° aluno:"))
media1 = int(input("Digite sua primeira nota"))
media2= int(input("Digite sua segunda nota"))
resultado = (media1+media2)/2

diferenca = (nota_final - resultado)

print("A diferença entre eles é em média de:", diferenca, ".")


#06 question

base = int(input("Digite a medida da base:"))
altura = int(input("Digite a altura:"))
print (base * altura/2)

#07 question

numero = int(input("Escolha um respectivo número:"))
sucessor = int(numero + 1)
print("O sucessor do seu respectivo número é de:", sucessor)

#08 question

celsius = float(input("Escolha uma temperatura em Celsius:"))
fahrenheit = print(float(celsius * 9/5) +32)

#09 question

aleatoria = input("Qual produto deseja?")
produto = float(input("Qual o preço você deseja?"))
desconto = float(input("Quanto de desconto deseja?"))
valor_final = print(produto/desconto, ", este é o desconto deste produto.")
