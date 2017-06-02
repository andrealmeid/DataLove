## Consultas

- Spotteds recebido por uma pessoa Fulano
``` sql
SELECT texto FROM Spotted WHERE Spotted.cita = (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano');
SELECT Spotted.texto FROM Spotted JOIN Pessoa ON Spotted.cita = Pessoa.id_pes AND Pessoa.nome = 'Fulano';
```

- Fenótipos de uma pessoa
``` sql
SELECT Resultado.nome, Fenotipo.categoria FROM Fenotipo NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = 'Fulano'))) AS Resultado;
```

- Locais que uma pessoa que recebeu spotteds estava    
``` sql
SELECT Resultado.nome AS "nome", "Local".evento AS "evento" FROM "Local" NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = 'Fulano'))) AS Resultado;
```

- Local mais comum
``` sql
SELECT Tag.nome, "Local".evento, Tag.quantidade FROM Tag NATURAL JOIN "Local" ORDER BY Tag.quantidade DESC LIMIT 1;
```

- Quais fenótipos mais comuns
``` sql
SELECT Tag.nome, Fenotipo.categoria, Tag.quantidade FROM Tag NATURAL JOIN Fenotipo ORDER BY Tag.quantidade DESC;
```

- Curso de uma pessoa
``` sql
SELECT Resultado.nome, Curso.instituto FROM Curso NATURAL JOIN (SELECT * FROM Tag NATURAL JOIN (SELECT Descrita.id_tag FROM Descrita NATURAL JOIN (SELECT * FROM Pessoa WHERE nome = 'Fulano'))) AS Resultado;
```

- Todas as pessoas que reagiram a um spotted e o horario em que isso aconteceu
``` sql
SELECT Pessoa.nome, tipo as "reação", Resultado.horario FROM Pessoa NATURAL JOIN (SELECT * FROM Reage NATURAL JOIN (SELECT * FROM Spotted WHERE id_spot = <id>)) AS Resultado;
```

- Os três spotteds mais recentes
``` sql
SELECT * FROM Spotted ORDER BY "horário" DESC LIMIT 3;
```

- Todos os spotteds que uma pessoa reagiu
``` sql
SELECT texto, tipo as "reação" FROM Spotted NATURAL JOIN (SELECT * FROM Reage NATURAL JOIN (SELECT * FROM Pessoa WHERE nome = "Fulano"));
```

- Todos os comentários que uma pessoa fez (e seus respectivos spotteds de origem)
``` sql
SELECT Spotted.texto, Resultado.texto FROM Spotted JOIN (SELECT texto, id_spot FROM Comentario JOIN (SELECT * FROM Pessoa WHERE Pessoa.nome = 'Italove') ON id_pes = autor) AS Resultado ON Resultado.id_spot = Spotted.id_spot;
```

- Todos os spotteds anônimos
``` sql
SELECT * FROM Spotted WHERE autor IS NULL;
```

- Todos os spotteds escritos por uma pessoa Fulano
``` sql
SELECT * FROM Spotted JOIN (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano') ON id_pes = autor;
```
