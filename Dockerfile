FROM python:3.8

WORKDIR /usr/src/app

ENV TELEGRAM_API_TOKEN=""

COPY . /usr/src/app
RUN pip install poetry
RUN make install

CMD ["python", "application.py"]
