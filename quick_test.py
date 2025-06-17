#!/usr/bin/env python3
"""
Teste rápido do funcionamento das rotas
"""

import requests
import time
from threading import Thread
from app_handler import run_redirect_server

def test_routes():
    """Testa se as rotas estão funcionando"""
    
    # Inicia o servidor
    server_thread = Thread(target=lambda: run_redirect_server(port=8001))
    server_thread.daemon = True
    server_thread.start()
    
    # Aguarda o servidor iniciar
    time.sleep(2)
    
    base_url = "http://localhost:8001"
    
    print("Testando rotas...")
    
    # Testa página principal
    try:
        response = requests.get(f"{base_url}/")
        print(f"Página principal: {response.status_code}")
    except Exception as e:
        print(f"Erro na página principal: {e}")
    
    # Testa rota gauss_elimination
    try:
        response = requests.get(f"{base_url}/gauss_elimination")
        print(f"Gauss elimination: {response.status_code}")
        if response.status_code == 200:
            print("✅ Rota gauss_elimination funcionando!")
        else:
            print("❌ Problema na rota gauss_elimination")
    except Exception as e:
        print(f"Erro em gauss_elimination: {e}")
    
    # Testa rota numeric_calculator
    try:
        response = requests.get(f"{base_url}/numeric_calculator")
        print(f"Numeric calculator: {response.status_code}")
    except Exception as e:
        print(f"Erro em numeric_calculator: {e}")

if __name__ == "__main__":
    test_routes()
