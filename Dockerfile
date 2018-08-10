FROM python:3.6-slim-stretch
COPY . /project
WORKDIR /project
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD ["python3", "app/app.py"]
