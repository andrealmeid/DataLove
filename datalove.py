#!/bin/python3
import sqlite3 as sql
import sys
from querys import *

# funcao que conecta no database de nome 'database_file'
# se for bem sucedida retorna um cursor; se nao printa uma mensagem de erro e sai
def connectDatabase(database_file):
    try:
        connection = sql.connect(database_file)
        return connection.cursor()

    except sql.Error:
        print("Falha ao conectar ao banco de dados.")
        sys.exit(1)

def printHelp():
    print("\nComando disponíveis:")
    print("q  : sai do programa")
    print("gs : pega Spotteds recebido por uma pessoa")
    print("h  : mostra esse menu\n")

def main():
    cursor = connectDatabase('datalove.sqlite')
    print("DataLove (Ɔ) Copyleft RCG 2017")
    printHelp()
    while(True):
        cmd = input("> ")

        if cmd == "h":
            printHelp()

        elif cmd == "q":
            sys.exit(0)

        elif cmd == "gs":
            nome = input("Digite o nome: ")
            data = getSpotted("'"+nome+"'", cursor)
            if data == None:
                print("Nenhum resultado.\n")
            else:
                print(data)
                print()

        else:
            print("Comando não reconhecido.")

main()
