FROM python:3.9

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ,"main.py"]
