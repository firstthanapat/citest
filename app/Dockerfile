# ใช้ Python 3.9 เป็น base image
FROM python:3.9

# ตั้งค่าที่ทำงานเป็น /app
WORKDIR /app

# คัดลอกไฟล์ที่จำเป็นเข้าไป
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดเข้าไป
COPY . .

# รัน Flask
CMD ["python", "app.py"]

