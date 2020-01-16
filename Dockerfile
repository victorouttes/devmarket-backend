FROM python:3.7
RUN apt-get update && apt-get install libsasl2-dev python3-dev libldap2-dev libpq-dev libssl-dev -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=pt_BR.UTF-8
ENV LANG pt_BR.UTF-8

RUN mkdir -p /home/appl
ENV APP_HOME /home/appl/web
RUN mkdir -p ${APP_HOME}
COPY . ${APP_HOME}
WORKDIR ${APP_HOME}

RUN pip install -r requirements-production.txt

EXPOSE 8000