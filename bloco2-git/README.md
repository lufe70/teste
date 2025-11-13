# Bloco 2: Git - Governança e Rastreabilidade

## 🎯 Objetivo

Aprender a usar Git para:
- **Rastrear** mudanças no código (quem, quando, o quê)
- **Reverter** deploys desastrosos em < 1 minuto
- **Auditar** decisões críticas de produção
- **Colaborar** sem sobrescrever trabalho do time

---

## 📁 Estrutura

```
bloco2-git/
├── exemplo-inicial/        # API estável com histórico Git
├── exemplo-rollback/       # Cenário de rollback de emergência
└── scripts/                # Scripts de setup do Git
```

---

## 🚀 Como Usar

### **1. Exemplo Inicial - API Estável**

Veja uma API com histórico Git já configurado:

```bash
cd exemplo-inicial
git log --oneline
# Você verá o histórico de commits
```

### **2. Exemplo Rollback - Recuperação de Desastre**

Simule um deploy que quebra produção e aprenda a reverter:

```bash
cd exemplo-rollback
cat comandos.md  # Siga o roteiro passo a passo
```

---

## 🔧 Setup Git (Primeira Vez)

Se você nunca configurou o Git no seu computador:

**Windows:**
```bash
cd scripts
./setup_git.bat
```

**Linux/Mac:**
```bash
cd scripts
chmod +x setup_git.sh
./setup_git.sh
```

---

## 📚 Conceitos-Chave

### **Git vs GitHub**
- **Git**: Software no seu PC (máquina do tempo local)
- **GitHub**: Google Drive do código (nuvem colaborativa)

### **Por Que Git em ML?**
1. **Auditoria**: Quem mudou o threshold de fraude? Quando?
2. **Rollback**: Deploy quebrou? Voltar à versão estável em 1 minuto
3. **Experimentos**: Testar novo modelo sem afetar produção
4. **Colaboração**: 3 cientistas de dados no mesmo projeto

---

## ⚠️ Importante

- Git **NÃO apaga** erros, ele os **documenta** para aprendizado
- Em produção, ninguém comita direto na `main`
- Todo código passa por **Pull Request** (revisão de código)

---

## 📖 Comandos Essenciais

```bash
# Ver histórico
git log --oneline

# Reverter commit (mantém histórico)
git revert [hash]

# Quem mudou cada linha?
git blame arquivo.py
```

---

## 🎓 Próximos Passos

Após dominar o Bloco 2, você estará pronto para:
- **Bloco 3**: Debug e Observabilidade (diagnosticar falhas)
- **Bloco 4**: Testes Automatizados (garantir qualidade)
