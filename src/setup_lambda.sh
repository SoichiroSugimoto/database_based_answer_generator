#! /bin/bash

# remove
touch database_based_answer_generator.zip
rm database_based_answer_generator.zip
cd database_based_answer_generator

# compress
zip -r ../database_based_answer_generator.zip ./*
cd ..

if [ ! -f ./lambda_layer.zip ]; then
  mkdir python
  pip install -t ./python numpy --upgrade
  pip install -t ./python requests
  pip install -t ./python pynamodb
  pip install -t ./python openai
  pip install -t ./python mecab-python3
  pip install -t ./python unidic-lite
  zip -r ./lambda_layer.zip ./python
fi
