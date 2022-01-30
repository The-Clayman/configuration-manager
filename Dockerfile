FROM python:3.8-slim-buster

MAINTAINER The-Clayman https://github.com/The-Clayman

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# build commands
# docker build -t configuration-manager:v1 .

# run command
# docker run -d --name configuraion-manager -p 5000:5000 configuration-manager:v1

