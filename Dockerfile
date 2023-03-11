# Use Specific-Version \ Small-Sized \ Official Docker image
FROM python:3.9-alpine

ARG UNAME=webapp-usr
ARG UID=1008
ARG GID=1008

RUN pip install --upgrade pip

# Create a new user to run the app as non-root user
RUN addgroup -g $GID $UNAME
RUN adduser -S $UNAME -u $UID -G $UNAME -H -D -s /bin/sh

COPY --chown=$UNAME:$UNAME requirements.txt .
RUN pip install -r requirements.txt

# Copy the files and set the owner as the new user
COPY --chown=$UNAME:$UNAME ./webapp ./app

WORKDIR /app

USER $UNAME

EXPOSE 8080

CMD ["python", "run.py"]
