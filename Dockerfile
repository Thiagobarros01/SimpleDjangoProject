# Imagem base do Python
FROM python:3.12

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Arquivo requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Expõe a porta que o Django usa
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
