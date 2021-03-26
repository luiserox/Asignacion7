FROM python:latest

RUN pip install requests

CMD ["python","/tmp/asignacion7.py"]