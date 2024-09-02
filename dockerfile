FROM python:3.9.19-slim

COPY . .

RUN pip install -r requirements.txt


ENTRYPOINT ["python","main.py"]