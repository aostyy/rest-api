Należy:
1) Zainstalować api w konsoli visual studio komendą: pip install fastapi uvicorn requests
2) Otworzyć drugą konsolę i wpisać następująco:
3) W pierwszej: python -m uvicorn product_service:app --host 127.0.0.1 --port 8001 --reload
4) W drugiej: python -m uvicorn stock_service:app --host 127.0.0.1 --port 8002 --reload
5) Przetestować działanie komendami:
6) curl.exe -i http://127.0.0.1:8002/stock/1    (Istniejący produkt)
7) curl.exe -i http://127.0.0.1:8002/stock/999  (Nieistniejący produkt - błąd)
