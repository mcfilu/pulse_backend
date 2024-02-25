# 
FROM python:3.10

# 
WORKDIR /backEnd

# 
COPY ./requirements.txt /backEnd/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /backEnd/requirements.txt

# 
COPY ./app /backEnd/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
