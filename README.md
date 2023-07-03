# Minha CPU RISC de 4 bits
Este é um projeto de uma CPU RISC (Reduced Instruction Set Computer) de 4 bits que eu desenvolvi. A CPU foi projetada com o objetivo de fornecer um conjunto mínimo de instruções para realizar operações simples em dados de 4 bits.

# Arquitetura
A CPU RISC de 4 bits possui as seguintes características:

Arquitetura RISC simplificada com um conjunto limitado de instruções.
Barramento de dados de 4 bits para manipulação de dados.
Barramento de endereço de 4 bits para acessar a memória.
Registradores de uso geral de 4 bits para armazenar valores intermediários e resultados.
Conjunto de Instruções
# O conjunto de instruções da CPU RISC de 4 bits inclui as seguintes operações básicas:

ADD: Adiciona dois valores e armazena o resultado no registrador de destino.  
SUB: Subtrai dois valores e armazena o resultado no registrador de destino.  
AND: Realiza a operação lógica "AND" entre dois valores e armazena o resultado no registrador de destino.  
OR: Realiza a operação lógica "OR" entre dois valores e armazena o resultado no registrador de destino.  
LOAD: Carrega um valor da memória para um registrador.  
STORE: Armazena um valor de um registrador na memória.  
JUMP: Salta para um endereço específico na memória.  
BRANCH: Realiza um salto condicional com base em uma condição específica.  
MOVE: Move um valor de um registrador para outro registrador.  
NOT: Inverte os bits de um valor e armazena o resultado no registrador de destino.  
SHIFT: Realiza uma operação de deslocamento (shift) à esquerda ou à direita em um valor e armazena o resultado no registrador de destino.  

# Utilização com o Logisim
Este projeto pode ser aberto e explorado utilizando o software Logisim. O arquivo principal do projeto contém o circuito digital da CPU, incluindo todos os componentes e conexões necessárias para o funcionamento correto da CPU RISC de 4 bits.

# Assembly para Python
Faço um [código](https://github.com/IgorPeli/Logisim/blob/main/main.py) em python onde você pode converter uma instrução em Assembly para hexadecimal e para binário.  
MOVE 0, 0 é como se fosse MOVE  
MOVE 0, 1 é como se fosse MOVE(X)

# Assembly -> Linguagem de Máquina
Também compilo um código Assembly para uma instrução de linguagem de máquina.  
Onde opero os seguintes [comandos](https://github.com/MarceloCamponez/CPU_LOGISIM/blob/main/MPU_RISC_4BITS.pdf).

# Tabela de Conversão Assembly -> Binário -> Hexadecimal

| ASSEMBLY    | BINARY     | HEX |
| ----------- | ---------- | --- |
| MOVE 0, 1   | 00010000   | 10  |
| ADD A, 1    | 00110000   | 3a  |
| SUB 9, 1    | 01011000   | 59  |
| OR A, 1     | 01111010   | 7a  |
| XOR 1, 1    | 10010001   | 91  |
| SHIFT 9, 1  | 10111001   | b9  |
| JMP 9, 0    | 11001000   | c9  |
| GO 9, 0     | 11011000   | ea  |
| STR F, 0    | 11011000   | ff  |




