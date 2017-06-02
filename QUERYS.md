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

- Comentários que uma pessoa fez
``` sql
SELECT Resultado.nome, Spotted.texto, Resultado.texto FROM Spotted NATURAL JOIN (SELECT * FROM Comentario NATURAL JOIN (SELECT * FROM Pessoa Where Pessoa.nome = 'Fulano'))) AS Resultado;
```
