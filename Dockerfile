FROM python:2-alpine
EXPOSE 8081

# Install basic utilities
RUN apk add -U ca-certificates \
  && rm -rf /var/cache/apk/* \
  && pip install --no-cache-dir \
          setuptools \
          wheel

COPY requirements.txt /app/
ENV MYSQLXPB_PROTOC=/usr/bin/protoc
ENV MYSQLXPB_PROTOBUF_INCLUDE_DIR=/usr/include/google/protobuf
ENV MYSQLXPB_PROTOBUF_LIB_DIR=/usr/lib/x86_64-linux-gnu
RUN pip install -r /app/requirements.txt

WORKDIR /app
ADD lunchmenu.py /app/

CMD [ "python", "./lunchmenu.py", "8081" ]
