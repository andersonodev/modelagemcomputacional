# 🧮 Modelagem Computacional - Métodos Numéricos

Um projeto unificado que implementa diferentes métodos numéricos para resolver problemas de engenharia computacional.

## 📋 Visão Geral

Este projeto combina dois aplicativos de métodos numéricos em uma interface unificada:

1. **Cálculo de Raízes de Funções** - Métodos de Falsa Posição e Newton-Raphson
2. **Resolução de Sistemas Lineares** - Eliminação Gaussiana com Pivoteamento Parcial

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- Bibliotecas: tkinter, flask, webbrowser

### Execução
1. Clone o repositório
2. Navegue até o diretório do projeto
3. Execute o comando:
```bash
python3 main.py
```

4. A página principal será aberta automaticamente no seu navegador
5. Escolha o método desejado e comece a usar!

## 🔧 Resolução de Problemas

Se o CSS não estiver carregando corretamente, consulte o arquivo [TROUBLESHOOTING.md](TROUBLESHOOTING.md) para soluções detalhadas.

### Problemas Comuns:
- **CSS não carrega**: Verifique se ambos os servidores estão rodando (portas 8000 e 8080)
- **Botão "Voltar" não funciona**: Limpe o cache do navegador ou force refresh (Ctrl+F5)
- **Aplicação não abre**: Verifique se as portas não estão em uso por outros processos

## 🎯 Funcionalidades

### 🏠 Página Principal
- Interface unificada para seleção de método
- Design responsivo e atrativo
- Navegação intuitiva entre aplicações

### 📐 Cálculo de Raízes
- **Método da Falsa Posição (Regula-Falsi)**
- **Método de Newton-Raphson**
- Interface web interativa
- Calculadora científica integrada
- Visualização detalhada das iterações
- Editor matemático com LaTeX

### 🔢 Sistemas Lineares
- **Eliminação Gaussiana com Pivoteamento Parcial**
- Interface gráfica intuitiva
- Solução passo-a-passo detalhada
- Verificação automática da solução
- Exemplos pré-carregados

## 🔄 Navegação

Ambas as aplicações possuem botão **"Voltar ao Menu Principal"** que permite:
- Retornar à página inicial
- Navegar entre diferentes métodos
- Fechar aplicações desktop quando necessário

## 👥 Equipe

- **Anderson Lima de Araújo Júnior**
- **Lucas**
- **Sabrina**
- **Babinski**

## 📚 Disciplina

**Modelagem Computacional**  
Métodos Numéricos para Engenharia  
© 2025

## 🎨 Design

Interface desenvolvida com tema rosa/feminino, proporcionando uma experiência visual agradável e moderna.

---

### 📁 Estrutura do Projeto

```
modelagem-computacional_trabalho/
├── main.py                    # Aplicação principal
├── app_handler.py            # Handler de redirecionamento
├── index.html               # Página inicial unificada
├── style.css               # Estilos da página principal
├── images/                 # Imagens da interface
│   ├── root-finding.png
│   └── linear-system.png
├── NumericCalculator/      # Aplicação de cálculo de raízes
│   ├── app.py
│   ├── main.py
│   ├── numerical_methods.py
│   ├── templates/
│   └── static/
└── GaussEliminationSolver/ # Aplicação de sistemas lineares
    ├── main.py
    ├── gui_components.py
    ├── gaussian_solver.py
    └── matrix_display.py
```
# modelagemcomputacional
