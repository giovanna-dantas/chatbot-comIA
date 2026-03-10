# listas
lista_nova = []
nomes = ['João', 'Maria', 'Pedro']
print(nomes[0])
print(nomes)

nomes.append('Ana') #add infos na lista
print(nomes)

# dicionario

#dicionario = {chave: valor, chave: valor}
idades={"gio": 19, "marcos": 20}
print(idades['gio'])#pega info no dic-> dicionario[chave]
idades["Miguel"] = 5 #add info
idades['gio'] = 20 #editando
print(idades)

# role = quem é o usuario
# content = conteudo da mensagem
mensagem1 = {"role": "assistant", "content": "Bora aprender PY"}
mensagem2 = {"role": "user", "content": "Vamos sim"}
mensagem3 = {"role": "assistant", "content": "Começando Aula..."}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Opa, agora vamos colocar Python para jogo!"}
lista_mensagens.append = (nova_mensagem)

print(lista_mensagens)