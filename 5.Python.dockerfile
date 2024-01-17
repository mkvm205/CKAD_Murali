FROM python:latest

LABEL version ="3.0.0"
LABEL maintainer: "mkvm2050@gmail.com"

ADD triangle.py / 
CMD ["python3", "./triangle.py"]