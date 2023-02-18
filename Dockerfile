FROM amazon/aws-sam-cli-build-image-python3.9
USER root

RUN pip install mecab-python3
