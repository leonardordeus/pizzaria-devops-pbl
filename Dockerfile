# 1. Escolhe a imagem base do Python
FROM python:3.9-slim

# 2. Define a pasta de trabalho dentro do container
WORKDIR /app

# 3. Copia a lista de dependências e instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copia o resto do código do projeto
COPY . .

# 5. Informa a porta que a aplicação usa
EXPOSE 8080

# 6. Comando para ligar a aplicação
CMD ["python", "app.py"]