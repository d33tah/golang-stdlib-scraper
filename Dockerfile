FROM python:3.10
ADD ./requirements.txt .
RUN python3 -m pip install -r requirements.txt
WORKDIR /tmp
ADD parse-tree.py .
ADD render.py .
ADD run.sh .
ENTRYPOINT /tmp/run.sh
