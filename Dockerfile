FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV DEBUG False

WORKDIR /app/

# Install dependencies
COPY Pipfile.lock ./
RUN pip install --upgrade pipenv \
    && pipenv requirements > requirements.txt \
    && pip install -r requirements.txt \
    && pip uninstall -y pipenv \
    && rm Pipfile.lock requirements.txt \
    && mkdir data

# Copy source files
COPY . /app/
RUN ./manage.py collectstatic

# Add user
RUN useradd user
USER user

EXPOSE 8000
ENTRYPOINT ./manage.py migrate \
            && gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 1
