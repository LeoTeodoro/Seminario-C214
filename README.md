# Seminario-C214
Repositório para a apresentação do seminário de C214

# Comando para a instalação das dependências com pipenv
- pip install pipenv
- pipenv install

# Instale o coverage
- pipenv install coverage

# Execute seus scripts ou testes como de costume. Por exemplo, para executar testes com unittest:
- python -m unittest discover tests

# Para medir a cobertura de código e gerar relatórios, use os seguintes comandos:
- coverage html

# Pipfile e Pipfile.lock
    Pipfile: Este arquivo lista as dependências do projeto e é usado pelo pipenv para gerenciá-las
    Pipfile.lock: Este arquivo é gerado pelo pipenv e contém uma versão bloqueada das dependências, garantindo que a instalação seja a mesma em qualquer máquina