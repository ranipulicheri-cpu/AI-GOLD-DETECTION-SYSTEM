FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install gradio openai requests

EXPOSE 7860

CMD ["python", "app.py"]
