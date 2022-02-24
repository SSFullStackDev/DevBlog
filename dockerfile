FROM python:3.9

WORKDIR /DevBlog

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "DevBlog/manage.py", "runserver", "0.0.0.0:8000"]
