# 🚀 Careers API

API desenvolvida para o teste técnico de backend.  
Projeto construído com **Django**, **Django REST Framework**, **PostgreSQL** e **Swagger** (via `drf-yasg`), e containerizado com **Docker**.

---

## 🧪 Funcionalidades

- Criar, listar, editar e deletar os 'careers' de usuários.
- Documentação Swagger disponível em `/swagger/`.

---

## ⚙️ Requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados.

---

## 📁 Variáveis de ambiente

Crie um arquivo `.env` na pasta `dotenv_files` (localizada na raiz do projeto) a partir do arquivo de exemplo `.env-example`.

---

## 🚀 Como executar

1. Abra o terminal e navegue até a raiz do projeto.  
2. Execute o comando abaixo para subir os containers e construir a aplicação:

```bash
docker-compose up --build
```

3. Aguarde a inicialização completa do servidor.
4. Após o início, os serviços estarão disponíveis nos seguintes endereços:

- API: http://localhost:8000/
- Swagger: http://localhost:8000/swagger/

---

## 🧼 Extras

- Banco de dados: PostgreSQL (em container separado).
- Documentação automática: Swagger via drf-yasg.

---
  
## 📦 Exemplos de Requisições

**POST** `/careers/`

```json
{
    "username": "string",
    "title": "string",
    "content": "string"
}
```

**Resposta:**
```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
```

---

**GET** `/careers/`

**Resposta:**
```json
[
  {
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
  }
]
```

---

**PATCH** `/careers/1/`

```json
{
    "title": "string",
    "content": "string"
}
```

**Resposta:**
```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
```

---

**DELETE** `/careers/1/`

**Resposta:**
Status 204 No Content

---

## 📬 Contato  

Caso tenha dúvidas, entre em contato:  

📧 E-mail: [pedroiegler1601@outlook.com](mailto:pedroiegler1601@outlook.com)  
