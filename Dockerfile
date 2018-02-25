FROM python:3.6.1
# FROM python:3.6.1

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install Dockerize
ENV DOCKERIZE_VERSION v0.6.0

# install environment dependencies
RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends \
    openssl \
  && apt-get -q clean

RUN  wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# add requirements (to leverage Docker cache)
COPY requirements.txt ./
# install requirements
RUN pip install -U --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD python -B -u manage.py run -h 0.0.0.0