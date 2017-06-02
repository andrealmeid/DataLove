#!/bin/python3
import sqlite3 as sql
import sys
from querys import *

# funcao que conecta no database de nome 'database_file'
# se for bem sucedida retorna um cursor; se nao printa uma mensagem de erro e sai
def connectDatabase(database_file):
    print("Conectando ao banco de dados " + database_file + "...")

    try:
        connection = sql.connect(database_file)
        print("Conexão bem sucedida!\n")
        return connection.cursor()

    except Error as e:
        print("Falha ao conectar ao banco de dados.")
        print(e)
        sys.exit(1)

def printHelp():
    print("Comando disponíveis:")
    print("gs : consulta os Spotteds recebido por uma pessoa")
    print("gf : consulta os fenótipos de uma pessoa citada no Spotted")
    print("gl : consulta os locais em que a pessoa que recebeu o Spotted estava quando o recebeu")
    print("lc : consulta o lugar mais citado em spotteds")
    print("q  : sai do programa")
    print("h  : mostra esse menu\n")

def main():
    print("DataLove (Ɔ) Copyleft RCG 2017")
    cursor = connectDatabase('datalove.sqlite')
    printHelp()
    while(True):
        cmd = input("> ")

        # help
        if cmd == "h":
            printHelp()

        # quit
        elif cmd == "q":
            sys.exit(0)

        # get spotted
        elif cmd == "gs":
            nome = input("Digite o nome: ")
            data = getSpotted("'"+nome+"'", cursor)
            if data == []:
                print("Nenhum resultado.")
            else:
                for post in data:
                    print(post[0])
                print()

        # get fenotipo
        elif cmd == "gf":
            nome = input("Digite o nome: ")
            data = getFenotipo("'"+nome+"'", cursor)
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
            data = getLocal("'"+nome+"'", cursor)
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

        else:
            print("Comando não reconhecido.")

main()
