1 - criar o ambiente virtual
  $ python3 -m venv .venv

2 - ativar o ambiente virtual
  $ source .venv/bin/activate

3 - instalar as dependências no ambiente virtual
  $ python3 -m pip install -r dev-requirements.txt

O arquivo dev-requirements.txt contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um package.json de um projeto Node.js.