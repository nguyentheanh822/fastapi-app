# Sử dụng image Python 3.9 slim làm base image
FROM python:3.9-slim

# Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# Sao chép tất cả các file trong thư mục hiện tại vào thư mục làm việc trong container
COPY . /app

# Cài đặt các thư viện yêu cầu (FastAPI và Uvicorn)
RUN pip install fastapi uvicorn

# Chạy ứng dụng FastAPI bằng Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
