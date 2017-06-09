
def inserePessoa(cursor, nome, idade):
    if idade == "":
        cursor.execute("INSERT INTO Pessoa (nome) VALUES ('"+nome+"')")
    else:
        cursor.execute("INSERT INTO Pessoa (nome, idade) VALUES ('"+nome+"',"+str(idade)+")")

def insereSpotted(cursor, texto, horario, cita, autor):
    if cita == "" and autor == "":
        cursor.execute("INSERT INTO Spotted (texto, horário) VALUES ('"+texto+"','"+horario+"')")
    elif cita == "":
        cursor.execute("INSERT INTO Spotted (texto, horário, autor) VALUES ('"+texto+"','"+horario+"',"+str(autor)+")")
    elif autor == "":
        cursor.execute("INSERT INTO Spotted (texto, horário, cita) VALUES ('"+texto+"','"+horario+"',"+str(cita)+")")
    else:
        cursor.execute("INSERT INTO Spotted (texto, horário, cita, autor) VALUES ('"+texto+"','"+horario+"',"+str(cita)+","+str(autor)+")")

