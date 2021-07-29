FROM python:3.7

# Install dependencies
RUN apt-get update --fix-missing && \
apt-get install -y dos2unix

# copy all files to a working directory
# Project Files and Settings
ARG PROJECT=demo
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
COPY . /var/www/
WORKDIR $PROJECT_DIR

# install upgrade pip and Django 2.2
RUN pip install --upgrade pip
RUN pip install django=='2.2.*'

# Server Directives
EXPOSE 8080
STOPSIGNAL SIGINT
RUN dos2unix /var/www/entrypoint.sh
RUN chmod +x /var/www/entrypoint.sh
ENTRYPOINT ["/var/www/entrypoint.sh"]
