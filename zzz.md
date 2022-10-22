1 - criar o ambiente virtual
$ python3 -m venv .venv

2 - ativar o ambiente virtual
$ source .venv/bin/activate

3 - instalar as dependências no ambiente virtual
$ python3 -m pip install -r dev-requirements.txt

O arquivo dev-requirements.txt contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um package.json de um projeto Node.js.

4 - python3 -i abre o terminal interativo

5 - python3 -m <caminho a patrir da raiz> para rodar minha funçao -> com . no lugar das / para ir rodando (obs: src.jobs ex de caminho) vai mmostrar o meu print

6 - python3 -m pytest tests/test_jobs.py rodo o teste sem o terminal interativo

https://docs.python.org/pt-br/3/library/csv.html

- O read()método retorna o número especificado de bytes do arquivo. O padrão é -1, o que significa o arquivo inteiro.

- o With substitue o uso do try finally garantindo a finalizaçao.

- A open()função retorna um objeto de arquivo, que possui um read()método para leitura.

- Um CSV é um arquivo no qual os dados estão na forma de um delimitador separado por vírgula ou outro delimitador escolhido pelo usuário
  O csvmódulo implementa classes para ler e gravar dados tabulares no formato CSV.

modulo CSV - funçoes{reader, writer, register_dialect, unregister_dialect, get_dialect, list_dialects, field_size_limit DictReader } e class {DictReader, DictWriter, Dialect, excel, excel_tab, unix_dialect, Sniffer} e constante {QUOTE_ALL, QUOTE_MINIMAL, QUOTE_NONNUMERIC, QUOTE_NONE} e os dialetos possuem suporte aos seguintes atributos {delimiter, doublequote, escapechar, lineterminator, quotechar, quoting, skipinitialspace, strict}

- Método DictReader() para ler o nome da coluna específica.

- delimiter Uma string de um caractere usada para separar campos. O padrão é ','.

- quotechar Uma string de um caractere usada para citar campos contendo caracteres especiais, como delimiter ou quotechar, ou que contêm caracteres de nova linha. O padrão é '"'.

https://www.w3schools.com/python/python_for_loops.asp

- loops for

- set()retorna:
  um conjunto vazio se nenhum parâmetro for passado
  um conjunto construído a partir do parâmetro iterável fornecido
  tbm ja ordena a-z e 0-n

- list()função cria um objeto de lista. Um objeto de lista é uma coleção que é ordenada e mutável.

- != "" usado para considerar valores vazios -> != operador de diferente, "" vazio.

https://www.programiz.com/python-programming/methods/built-in/int
https://www.programiz.com/python-programming/methods/built-in/isnumeric
https://www.programiz.com/python-programming/methods/built-in/max

- O int()método converte qualquer string, objeto semelhante a bytes ou um número para inteiro e retorna.
- O isnumeric()método verifica se todos os caracteres da string são numéricos.
- A max()função retorna o maior item em um iterável. Também pode ser usado para encontrar o maior item entre dois ou mais parâmetros.
- A min()função retorna o item com o valor mais baixo ou o item com o valor mais baixo em um iterável.
- and usado para fazer conbinaçoes entre duas ou mais expreçoes boleanas
- pass é usada como um espaço reservado para código futuro. Quando a passinstrução é executada, nada acontece, mas você evita obter um erro quando o código vazio não é permitido. Código vazio não é permitido em loops, definições de função, definições de classe ou em instruções if.
