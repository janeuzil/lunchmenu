FROM python:2-alpine
EXPOSE 8081

# Install basic utilities
RUN apk add -U ca-certificates --update --no-cache g++ gcc libxslt-dev \
  && rm -rf /var/cache/apk/* \
  && pip install --no-cache-dir \
          setuptools \
          wheel

COPY requirements.txt /app/
COPY gcp_sak.json /app/

RUN pip install -r /app/requirements.txt

WORKDIR /app
ADD lunchmenu/ /app/

CMD [ "python", "./lunchmenu.py", "8081" ]
