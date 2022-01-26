FROM python:3.9

WORKDIR /price_tracker

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "price_tracker/manage.py", "runserver", "0.0.0.0:8000"]
