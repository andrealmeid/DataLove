# bibliteca com as consultas implementadas

# implementacao de Spotteds recebido por uma pessoa
def getSpotted(nome, cursor):
    cursor.execute("SELECT Spotted.texto FROM Spotted WHERE Spotted.cita = (SELECT id_pes FROM Pessoa WHERE nome = "+nome+")")
    return cursor.fetchall()

# implementacao de Fenótipos de uma pessoa
def getFenotipo(nome, cursor):
    cursor.execute("SELECT Resultado.nome, Fenotipo.categoria FROM Fenotipo NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = "+nome+"))) AS Resultado")
    return cursor.fetchall()

# implementacao de Local que uma pessoa que recebeu o spotted estava
def getLocal(nome, cursor):
    cursor.execute("SELECT Resultado.nome AS 'nome', 'Local'.evento AS 'evento' FROM 'Local' NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = "+nome+"))) AS Resultado")
    return cursor.fetchall()

# implementacao de Locais mais comuns


# implementacao de Quais fenótipos mais comuns

# implementacao de Curso de uma pessoa
