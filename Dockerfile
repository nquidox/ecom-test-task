FROM python:3.12-slim

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HOST=0.0.0.0
ENV PORT=9000

EXPOSE 9000

CMD ["python", "main.py"]