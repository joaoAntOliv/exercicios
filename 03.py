#Escreva uma função que recebe uma lista de números e retorna a média.
def calcula_media(lista):
    if len(lista) == 0:
        return 0  
    else:
        soma = sum(lista)  
        media = soma / len(lista) 
        return media
    
lista = [1, 2, 3, 4, 5]
media = calcula_media(lista)
print(media)  