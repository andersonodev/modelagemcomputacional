#!/usr/bin/env python3
"""
Servidor de teste simples para debug
"""

import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

# Caminho raiz
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Requisição recebida: {self.path}")
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/gauss_elimination':
            print("Acessando rota /gauss_elimination")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = """
            <html>
            <body>
                <h1>Rota /gauss_elimination funcionando!</h1>
                <p>A rota está sendo reconhecida corretamente.</p>
                <a href="/">Voltar</a>
            </body>
            </html>
            """
            self.wfile.write(response.encode())
        elif parsed_path.path == '/numeric_calculator':
            print("Acessando rota /numeric_calculator")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = """
            <html>
            <body>
                <h1>Rota /numeric_calculator funcionando!</h1>
                <p>A rota está sendo reconhecida corretamente.</p>
                <a href="/">Voltar</a>
            </body>
            </html>
            """
            self.wfile.write(response.encode())
        elif parsed_path.path == '/' or parsed_path.path == '/index.html':
            print("Servindo página inicial")
            try:
                with open(os.path.join(ROOT_DIR, 'index.html'), 'r', encoding='utf-8') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode())
            except Exception as e:
                print(f"Erro ao servir index.html: {e}")
                self.send_error(500, str(e))
        else:
            print(f"Rota não encontrada: {parsed_path.path}")
            self.send_error(404, 'Página não encontrada')

def run_test_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, TestHandler)
    print("Servidor de teste rodando em http://localhost:8000")
    print("Pressione Ctrl+C para parar")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor parado")

if __name__ == "__main__":
    run_test_server()
