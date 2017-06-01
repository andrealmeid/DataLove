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

def main():
    cursor = connectDatabase('datalove.sqlite')
    data = getSpotted("'Mateus Camilli'", cursor)
    print(data)

main()
