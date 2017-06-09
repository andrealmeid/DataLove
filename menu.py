# biblioteca para implementar os menus de consultas e insercoes
from querys import *
from insercoes import *

## QUERYS ##
def printQuerys():
    print("consultas disponíveis: ")
    print("gas: Todos os spotteds")
    print("gac: Todos os comentários")
    print("gat: Todos as tags")
    print("gap: Todos as pessoas")
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
    print("gsa: spotteds anônimos:")
    print("gse: spotteds escritos por uma pessoa")
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

        # get all spotteds
        elif cmd == "gas":
            data = getAllSpotteds(cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print("| ", end="")
                    for item in post:
                        print(str(item) + " | ", end="")
                    print()
                print()

        # get all comentarios
        elif cmd == "gac":
            data = getAllComentarios(cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print("| ", end="")
                    for item in post:
                        print(str(item) + " | ", end="")
                    print()
                print()

        # get all tags
        elif cmd == "gat":
            data = getAllTags(cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print("| ", end="")
                    for item in post:
                        print(str(item) + " | ", end="")
                    print()
                print()

        # get all people
        elif cmd == "gap":
            data = getAllPessoas(cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print("| ", end="")
                    for item in post:
                        print(str(item) + " | ", end="")
                    print()
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
                print("Curso          |   Instituto")
                print(data[0][0] + " | " + data[0][1])

        # pessoas que reagiram a um spotted
        elif cmd == "rs":
            spotted = input("Digite o id do spotted: ")
            data = getReacaoSpotted(spotted, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                print("Nome    | Tipo")
                print("--------|--------")
                for post in data:
                    print(post[0] + " | " + post[1])
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
                    print("Nome      |  Comentário")
                    print("----------|------------")
                    print(post[0] + " | " + post[1])
                print()
        elif cmd == "gsa":
            data = getSpottedAnonimo(cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    if post[2]:
                        print("Data e Horário      | Spotted Anônimo")
                        print("------------------- | ---------------")
                        print(post[2] + " | " + post[1])
                        print()
                    else:
                        print("Spotted Anônimo")
                        print("---------------")
                        print(post[1])
                        print()
                print()
        elif cmd == "gse":
            nome = input("Digite o nome: ")
            data = getSpottedEscrito(nome, cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print(post[1])
                    print()
                print()
        # retorna ao menu principal
        elif cmd == "q":
            return

        # mostra opcoes
        elif cmd == "h":
            printQuerys()

        else:
            print("Comando não reconhecido.")

## INSERTIONS ##
def printInsertions():
    print("inserções disponíveis: ")
    print("p  : insere uma pessoa")
    print("s  : insere um spotted")
    print("h  : mostra esse menu")
    print("q  : volta ao menu principal\n")

def menuInsertions(connection, cursor):
    printInsertions()

    while (True):
        cmd = input("insert > ")

        # insere uma pessoa
        if cmd == "p":
            nome = input("Digite o nome: ")
            idade = input("Digite a idade (default = NULL): ")
            inserePessoa(cursor, nome, idade)
            connection.commit()
            print()

        # insere um spotted
        if cmd == "s":
            texto = input("Digite o texto: ")
            horario = input("Digite a data e horario (YYYY-MM-DD HH:MM:SS): ")
            cita = input("Digite o id da pessoa citada (default = NULL): ")
            autor = input("Digite o id do autor (default = NULL): ")
            insereSpotted(cursor, texto, horario, cita, autor)
            connection.commit()
            print()

        # retorna ao menu principal
        elif cmd == "q":
            return

        # mostra opcoes
        elif cmd == "h":
            printQuerys()

        else:
            print("Comando não reconhecido.")
