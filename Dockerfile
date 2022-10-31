FROM python:3.9.13-slim-bullseye

ARG APP_NAME
ARG DEPLOYMENT_USER=beyonce
ARG WORK_DIR=/project

LABEL app=${APP_NAME}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR ${WORK_DIR}

RUN addgroup --system ${DEPLOYMENT_USER} \
    && adduser --system --disabled-password --disabled-login --gecos "" --group ${DEPLOYMENT_USER} \
    && chown -R ${DEPLOYMENT_USER} ${WORK_DIR}

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt 

COPY --chown=${DEPLOYMENT_USER}:${DEPLOYMENT_USER} . .

USER ${DEPLOYMENT_USER}

EXPOSE 8000
