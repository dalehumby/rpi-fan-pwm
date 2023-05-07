FROM python:3.8-alpine

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD [ "python", "./fan.py" ]
