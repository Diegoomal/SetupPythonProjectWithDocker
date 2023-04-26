# Usa uma imagem do Python como base
FROM python:3.10-alpine

# Define o diretório de trabalho do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório /app do contêiner
COPY app/requirements.txt .

# Instala as dependências do Python especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do diretório src/app para o diretório /app do contêiner
COPY app/ .

# Executa o comando padrão do contêiner (neste caso, executa o arquivo __init__.py)
CMD ["python", "__init__.py"]