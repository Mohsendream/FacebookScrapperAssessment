FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /code/app
CMD ["uvicorn","Scrapper.main:app","--host","0.0.0.0","--port","80"]