## Consultas

- Spotteds recebido por uma pessoa Fulano
``` sql
SELECT Spotted.texto FROM Spotted WHERE Spotted.cita = (SELECT id_pes FROM Pessoa WHERE nome = ‘Fulano’)
```

- Fenótipos de uma pessoa
``` sql
SELECT categoria FROM Fenotipo WHERE nome = (SELECT nome FROM Pessoa WHERE nome = ‘Fulano')
```

- Local que uma pessoa que recebeu o spotted estava    

- Locais mais comuns

- Quais fenótipos mais comuns

- Curso de uma pessoa
