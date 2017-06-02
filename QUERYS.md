## Consultas

- Spotteds recebido por uma pessoa Fulano
``` sql
SELECT Spotted.texto FROM Spotted WHERE Spotted.cita = (SELECT id_pes FROM Pessoa WHERE nome = ‘Fulano’)
```

- Fenótipos de uma pessoa
``` sql
SELECT nome, categoria FROM Fenotipo WHERE nome IN (SELECT nome FROM Descrita WHERE id_pes = (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano'));
```

- Locais que uma pessoa que recebeu spotteds estava    
``` sql
SELECT nome, evento FROM "Local" WHERE nome IN (SELECT nome FROM Descrita WHERE id_pes IN (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano'));
```

- Locais mais comuns
``` sql
SELECT Tag.nome, "Local".evento, Tag.quantidade FROM Tag, "Local" WHERE Tag.nome = "Local".nome ORDER BY Tag.quantidade DESC LIMIT 1;
```

- Quais fenótipos mais comuns
``` sql
SELECT Fenotipo.nome, Fenotipo.categoria, Tag.quantidade FROM Tag, Fenotipo WHERE Tag.nome = Fenotipo.nome ORDER BY Tag.quantidade DESC;
```

- Curso de uma pessoa
``` sql
SELECT Curso.nome, Curso.instituto FROM Curso WHERE nome IN (SELECT nome FROM Descrita WHERE id_pes IN (SELECT id_pes FROM Pessoa WHERE nome = 'Fulano'));
```
