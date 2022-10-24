FROM python:3
RUN apt update
RUN apt install python3 -y
COPY server.py ./
EXPOSE 8888
CMD ["python3", "./server.py"]
