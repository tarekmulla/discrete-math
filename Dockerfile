# Use Specific-Version \ Small-Sized \ Official Docker image
FROM python:3.9-alpine

RUN pip install --upgrade pip

# Create a new user to run the app as non-root user
RUN adduser -D webapp-usr
USER webapp-usr
WORKDIR /home/webapp-usr

RUN pip install --user pipenv
ENV PATH="/home/webapp-usr/.local/bin:${PATH}"

COPY --chown=webapp-usr:webapp-usr requirements.txt .
RUN pip install --user -r requirements.txt

# Copy the files and set the owner as the new user
COPY --chown=webapp-usr:webapp-usr ./webapp ./app

EXPOSE 80

CMD ["python", "app/run.py"]
