FROM python:3.6

ARG project_dir=/app/
WORKDIR ${project_dir}

COPY requirements.txt $project_dir


WORKDIR ${project_dir}

RUN pip install -U flask
RUN pip install -U flask_cors
RUN pip install -U PyMySQL
RUN pip install -U FLASK-SQLAlchemy
RUN pip install -r requirements.txt --no-cache-dir

COPY . $project_dir

CMD ["python","api.py"]
