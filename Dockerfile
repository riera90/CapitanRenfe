FROM python:3.6
COPY . /app
WORKDIR /app
CMD python3 -m pip install -r requirements.txt && python3 ./init.py
