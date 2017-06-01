# bibliteca com as consultas implementadas

# implementacao de Spotteds recebido por uma pessoa
def getSpotted(nome, cursor):
    cursor.execute("SELECT Spotted.texto FROM Spotted WHERE Spotted.cita = (SELECT id_pes FROM Pessoa WHERE nome = "+nome+")")
    return cursor.fetchone()

# implementacao de Fenótipos de uma pessoa
def getFenotipo(nome, cursor):
    return

# implementacao de Local que uma pessoa que recebeu o spotted estava

# implementacao de Locais mais comuns

# implementacao de Quais fenótipos mais comuns

# implementacao de Curso de uma pessoa
