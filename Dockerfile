FROM python:3.6
ADD . /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
CMD python3 ./init.py
