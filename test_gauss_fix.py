#!/usr/bin/env python3
"""
Script de teste para verificar o funcionamento das rotas
"""

import webbrowser
import time
from threading import Thread
from app_handler import run_redirect_server

def test_server():
    """Testa o servidor"""
    print("Iniciando servidor de teste...")
    
    # Inicia o servidor em uma thread separada
    server_thread = Thread(target=lambda: run_redirect_server(port=8000))
    server_thread.daemon = True
    server_thread.start()
    
    # Aguarda um pouco para o servidor iniciar
    time.sleep(2)
    
    print("Servidor iniciado!")
    print("Testando URLs:")
    print("- Página principal: http://localhost:8000/")
    print("- NumericCalculator: http://localhost:8000/numeric_calculator")
    print("- GaussElimination: http://localhost:8000/gauss_elimination")
    print("- GaussWeb: http://localhost:8000/gauss_web")
    
    # Abre o navegador
    webbrowser.open("http://localhost:8000/")
    
    try:
        while True:
            comando = input("\nDigite 'exit' para sair ou 'test' para testar gauss: ").strip().lower()
            if comando == 'exit':
                break
            elif comando == 'test':
                webbrowser.open("http://localhost:8000/gauss_elimination")
            elif comando == 'web':
                webbrowser.open("http://localhost:8000/gauss_web")
    except KeyboardInterrupt:
        pass
    
    print("Encerrando...")

if __name__ == "__main__":
    test_server()
