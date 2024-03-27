# No precompiled wheel for scikit-learn beyond Python 3.9.
# Building one within Docker for Python 3.10 takes too long.
FROM python:3.9-slim

RUN apt-get update

WORKDIR /app
ADD . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

CMD ["python", "app.py"]