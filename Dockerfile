FROM python:3.6
COPY . /app
WORKDIR /app
RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["./init.py"]
