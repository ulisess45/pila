from Pila import Stack

def verificar(cadena):
    p=Stack()
    tmp=0
    while tmp < 0 and len(cadena):
        simbolo=cadena[i]
        if cadena in "([{":
            p.push('@')
        elif cadena in ")]}":
            p.pop()
    tmp+=1
    if p.is_empty():
        print("Esta balanceado")
    if p.is_empty == '@' :
        print("No esta balanceado")

    return cadena

def main():
    archivo=open('c.txt','r')
    contenido=archivo.read()
    print(verificar(contenido))

main()

