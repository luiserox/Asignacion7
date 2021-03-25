FROM python:latest

RUN pip install requests

COPY "asignacion7.py" .

CMD ["python","asignacion7.py"]