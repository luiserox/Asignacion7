FROM python:latest

RUN pip install requests

WORKDIR C/Users/LuisEduardo/Documents/Tareas/"Tarea 7"/Asignacion7

COPY . .

CMD ["python","asignacion7.py"]