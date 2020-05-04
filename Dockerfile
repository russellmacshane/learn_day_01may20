FROM python:3.8.2-slim
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    && pip install tox

WORKDIR /opt/learn-day
COPY . /opt/learn-day
RUN pip install -r /opt/learn-day/requirements.txt
ENTRYPOINT ["/bin/bash", "start_flask.sh"]