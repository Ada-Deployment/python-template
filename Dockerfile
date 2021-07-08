FROM python:3.7
WORKDIR /code
ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . /code
CMD ["flask", "run"]