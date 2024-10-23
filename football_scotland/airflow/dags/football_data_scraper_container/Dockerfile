#!/usr/bin/env python
FROM python:3.10.14-bullseye

WORKDIR /app

RUN mkdir csv

# Copy your Python script into the container
COPY . .
# Install dependencies
RUN pip install -r requirements.txt



# Command to run the script
CMD ["python", "football_data_scraper.py"]
