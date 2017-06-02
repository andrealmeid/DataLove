# DataLove
_An amazing database to store love_

                                oo                                        
                                  oo                                        
                                   oo     OOOOOOOO:       OOOOOOOO!       
                                      oOOOO!!!!;;;;O    OO.......:;!O     
                                     'OOO!!!;;;;;;;;O  O.......:   ;!O    
                                     OOO!!!!;;::::::.OO........:    ;!O   
                                     OO!!!!;;:::::..............:   ;!O   
                                     OOO!!!;::::::..............:   ;!O   
                                      OO!!;;::::::.............:   ;!O    
                                       OO!;;::::::......oo.....::::!O     
                                         O!!;::::::........oo..:::O       
                                           !!!;:::::..........ooO         
                                              !!;:::::.......O   oo       
                                                ;;::::.....O        oo  ,o
                                                   :::..O              ooo
                                                     ::.              oooo
                                                      :                   


## Parte escrita
[Link para T3 no Google Docs](https://docs.google.com/document/d/1bWyk3xRlpup9H-jTxx2dAkVM_91c94KdML-5VZgI2u8/edit?usp=sharing) (entrega dia 02/06).

## Parte prática
__[Especificação](http://www.ic.unicamp.br/~cmbm/MC536/trab30117.pdf)__ (entrega dia 09/06).

Resumo:
-  Desenvolver o que foi prometido em [T2](https://docs.google.com/document/d/10PkkHCgRBObbstiPGx3No5o24EuxUXqwiarU6lrdD0c/edit); salvo exceções que devem ser justificadas na parte escrita;
- Fazer uma apresentação de 15 minutos, incluindo uma demostração ao vivo do software. Deve ser possível ver o código fonte das consultas e inserções.
- Usar um SGDB relacional, pode ser do Kleber ou instalado na maquina de alguem.


## Arquivos
### Python
- `datalove.py`: programa principal, com a interface para usuário realizar buscas e inserções.
- `querys.py` : biblioteca com as funções de consulta usada pelo `datalove.py`.
- `insert.py` : biblioteca com as funções de inserção usada pelo `datalove.py`.

### SQL
- `datalove.sqlite`: bando de dados com tabelas e tuplas, em formato SQLite3.
- `datalove_create.sql`: backup do script de criação de tabelas do banco.
- `database_insert.sql`: backup do script de inserção de tuplas no banco.
