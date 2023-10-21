#
# link: https://www.run.ai/guides/tensorflow/tensorflow-with-docker
#

FROM tensorflow/tensorflow:latest-gpu

COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY app/ .
CMD [ "python3", "main.py" ]