#setup server

#1: start docker kernal + python
FROM python:3.12.4-slim

#2: ENV : show logs
ENV PYTHONUNBUFFERED=1


# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

    

#4: create project folder : kernal
WORKDIR /app

#5: cOPY REQUIRS
COPY requirement.txt /app/requirement.txt

#6: install dep
RUN pip install -r /app/requirement.txt

#7: Copy project code --->docker
COPY . /app/

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]