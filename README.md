
# Ciência de Dados

Este é um projeto de Ciência de Dados desenvolvido em Python, utilizando bibliotecas como `pandas` e `matplotlib` para análise e visualização de dados.

## Configuração do Ambiente

Para garantir que todas as dependências sejam instaladas corretamente e evitar conflitos com outras bibliotecas, é recomendado criar um ambiente virtual antes de instalar as dependências.

### Criar e Ativar o Ambiente Virtual

#### Linux/MacOS
1. Crie o ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

2. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

#### Windows
1. Crie o ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```

### Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Executando o Projeto

Após configurar o ambiente e instalar as dependências, você pode executar os scripts do projeto com o seguinte comando:

```bash
python main.py
```

## Estrutura do Projeto

- **dataset/**: Contém os arquivos de dados utilizados no projeto.
- **graphics/**: Diretório para salvar os gráficos gerados (certifique-se de que este diretório está incluído no `.gitignore`).
- **venv/**: Ambiente virtual (ignorando pelo Git).
- **main.py**: Arquivo principal para execução do projeto.
- **utils.py**: Contém funções auxiliares para manipulação de dados.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas antes de executar o projeto.

---
