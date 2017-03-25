FROM python:latest

MAINTAINER huliqun "huliquns@126.com"

#RUN apt-get install -y python3-numpy
#RUN apt-get install -y python3-scipy
#RUN apt-get install -y python3-matplotlib
RUN pip3 install --no-cache-dir falcon #-i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install --no-cache-dir cython #-i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install --no-binary :all: falcon

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt #-i https://pypi.tuna.tsinghua.edu.cn/simple

#ENTRYPOINT [gunicorn]
