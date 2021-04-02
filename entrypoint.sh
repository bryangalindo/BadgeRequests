sh -c 'cd /app/API && uvicorn main:app --host 0.0.0.0 --port 8000' & jobs
sh -c 'cd /app/Client && npm start' & jobs