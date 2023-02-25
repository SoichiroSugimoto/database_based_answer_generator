FROM amazon/aws-sam-cli-build-image-python3.9
USER root

RUN apt-get install mecab mecab-ipadic-utf8 libmecab-dev swig