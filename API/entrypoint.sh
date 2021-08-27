cd /app/API
uvicorn main:app --host 0.0.0.0 --port 8000 &
cd /app/Client
npm start --port 5000 --host 0.0.0.0
