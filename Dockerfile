# 1. Python image
FROM python:3.10-slim

# 2. Ishchi katalog
WORKDIR /app

# 3. Fayllarni konteynerga nusxalash
COPY . .

# 4. Zaruriy kutubxonalarni o'rnatish
RUN pip install --no-cache-dir -r requirements.txt

# 5. Flask uchun port
EXPOSE 8080

# 6. Botni ishga tushirish
CMD ["python", "bot.py"]
