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
