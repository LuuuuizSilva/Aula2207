lista_nome = []
lista_notas = []

contador = 0

# Lista para adicionar os nomes e notas dos alunos 
while contador != 3:
    print("==="*10)
    nome = input("Digite o nome do aluno: ")
    lista_nome.append(nome)
    
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    
    contador += 1

contador_media = 0
contador_lista = 0

# Verifica aprovação
while contador_media != 3:
    print("")
    nota1 = lista_notas[contador_lista]
    nota2 = lista_notas[contador_lista + 1]
    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f"{lista_nome[contador_media]} foi Aprovado :)")
    else:
        print(f"{lista_nome[contador_media]} foi Reprovado :(")
    
    print("")
    contador_media += 1
    contador_lista += 2

print("Programa Finalizado!!")

