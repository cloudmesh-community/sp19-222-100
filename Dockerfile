FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN git clone https://github.com/cloudmesh-community/sp19-222-100.git

COPY

RUN pip install -r requirments.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]

