# Use Specific-Version \ Small-Sized \ Official Docker image
FROM python:3.9-alpine

RUN pip install --upgrade pip

# Create a new user to run the app as non-root user
RUN adduser -D webapp-usr
USER webapp-usr

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the files and set the owner as the new user
COPY --chown=webapp-usr:webapp-usr ./webapp ./app

EXPOSE 80

WORKDIR /app

CMD ["python", "run.py"]
