# Use Specific-Version \ Small-Sized \ Official Docker image
FROM python:3.9-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./webapp ./app

# Create user and group
RUN groupadd -r webapp-grp && useradd -g webapp-usr webapp-grp

# Change the owner of the webapp folder to the new user
USER chown -R webapp-usr:webapp-grp /app

EXPOSE 80

WORKDIR /app

USER webapp-usr

CMD ["python", "run.py"]
