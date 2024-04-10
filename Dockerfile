# Use an official Python runtime as a parent image
FROM python:3.10
# Set the working directory in the container to /openai-proxy
WORKDIR /reverse-proxy
# Add the current directory contents into the container at /openai-proxy
COPY . .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Run the application when the container launches
EXPOSE 7065

CMD sh -c 'gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:7065 app:app'