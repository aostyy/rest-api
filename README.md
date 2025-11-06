Należy:
1) Zainstalować api w konsoli visual studio komendą: pip install fastapi uvicorn requests
2) Otworzyć drugą konsolę i wpisać następująco:
   W pierwszej: python -m uvicorn product_service:app --host 127.0.0.1 --port 8001 --reload
   W drugiej: python -m uvicorn stock_service:app --host 127.0.0.1 --port 8002 --reload
3) Przetestować działanie komendami:
   curl.exe -i http://127.0.0.1:8002/stock/1    (Istniejący produkt)
   curl.exe -i http://127.0.0.1:8002/stock/999  (Nieistniejący produkt - błąd)
