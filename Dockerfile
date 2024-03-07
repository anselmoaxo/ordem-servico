# Use uma imagem específica do Python e especifique a versão
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os requisitos do projeto e instala as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código fonte para o diretório de trabalho
COPY . /app/

# Expor a porta que a aplicação estará escutando
EXPOSE 8000

# Comando para iniciar o aplicativo Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
