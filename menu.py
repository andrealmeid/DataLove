# biblioteca para implementar os menus de consultas e insercoes
from querys import *

## QUERYS ##
def printQuerys():
    print("consultas disponíveis: ")
    print("gs : consulta os Spotteds recebido por uma pessoa")
    print("gf : consulta os fenótipos de uma pessoa citada no Spotted")
    print("gl : consulta os locais em que a pessoa que recebeu o Spotted estava quando o recebeu")
    print("lc : consulta o lugar mais citado em spotteds")
    print("h  : mostra esse menu")
    print("q  : volta ao menu principal\n")

def menuQuerys(cursor):
    printQuerys()

    while (True):
        cmd = input("query > ")

        # get spotted recebido
        if cmd == "gs":
            nome = input("Digite o nome: ")
            data = getSpottedRecebido(nome, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print(post[0])
                print()

        # get fenotipo
        elif cmd == "gf":
            nome = input("Digite o nome: ")
            data = getFenotipo(nome, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                print("Nome  |  Tipo")
                print("------|------")
                for post in data:
                    print(post[0] + " | " + post[1])
                print()

        # get lugar
        elif cmd == "gl":
            nome = input("Digite o nome: ")
            data = getLocal(nome, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                print("Lugar  |  Evento")
                print("-------|--------")
                for post in data:
                    print(post[0] + " | " + post[1])
                print()

        # lugar mais comum
        elif cmd == "lc":
            data = getLocalMaisComum(cursor)
            print(data[0] + ", com " + str(data[2]) + " citações durante " + data[1] + ".")

        # retrona ao menu principal
        elif cmd == "q":
            return

        # mostra opcoes
        elif cmd == "h":
            printQuerys()

        else:
            print("Comando não reconhecido.")
