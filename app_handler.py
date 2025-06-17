#!/usr/bin/env python3
"""
Manipulador para redirecionamento entre os aplicativos
"""

import os
import sys
import subprocess
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Caminhos para os projetos
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NUMERIC_CALCULATOR_PATH = os.path.join(ROOT_DIR, 'NumericCalculator')
GAUSS_ELIMINATION_PATH = os.path.join(ROOT_DIR, 'GaussEliminationSolver')

print(f"DEBUG: ROOT_DIR = {ROOT_DIR}")
print(f"DEBUG: NUMERIC_CALCULATOR_PATH = {NUMERIC_CALCULATOR_PATH}")
print(f"DEBUG: GAUSS_ELIMINATION_PATH = {GAUSS_ELIMINATION_PATH}")

class AppRedirectHandler(BaseHTTPRequestHandler):
    """Handler que processa os redirecionamentos para os diferentes aplicativos"""
    
    def do_GET(self):
        """Processa requisições GET"""
        # Analisa a URL
        parsed_path = urlparse(self.path)
        print(f"DEBUG: Requisição recebida para: {parsed_path.path}")
        
        # Rota principal - serve o HTML da página inicial
        if parsed_path.path == '/' or parsed_path.path == '/index.html':
            print("DEBUG: Servindo página inicial")
            self._serve_file('index.html', 'text/html')
        
        # Serve o CSS
        elif parsed_path.path == '/style.css':
            print("DEBUG: Servindo CSS")
            self._serve_file('style.css', 'text/css')
            
        # Serve imagens
        elif parsed_path.path.startswith('/images/'):
            print(f"DEBUG: Servindo imagem: {parsed_path.path}")
            image_path = parsed_path.path[1:]  # Remove a barra inicial
            content_type = 'image/jpeg' if image_path.endswith('.jpg') else 'image/png'
            self._serve_file(image_path, content_type)
        
        # Redireciona para o aplicativo de Cálculo de Raízes
        elif parsed_path.path == '/numeric_calculator':
            print("DEBUG: Redirecionando para numeric_calculator")
            self._launch_numeric_calculator()
            
        # Serve arquivos estáticos do NumericCalculator
        elif parsed_path.path.startswith('/static/'):
            print(f"DEBUG: Servindo arquivo estático do NumericCalculator: {parsed_path.path}")
            file_path = parsed_path.path[1:]  # Remove a barra inicial
            self._serve_numeric_static(file_path)
            
        # Redireciona para o aplicativo de Eliminação de Gauss
        elif parsed_path.path == '/gauss_elimination':
            print("DEBUG: Redirecionando para gauss_elimination")
            # Sempre serve a versão web se disponível
            gauss_html_path = os.path.join(GAUSS_ELIMINATION_PATH, 'index.html')
            if os.path.exists(gauss_html_path):
                print("DEBUG: Servindo versão web do Gauss")
                self._serve_gauss_web()
            else:
                print("DEBUG: Lançando versão desktop do Gauss")
                self._launch_gauss_elimination()
            
        # Serve a versão web do GaussEliminationSolver
        elif parsed_path.path == '/gauss_web':
            print("DEBUG: Servindo versão web do Gauss")
            self._serve_gauss_web()
            
        # Serve arquivos estáticos do GaussEliminationSolver
        elif parsed_path.path.startswith('/gauss_static/'):
            print(f"DEBUG: Servindo arquivo estático do Gauss: {parsed_path.path}")
            file_path = parsed_path.path.replace('/gauss_static/', '')
            self._serve_gauss_static(file_path)
            
        # Rota não encontrada
        else:
            print(f"DEBUG: Rota não encontrada: {parsed_path.path}")
            self.send_error(404, 'Página não encontrada')
    
    def _serve_file(self, relative_path, content_type):
        """Serve um arquivo estático"""
        try:
            file_path = os.path.join(ROOT_DIR, relative_path)
            print(f"DEBUG: Tentando servir arquivo: {file_path}")
            
            with open(file_path, 'rb') as file:
                content = file.read()
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(content)
            print(f"DEBUG: Arquivo servido com sucesso: {file_path}")
            
        except FileNotFoundError:
            print(f"DEBUG: Arquivo não encontrado: {file_path}")
            self.send_error(404, 'Arquivo não encontrado')
        except Exception as e:
            print(f"DEBUG: Erro ao servir arquivo: {str(e)}")
            self.send_error(500, f'Erro ao servir arquivo: {str(e)}')
    
    def _launch_numeric_calculator(self):
        """Inicia o aplicativo de Cálculo de Raízes e redireciona"""
        try:
            # Envia resposta com página de carregamento 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            message = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Iniciando Aplicativo</title>
                <style>
                    body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #FFE4E6; }
                    .spinner { border: 4px solid #f3f3f3; border-top: 4px solid #FF69B4; 
                              border-radius: 50%; width: 50px; height: 50px; 
                              animation: spin 1s linear infinite; margin: 20px auto; }
                    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                    .button { display: inline-block; padding: 10px 20px; margin: 20px;
                             background-color: #FF69B4; color: white; border-radius: 25px;
                             text-decoration: none; font-weight: bold; }
                    h1 { color: #C71585; }
                </style>
                <meta http-equiv="refresh" content="2;url=http://localhost:8080">
            </head>
            <body>
                <h1>Iniciando o Calculador de Raízes...</h1>
                <div class="spinner"></div>
                <p>O aplicativo está sendo iniciado. Você será redirecionado automaticamente.</p>
                <p>Se não for redirecionado, <a href="http://localhost:8080" style="color: #FF1493;">clique aqui</a></p>
                <p><a href="/" class="button">Voltar à página principal</a></p>
            </body>
            </html>
            """
            
            self.wfile.write(message.encode())
            
            # Inicia o aplicativo em um processo separado
            subprocess.Popen([sys.executable, os.path.join(NUMERIC_CALCULATOR_PATH, 'main.py')])
            
        except Exception as e:
            self.send_error(500, f'Erro ao iniciar o aplicativo: {str(e)}')
    
    def _launch_gauss_elimination(self):
        """Inicia o aplicativo de Eliminação de Gauss e redireciona"""
        try:
            print("DEBUG: Iniciando _launch_gauss_elimination")
            
            # Verifica se existe versão web
            gauss_html_path = os.path.join(GAUSS_ELIMINATION_PATH, 'index.html')
            if os.path.exists(gauss_html_path):
                print("DEBUG: Versão web encontrada, servindo diretamente")
                # Serve a versão web diretamente
                self._serve_gauss_web()
            else:
                print("DEBUG: Só versão desktop disponível")
                # Envia resposta de "aplicativo em execução"
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                
                message = """<!DOCTYPE html>
<html>
<head>
    <title>Iniciando Aplicativo</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #FFE4E6; }
        .spinner { border: 4px solid #f3f3f3; border-top: 4px solid #FF69B4; 
                  border-radius: 50%; width: 50px; height: 50px; 
                  animation: spin 1s linear infinite; margin: 20px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .button { display: inline-block; padding: 10px 20px; margin: 20px;
                 background-color: #FF69B4; color: white; border-radius: 25px;
                 text-decoration: none; font-weight: bold; }
        h1 { color: #C71585; }
    </style>
    <meta http-equiv="refresh" content="3;url=/">
</head>
<body>
    <h1>Iniciando o aplicativo de Eliminação de Gauss...</h1>
    <div class="spinner"></div>
    <p>O aplicativo está sendo iniciado em uma janela separada.</p>
    <p>Você será redirecionado para a página principal em 3 segundos.</p>
    <p><a href="/" class="button">Voltar à página principal</a></p>
</body>
</html>"""
                
                self.wfile.write(message.encode('utf-8'))
                print("DEBUG: Página de carregamento enviada")
                
                # Inicia o aplicativo em um processo separado
                print("DEBUG: Iniciando aplicativo Gauss")
                subprocess.Popen([sys.executable, os.path.join(GAUSS_ELIMINATION_PATH, 'main.py')])
                print("DEBUG: Aplicativo Gauss iniciado")
            
        except Exception as e:
            print(f"DEBUG: Erro em _launch_gauss_elimination: {str(e)}")
            self.send_error(500, f'Erro ao iniciar o aplicativo: {str(e)}')
    
    def _serve_gauss_web(self):
        """Serve a versão web do GaussEliminationSolver"""
        try:
            gauss_html_path = os.path.join(GAUSS_ELIMINATION_PATH, 'index.html')
            
            # Lê o arquivo HTML e modifica os links para usar gauss_static
            with open(gauss_html_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Ajusta os caminhos dos arquivos estáticos
            content = content.replace('href="style.css"', 'href="/gauss_static/style.css"')
            content = content.replace('src="gaussian_solver.js"', 'src="/gauss_static/gaussian_solver.js"')
            content = content.replace('src="app.js"', 'src="/gauss_static/app.js"')
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
            print("DEBUG: Versão web do Gauss servida com sucesso")
            
        except FileNotFoundError:
            print("DEBUG: Arquivo index.html do Gauss não encontrado")
            self.send_error(404, 'Versão web não encontrada')
        except Exception as e:
            print(f"DEBUG: Erro ao servir versão web do Gauss: {str(e)}")
            self.send_error(500, f'Erro ao servir versão web: {str(e)}')
    
    def _serve_gauss_static(self, file_path):
        """Serve arquivos estáticos do GaussEliminationSolver"""
        try:
            full_path = os.path.join(GAUSS_ELIMINATION_PATH, file_path)
            print(f"DEBUG: Tentando servir arquivo estático: {full_path}")
            
            # Determina o tipo de conteúdo
            if file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'
            elif file_path.endswith('.png'):
                content_type = 'image/png'
            elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                content_type = 'image/jpeg'
            else:
                content_type = 'text/plain'
            
            with open(full_path, 'rb') as file:
                content = file.read()
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(content)
            print(f"DEBUG: Arquivo estático servido: {full_path}")
            
        except FileNotFoundError:
            print(f"DEBUG: Arquivo estático não encontrado: {full_path}")
            self.send_error(404, 'Arquivo não encontrado')
        except Exception as e:
            print(f"DEBUG: Erro ao servir arquivo estático: {str(e)}")
            self.send_error(500, f'Erro ao servir arquivo: {str(e)}')
    
    def _serve_numeric_static(self, file_path):
        """Serve arquivos estáticos do NumericCalculator"""
        try:
            full_path = os.path.join(NUMERIC_CALCULATOR_PATH, file_path)
            print(f"DEBUG: Tentando servir arquivo estático do NumericCalculator: {full_path}")
            
            # Determina o tipo de conteúdo
            if file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'
            elif file_path.endswith('.png'):
                content_type = 'image/png'
            elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                content_type = 'image/jpeg'
            else:
                content_type = 'text/plain'
            
            with open(full_path, 'rb') as file:
                content = file.read()
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(content)
            print(f"DEBUG: Arquivo estático do NumericCalculator servido: {full_path}")
            
        except FileNotFoundError:
            print(f"DEBUG: Arquivo estático do NumericCalculator não encontrado: {full_path}")
            self.send_error(404, 'Arquivo não encontrado')
        except Exception as e:
            print(f"DEBUG: Erro ao servir arquivo estático do NumericCalculator: {str(e)}")
            self.send_error(500, f'Erro ao servir arquivo: {str(e)}')


def run_redirect_server(port=8000):
    """Inicia o servidor HTTP com o handler de redirecionamento"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, AppRedirectHandler)
    print(f"Servidor de redirecionamento rodando em http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_redirect_server()
