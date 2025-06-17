#!/usr/bin/env python3
"""
Script de validação completa do projeto
Verifica se todos os componentes estão funcionando corretamente
"""

import os
import sys
import subprocess
import time
import webbrowser
from threading import Thread

def check_file_structure():
    """Verifica se a estrutura de arquivos está correta"""
    print("🔍 Verificando estrutura de arquivos...")
    
    required_files = [
        'main.py',
        'app_handler.py',
        'index.html',
        'style.css',
        'images/root-finding.png',
        'images/linear-system.png',
        'NumericCalculator/app.py',
        'NumericCalculator/main.py',
        'NumericCalculator/static/css/style.css',
        'NumericCalculator/templates/index.html',
        'GaussEliminationSolver/main.py',
        'GaussEliminationSolver/gui_components.py',
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Arquivos ausentes:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ Todos os arquivos necessários estão presentes")
        return True

def check_css_content():
    """Verifica se o CSS tem conteúdo adequado"""
    print("\n🎨 Verificando conteúdo do CSS...")
    
    css_files = [
        ('style.css', 'CSS da página principal'),
        ('NumericCalculator/static/css/style.css', 'CSS do NumericCalculator')
    ]
    
    for css_file, description in css_files:
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content) > 1000:
                    print(f"✅ {description}: {len(content)} caracteres")
                else:
                    print(f"⚠️ {description}: Muito pequeno ({len(content)} caracteres)")
        else:
            print(f"❌ {description}: Arquivo não encontrado")

def check_html_css_links():
    """Verifica se os links CSS estão corretos no HTML"""
    print("\n🔗 Verificando links CSS no HTML...")
    
    html_file = 'NumericCalculator/templates/index.html'
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'url_for(\'static\', filename=\'css/style.css\')' in content:
                print("✅ Link CSS correto no template do NumericCalculator")
            else:
                print("❌ Link CSS ausente no template do NumericCalculator")
                
            if 'href="http://localhost:8000"' in content:
                print("✅ Botão 'Voltar' aponta para o servidor correto")
            else:
                print("⚠️ Botão 'Voltar' pode não estar apontando para o servidor correto")
    else:
        print("❌ Template HTML do NumericCalculator não encontrado")

def start_application():
    """Inicia a aplicação e testa o funcionamento"""
    print("\n🚀 Iniciando aplicação...")
    
    try:
        # Inicia o aplicativo principal em background
        process = subprocess.Popen([sys.executable, 'main.py'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # Aguarda um momento para o servidor iniciar
        time.sleep(3)
        
        print("✅ Aplicação iniciada com sucesso")
        print("🌐 Acesse: http://localhost:8000")
        
        # Opcionalmente abre o navegador
        choice = input("\nDeseja abrir o navegador automaticamente? (s/n): ")
        if choice.lower() == 's':
            webbrowser.open("http://localhost:8000")
        
        print("\n⚡ Para parar a aplicação, use Ctrl+C")
        
        # Mantém o processo em execução até o usuário decidir parar
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Parando aplicação...")
            process.terminate()
            process.wait()
            
    except Exception as e:
        print(f"❌ Erro ao iniciar aplicação: {str(e)}")

def main():
    """Função principal de validação"""
    print("🧪 VALIDAÇÃO COMPLETA DO PROJETO")
    print("=" * 50)
    
    # Verifica estrutura de arquivos
    if not check_file_structure():
        print("\n❌ Validação falhou - arquivos ausentes")
        return
    
    # Verifica conteúdo CSS
    check_css_content()
    
    # Verifica links HTML
    check_html_css_links()
    
    print("\n" + "=" * 50)
    print("✅ VALIDAÇÃO CONCLUÍDA")
    print("=" * 50)
    
    # Pergunta se quer iniciar a aplicação
    choice = input("\nDeseja iniciar a aplicação agora? (s/n): ")
    if choice.lower() == 's':
        start_application()
    else:
        print("\n📋 Para iniciar manualmente, execute: python3 main.py")

if __name__ == "__main__":
    main()
