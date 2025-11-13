# 📁 Bloco 5: Variáveis de Ambiente e CORS

## 🎯 Objetivo

Aprender a configurar APIs de forma profissional usando variáveis de ambiente e habilitar consumo por frontends através de CORS.

---

## 📚 O Que Você Vai Aprender

### 1. Variáveis de Ambiente (.env)

- ✅ Por que NÃO hardcodar configurações
- ✅ Criar e usar arquivo .env
- ✅ Proteger segredos com .gitignore
- ✅ Documentar com .env.example

### 2. CORS (Cross-Origin Resource Sharing)

- ✅ O que é CORS e por que é necessário
- ✅ Configurar CORS no FastAPI
- ✅ Diferença entre desenvolvimento e produção
- ✅ Testar CORS com frontend simples

---

## 📂 Estrutura do Bloco

```
bloco3-env-cors/
│
├── README.md                    # Este arquivo
│
├── 1-sem-env/                   # ❌ Código com hardcode
│   ├── main.py
│   └── README.md
│
├── 2-com-env/                   # ✅ Código com .env
│   ├── main.py
│   ├── .env.example
│   ├── .gitignore
│   └── README.md
│
├── 3-com-cors/                  # ✅ Código com CORS
│   ├── main.py
│   ├── .env.example
│   ├── .gitignore
│   ├── test_cors.html
│   └── README.md
│
└── guias/
    ├── guia-env.md              # Guia completo de .env
    └── guia-cors.md             # Guia completo de CORS
```

---

## 🚀 Como Usar Este Material

### Passo 1: Seguir a Sequência

1. Abra `1-sem-env/` - veja o problema do hardcode
2. Abra `2-com-env/` - aprenda a usar .env
3. Abra `3-com-cors/` - configure CORS

### Passo 2: Rodar os Exemplos

Cada pasta tem seu próprio README com instruções específicas.

### Passo 3: Consultar os Guias

- Dúvidas sobre .env? Leia `guias/guia-env.md`
- Dúvidas sobre CORS? Leia `guias/guia-cors.md`

---

## 💡 Conceitos-Chave

### Variáveis de Ambiente

```
❌ Ruim: model_path = "artifacts/models/model.pkl"
✅ Bom:  model_path = os.getenv("MODEL_PATH")
```

**Por quê?**

- Configurações fora do código
- Senhas NUNCA no Git
- Fácil mudar entre dev/prod

### CORS

```
Frontend (http://meu-site.com) 
    ↓ tenta chamar
API (http://localhost:8000)
    ↓ sem CORS
❌ BLOQUEADO pelo navegador

    ↓ com CORS
✅ PERMITIDO
```

**Por quê?**

- Segurança do navegador
- Controle de quem acessa sua API
- Necessário para frontends consumirem a API

---

## 📖 Leitura Recomendada

### Documentação Oficial

- [FastAPI - CORS](https://fastapi.tiangolo.com/tutorial/cors/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Artigos

- [The Twelve-Factor App - Config](https://12factor.net/config)
- [MDN - CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

## ❓ Perguntas Frequentes

**P: Posso commitar o .env no Git?**  
R: ❌ NUNCA! Use .env.example como template.

**P: Preciso instalar algo para usar .env?**  
R: Sim, `python-dotenv`. Está no requirements.txt de cada exemplo.

**P: Por que usar "*" em CORS é ruim em produção?**  
R: Permite que QUALQUER site acesse sua API. Sempre especifique domínios em produção.

**P: Como testo se CORS está funcionando?**  
R: Use o arquivo `test_cors.html` no exemplo `3-com-cors/`.

---

## ## 📝 Notas Importantes

⚠️ **Segurança**

- Nunca versione .env
- Nunca exponha API keys em código
- Sempre use .env.example para documentar

⚠️ **Produção**

- CORS: especifique domínios, nunca use "*"
- ENV: use variáveis de ambiente do servidor, não arquivo .env

---

## 
