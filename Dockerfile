# Użyj obrazu bazowego pythona 3.8.10
FROM python:3.8.10

# Ustaw katalog roboczy na /app
WORKDIR /app

# Skopiuj plik requirements.txt do katalogu roboczego
COPY requirements.txt .

# Zainstaluj zależności z pliku requirements.txt
RUN pip install -r requirements.txt

# Skopiuj pozostałe pliki projektu
COPY . .

# Uruchom serwer Django na porcie 8000
CMD ["python", "app.py"]
