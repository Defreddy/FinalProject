FROM python:3.10.0-slim
RUN python -m pip install -q --upgrade pip setuptools wheel python-multipart
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./project /code
RUN mkdir -p ./Website
COPY ./Website/login.html ./Website
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8051"]