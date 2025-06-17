#!/usr/bin/env python3
"""
Script para iniciar o servidor - Execute este arquivo para testar a aplicação
"""

import os
import sys
import webbrowser
from app_handler import run_redirect_server
from threading import Thread
import time

def main():
    print("Inicializando aplicação de Métodos Numéricos...")
    print("=" * 50)
    
    # Inicia o servidor em uma thread separada
    server_thread = Thread(target=lambda: run_redirect_server(port=8000))
    server_thread.daemon = True
    server_thread.start()
    
    # Aguarda um pouco para o servidor iniciar
    time.sleep(1)
    
    print("Servidor iniciado em http://localhost:8000")
    print("Abrindo navegador...")
    
    # Abre o navegador
    webbrowser.open("http://localhost:8000")
    
    print("\nComandos disponíveis:")
    print("- Digite 'open' para abrir o navegador novamente")
    print("- Digite 'exit' para sair")
    print("=" * 50)
    
    # Loop principal
    try:
        while True:
            command = input("Digite um comando: ").strip().lower()
            if command == 'exit':
                break
            elif command == 'open':
                webbrowser.open("http://localhost:8000")
                print("Navegador aberto!")
            else:
                print("Comando não reconhecido. Use 'open' ou 'exit'")
    except KeyboardInterrupt:
        pass
    
    print("\nEncerrando aplicação...")

if __name__ == "__main__":
    main()
