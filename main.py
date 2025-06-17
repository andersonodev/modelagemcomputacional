#!/usr/bin/env python3
"""
Aplicação principal para seleção de métodos numéricos
"""

import os
import sys
import webbrowser
import subprocess
from threading import Thread
from app_handler import AppRedirectHandler
from http.server import HTTPServer

# Caminhos para os projetos
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NUMERIC_CALCULATOR_PATH = os.path.join(ROOT_DIR, 'NumericCalculator')
GAUSS_ELIMINATION_PATH = os.path.join(ROOT_DIR, 'GaussEliminationSolver')

# Porta para servir a página principal
PORT = 8000

def run_server():
    """Executa o servidor HTTP com handler customizado para redirecionamentos"""
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, AppRedirectHandler)
    print(f"Servidor principal rodando em http://localhost:{PORT}")
    httpd.serve_forever()

def main():
    """Função principal que inicia o servidor e abre o navegador"""
    # Inicia o servidor em uma thread separada
    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    
    # Abre o navegador na página principal
    print("Abrindo navegador...")
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Mantém o programa em execução
    try:
        while True:
            command = input("Digite 'exit' para sair: ")
            if command.lower() == 'exit':
                break
    except KeyboardInterrupt:
        print("\nEncerrando aplicação...")

if __name__ == "__main__":
    main()
