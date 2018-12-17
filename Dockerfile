FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
COPY startup.sh /code/
RUN chmod +x /code/startup.sh

RUN pip install -r requirements.txt 
EXPOSE 8000
CMD ["/code/startup.sh"]
