# base image
FROM tensorflow/tensorflow:latest

# copy requirements 
ADD requirements.txt .

# install
RUN pip install -r requirements.txt
