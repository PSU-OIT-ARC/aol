FROM python:3.7-buster


ENV PROJECT_NAME aol
ENV PROJECT_DIR /webapps/${PROJECT_NAME}
ENV STATIC_ROOT ${PROJECT_DIR}/static
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y \
  build-essential \
  binutils libgdal-dev proj-bin

RUN adduser --no-create-home --home ${PROJECT_DIR} ${PROJECT_NAME}
RUN mkdir /venv && chown ${PROJECT_NAME} /venv

COPY ./entrypoint.sh /entrypoint.sh
COPY ./entrypoint-test.sh /entrypoint-test.sh
ENTRYPOINT ["/entrypoint.sh"]
