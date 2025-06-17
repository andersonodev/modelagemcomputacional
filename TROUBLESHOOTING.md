# 🔧 Guia de Resolução de Problemas - CSS

## ❗ Problema: CSS do NumericCalculator não carrega

### 🔍 Diagnóstico

1. **Verificar se os servidores estão rodando:**
   ```bash
   # Terminal 1 - Servidor principal
   python3 main.py
   
   # Terminal 2 - Teste de conectividade
   python3 test_routes.py
   ```

2. **Verificar estrutura de arquivos:**
   ```
   NumericCalculator/
   ├── static/
   │   ├── css/
   │   │   └── style.css  ← Deve existir
   │   └── js/
   ├── templates/
   │   └── index.html     ← Deve ter link para CSS
   └── app.py
   ```

### 🛠️ Soluções Implementadas

#### 1. **Link CSS Adicionado ao HTML**
No arquivo `NumericCalculator/templates/index.html`, foi adicionado:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

#### 2. **Botão "Voltar" Corrigido**
O link agora aponta diretamente para o servidor principal:
```html
<a href="http://localhost:8000" class="back-to-home">
```

#### 3. **Handler de Arquivos Estáticos**
No `app_handler.py`, foi adicionado suporte para servir arquivos estáticos:
```python
elif parsed_path.path.startswith('/static/'):
    self._serve_numeric_static(file_path)
```

### 🚀 Teste de Funcionamento

Execute o seguinte para testar:

```bash
# 1. Inicie a aplicação principal
python3 main.py

# 2. Em outro terminal, teste as rotas
python3 test_routes.py

# 3. Acesse no navegador
# - http://localhost:8000 (página principal)
# - Clique em "Cálculo de Raízes"
# - Verifique se o CSS carrega corretamente
```

### 🎯 Verificações Importantes

1. **CSS está carregando?**
   - Abra DevTools (F12)
   - Vá para Network
   - Recarregue a página
   - Verifique se `style.css` aparece e não retorna erro 404

2. **Servidor NumericCalculator está ativo?**
   - Acesse http://localhost:8080 diretamente
   - Se retornar erro, o servidor não iniciou

3. **Botão voltar funciona?**
   - Clique no botão "Voltar ao Menu Principal"
   - Deve retornar para localhost:8000

### 📋 Checklist de Resolução

- [ ] Arquivo CSS existe em `NumericCalculator/static/css/style.css`
- [ ] Link CSS está no HTML do template
- [ ] Servidor principal está rodando na porta 8000
- [ ] NumericCalculator está rodando na porta 8080
- [ ] Botão "Voltar" aponta para localhost:8000
- [ ] DevTools não mostra erros 404 para arquivos CSS
- [ ] Aplicação abre corretamente no navegador

### 🆘 Se o problema persistir

1. **Reinicie completamente:**
   ```bash
   # Pare todos os processos Python
   pkill -f python
   
   # Inicie novamente
   python3 main.py
   ```

2. **Verifique portas em uso:**
   ```bash
   lsof -i :8000
   lsof -i :8080
   ```

3. **Cache do navegador:**
   - Force refresh: Ctrl+F5 (Windows/Linux) ou Cmd+Shift+R (Mac)
   - Ou abra em aba anônima/privada

4. **Logs de debug:**
   - Verifique o terminal onde executou `python3 main.py`
   - Procure por mensagens de erro ou debug

---

## ✅ Status Atual

- ✅ Página principal unificada funcionando
- ✅ CSS da página principal carregando
- ✅ Redirecionamento para NumericCalculator funcionando
- ✅ CSS do NumericCalculator corrigido
- ✅ Botão "Voltar" funcionando
- ✅ Sistema de navegação completo
