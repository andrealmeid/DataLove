## Consultas

- Spotteds recebido por uma pessoa Fulano
``` sql
SELECT texto FROM Spotted WHERE Spotted.cita = (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano');
SELECT Spotted.texto FROM Spotted JOIN Pessoa ON Spotted.cita = Pessoa.id_pes AND Pessoa.nome = 'Fulano';
```

- Fenótipos de uma pessoa
``` sql
SELECT nome, categoria FROM Fenotipo WHERE nome IN (SELECT nome FROM Descrita WHERE id_pes = (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano'));
SELECT Fenotipo.nome, Fenotipo.categoria FROM Fenotipo JOIN (SELECT Descrita.nome FROM Descrita JOIN Pessoa ON Descrita.id_pes = Pessoa.id_pes AND Pessoa.nome = 'Fulano') AS Resultado ON Fenotipo.nome = Resultado.nome;
```

- Locais que uma pessoa que recebeu spotteds estava    
``` sql
SELECT nome, evento FROM "Local" WHERE nome IN (SELECT nome FROM Descrita WHERE id_pes IN (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano'));
SELECT "Local".nome AS "nome", "Local".evento AS "evento" FROM "Local" JOIN (SELECT Descrita.nome FROM Descrita JOIN Pessoa ON Descrita.id_pes = Pessoa.id_pes AND Pessoa.nome = 'Fulano') AS Resultado ON "Local".nome = Resultado.nome;
```

- Local mais comum
``` sql
SELECT Tag.nome, "Local".evento, Tag.quantidade FROM Tag JOIN "Local" ON Tag.nome = "Local".nome ORDER BY Tag.quantidade DESC LIMIT 1;
```

- Quais fenótipos mais comuns
``` sql
SELECT Fenotipo.nome, Fenotipo.categoria, Tag.quantidade FROM Tag JOIN Fenotipo ON Tag.nome = Fenotipo.nome ORDER BY Tag.quantidade DESC;
```

- Curso de uma pessoa
``` sql
SELECT Curso.nome, Curso.instituto FROM Curso WHERE nome IN (SELECT nome FROM Descrita WHERE id_pes IN (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano'));
SELECT Fenotipo.nome, Fenotipo.categoria FROM Fenotipo JOIN (SELECT Descrita.nome FROM Pessoa JOIN Descrita ON Pessoa.id_pes = Descrita.id_pes AND Pessoa.nome = 'Fulano') AS Resultado ON Fenotipo.nome = Resultado.nome;
```
