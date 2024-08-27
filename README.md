preço_produto = 23
frete = 10
total_gasto = preço_produto + frete
iremos_falir = preço_produto / frete

#formatação
print(f"O preço do produto é de: {preço_produto}, o frete foi de: {frete}, o total gasto foi de: {total_gasto}.")


email_cliente = "gabriel@gmail.com"

#maiúscula
email_cliente = email_cliente.upper()
print(email_cliente)

#minúscula
email_cliente = email_cliente.lower()
print(email_cliente)

#como pegar um determinado texto. Ex:"@"
print(email_cliente.find("@")) #-1 quando não encontrar o valor
 
#tamanho do texto
print(len(email_cliente))

#pegar um caractere expecifico
print(email_cliente[4])

print(email_cliente[-4]) #"-" representa o número de trás pra frente

#pegar um pedaço do texto
print(email_cliente[:4])

#trocar um pedaço de um texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

#trabalho com nomes
nome = "Beethoven"
print(nome.capitalize())
print(nome.title())

#pegar o servidor do email

posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

#pegar o 1° nome

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]







#pegar o sobrenome

sobrenome = nome[posicao_espaco+1:]
print(primeiro_nome)
print(sobrenome)

#formatação númerica

iremos_falir = round(iremos_falir, 2)
print(f"Iremos falir já que, {iremos_falir:0%}")
