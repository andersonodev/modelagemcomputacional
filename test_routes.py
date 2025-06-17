#!/usr/bin/env python3
"""
Script de teste para verificar se as rotas estão funcionando corretamente
"""

import requests
import time
import subprocess
import sys
import os

def test_main_page():
    """Testa se a página principal está carregando"""
    try:
        response = requests.get('http://localhost:8000')
        print(f"Página principal - Status: {response.status_code}")
        if response.status_code == 200:
            print("✅ Página principal funcionando")
        else:
            print("❌ Página principal com problema")
    except Exception as e:
        print(f"❌ Erro ao acessar página principal: {str(e)}")

def test_css_files():
    """Testa se os arquivos CSS estão sendo servidos"""
    css_files = [
        'http://localhost:8000/style.css',  # CSS da página principal
        'http://localhost:8080/static/css/style.css'  # CSS do NumericCalculator
    ]
    
    for css_url in css_files:
        try:
            response = requests.get(css_url)
            print(f"CSS {css_url} - Status: {response.status_code}")
            if response.status_code == 200:
                print(f"✅ CSS carregando: {css_url}")
            else:
                print(f"❌ CSS com problema: {css_url}")
        except Exception as e:
            print(f"❌ Erro ao carregar CSS {css_url}: {str(e)}")

def test_numeric_calculator():
    """Testa se o NumericCalculator está rodando"""
    try:
        response = requests.get('http://localhost:8080')
        print(f"NumericCalculator - Status: {response.status_code}")
        if response.status_code == 200:
            print("✅ NumericCalculator funcionando")
        else:
            print("❌ NumericCalculator com problema")
    except Exception as e:
        print(f"❌ Erro ao acessar NumericCalculator: {str(e)}")

def main():
    print("🧪 Testando rotas e arquivos estáticos...\n")
    
    print("1. Testando página principal:")
    test_main_page()
    
    print("\n2. Testando arquivos CSS:")
    test_css_files()
    
    print("\n3. Testando NumericCalculator:")
    test_numeric_calculator()
    
    print("\n4. Verificando estrutura de arquivos:")
    root_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(root_dir, 'NumericCalculator', 'static', 'css', 'style.css')
    
    if os.path.exists(css_path):
        print("✅ Arquivo CSS existe no sistema de arquivos")
        with open(css_path, 'r') as f:
            content = f.read()
            if len(content) > 1000:  # Verifica se tem conteúdo substancial
                print(f"✅ Arquivo CSS tem conteúdo ({len(content)} caracteres)")
            else:
                print(f"⚠️ Arquivo CSS muito pequeno ({len(content)} caracteres)")
    else:
        print(f"❌ Arquivo CSS não encontrado em: {css_path}")

if __name__ == "__main__":
    main()
