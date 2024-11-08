FROM python:3.9.16-slim-buster

WORKDIR /api

RUN pip install fastapi uvicorn
RUN pip install requests
RUN pip install jinja2
RUN pip install mysql-connector-python
RUN pip install schedule
RUN pip install openpyxl
RUN pip install python-multipart
RUN pip install reportlab

COPY . /api/
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]