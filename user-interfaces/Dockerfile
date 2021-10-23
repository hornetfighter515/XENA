FROM alpine:latest

RUN apk update && \
    apk add yarn
COPY xena-service-face /xena-service-face/

RUN (cd /xena-service-face; yarn;)
EXPOSE 3000 3000
ENTRYPOINT ["sh", "xena-service-face/entrypoint.sh"]

#docker run -p 3000:3000 -d CONTAINERID