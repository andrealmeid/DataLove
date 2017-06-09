#!/bin/python3
# -*- coding: utf-8 -*-
import sqlite3 as sql
import sys
from menu import *
from insercoes import *

# funcao que conecta no database de nome 'database_file'
# se for bem sucedida retorna um cursor; se nao printa uma mensagem de erro e sai
def connectDatabase(database_file):
    print("Conectando ao banco de dados " + database_file + "...")

    try:
        connection = sql.connect(database_file)
        print("Conexão bem sucedida!\n")
        return connection

    except Error as e:
        print("Falha ao conectar ao banco de dados.")
        print(e)
        sys.exit(1)

def printHelp():
    print("Comando disponíveis:")
    print("c : entra no menu de consultas")
    print("i : entra no menu de inserções")
    print("h : mostra esse menu")
    print("q : sai do programa\n")


def main():
    print("DataLove (Ɔ) Copyleft RCG 2017")
    connection = connectDatabase('datalove.sqlite')
    cursor = connection.cursor()
    printHelp()
    while(True):
        cmd = input("> ")

        # help
        if cmd == "h":
            printHelp()

        # quit
        elif cmd == "q":
            sys.exit(0)

        # menu de consultas/query
        elif cmd == "c":
            menuQuerys(cursor)

        # menu de insercoes
        elif cmd == "i":
            menuInsertions(connection, cursor)

        else:
            print("Comando não reconhecido.")

main()
