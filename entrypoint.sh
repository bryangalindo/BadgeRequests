cd /app/API
uvicorn main:app --host 0.0.0.0 --port 5000 &
cd /app/Client
npm start
