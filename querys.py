# bibliteca com as consultas implementadas

def getAllSpotteds(cursor):
    cursor.execute("SELECT * FROM Spotted;")
    return cursor.fetchall()

def getAllComentarios(cursor):
    cursor.execute("SELECT * FROM Comentario;")
    return cursor.fetchall()

def getAllTags(cursor):
    cursor.execute("SELECT * FROM Tag;")
    return cursor.fetchall()

def getAllPessoas(cursor):
    cursor.execute("SELECT * FROM Pessoa;")
    return cursor.fetchall()

# implementacao de Spotteds recebido por uma pessoa
def getSpottedRecebido(nome, cursor):
    cursor.execute("SELECT Spotted.texto FROM Spotted WHERE Spotted.cita = (SELECT id_pes FROM Pessoa WHERE nome = '"+nome+"')")
    return cursor.fetchall()

# implementacao de Fenótipos de uma pessoa
def getFenotipo(nome, cursor):
    cursor.execute("SELECT Resultado.nome, Fenotipo.categoria FROM Fenotipo NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = '"+nome+"'))) AS Resultado")
    return cursor.fetchall()

# implementacao de Local que uma pessoa que recebeu o spotted estava
def getLocal(nome, cursor):
    cursor.execute("SELECT Resultado.nome AS 'nome', 'Local'.evento AS 'evento' FROM 'Local' NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = '"+nome+"'))) AS Resultado")
    return cursor.fetchall()

# implementacao de Locais mais comuns
def getLocalMaisComum(cursor):
    cursor.execute("SELECT Tag.nome, 'Local'.evento, Tag.quantidade FROM Tag NATURAL JOIN 'Local' ORDER BY Tag.quantidade DESC LIMIT 1;")
    return cursor.fetchone()

# implementacao de Quais fenótipos mais comuns
def getFenotipoMaisComum(cursor):
    cursor.execute("SELECT Tag.nome, Fenotipo.categoria, Tag.quantidade FROM Tag NATURAL JOIN Fenotipo ORDER BY Tag.quantidade DESC;")
    return cursor.fetchone()

# implementacao de Curso de uma pessoa
def getCurso(nome, cursor):
    cursor.execute("SELECT Resultado.nome, Curso.instituto FROM Curso NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE nome = '"+nome+"'))) AS Resultado;")
    return cursor.fetchall()

# implementacao de Todas as pessoas que reagiram a um spotted e o horario em que isso aconteceu
def getReacaoSpotted(spotted, cursor):
    cursor.execute("SELECT Pessoa.nome, tipo as 'reação', Resultado.horario FROM Pessoa NATURAL JOIN (SELECT * FROM Reage NATURAL JOIN (SELECT * FROM Spotted WHERE id_spot = "+spotted+")) AS Resultado;")
    return cursor.fetchall()

# implementacao de Os tres spotteds mais recentes
def getSpottedsRecentes(cursor):
    cursor.execute("SELECT * FROM Spotted ORDER BY spotted.'horário' DESC LIMIT 3;")
    return cursor.fetchall()

# implementacao de Todos os spotteds que uma pessoa reagiu
def getReacaoPessoa(nome, cursor):
    cursor.execute("SELECT texto, tipo as 'reação' FROM Spotted NATURAL JOIN (SELECT * FROM Reage NATURAL JOIN (SELECT * FROM Pessoa WHERE nome = '"+nome+"'));")
    return cursor.fetchall()

# implementacao de Todos os comentários que uma pessoa fez (e seus respectivos spotteds de origem)
def getComentarios(nome, cursor):
    cursor.execute("SELECT Spotted.texto, Resultado.texto FROM Spotted JOIN (SELECT texto, id_spot FROM Comentario JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = '"+nome+"') ON id_pes = autor) AS Resultado ON Resultado.id_spot = Spotted.id_spot;")
    return cursor.fetchall()

# implementacao de Todos os spotteds anônimos
def getSpottedAnonimo(cursor):
    cursor.execute("SELECT * FROM Spotted WHERE autor IS NULL;")
    return cursor.fetchall()

# implementacao de Todos os spotteds escritos por uma pessoa
def getSpottedEscrito(nome, cursor):
    cursor.execute("SELECT * FROM Spotted JOIN (SELECT id_pes FROM Pessoa WHERE nome = '"+nome+"') ON id_pes = autor;")
    return cursor.fetchall()
