# biblioteca para implementar os menus de consultas e insercoes
from querys import *

## QUERYS ##
def printQuerys():
    print("consultas disponíveis: ")
    print("gs : Spotteds recebido por uma pessoa")
    print("gf : fenótipos de uma pessoa citada no Spotted")
    print("gl : locais em que a pessoa que recebeu o Spotted estava quando o recebeu")
    print("lc : lugar mais citado em spotteds")
    print("fc : fenotipo mais comum")
    print("gc : curso de uma pessoa")
    print("rs : pessoas que reagiram a um spotted")
    print("sr : spotteds recentes")
    print("gsr: spotteds que uma pessoa reagiu")
    print("gcm: comentarios de uma pessoa")
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

        # fenotipo mais comum
        elif cmd == "fc":
            data = getFenotipoMaisComum(cursor)
            print(data[1] + " do tipo " + data[0] + " num total de " + str(data[2]) + " vezes.")

        # get curso
        elif cmd == "gc":
            nome = input("Digite o nome: ")
            data = getCurso(nome, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                print(data[0][0])

        # pessoas que reagiram a um spotted
        elif cmd == "rs":
            spotted = input("Digite o id do spotted: ")
            data = getReacaoSpotted(spotted, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                print("Nome    | Data e Horario")
                print("--------|---------------")
                for post in data:
                    print(post[0] + " | " + post[2])
                print()

        # spotteds recentes
        elif cmd == "sr":
            data = getSpottedsRecentes(cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                print("Data e Horario      |  Spotted")
                print("--------------------|---------")
                for post in data:
                    print(post[2] + " | " + post[1])
                print()

        # spotteds que uma pessoa reagiu
        elif cmd == "gsr":
            nome = input("Digite o nome: ")
            data = getReacaoPessoa(nome, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                print("Reacao |  Spotted")
                print("-------|---------")
                for post in data:
                    print(post[1] + " | " + post[0])
                print()

        # comentarios de uma pessoa
        elif cmd == "gcm":
            nome = input("Digite o nome: ")
            data = getComentarios(nome, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print(post[0])
                    print("--> " + post[1])
                print()

        # retorna ao menu principal
        elif cmd == "q":
            return

        # mostra opcoes
        elif cmd == "h":
            printQuerys()

        else:
            print("Comando não reconhecido.")
