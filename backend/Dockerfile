FROM python:3.6

ARG project_dir=/app/

ADD requirements.txt $project_dir
ADD api.py $projectdir

WORKDIR ${project_dir}

RUN pip install flask
RUN pip install -r requirements.txt

CMD ["python","api.py"]
