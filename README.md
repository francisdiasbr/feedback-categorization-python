# POC: Categorização de Feedbacks com o uso de IA (OpenAI)

## Objetivo

Esta POC tem como objetivo categorizar comentários de clientes utilizando a OpenAI.

A análise será feita com base no texto do comentário para atribuir uma categoria específica que melhor descreva o feedback.

As categorias consideradas são:

- **ATTENDANCE**
- **PAYMENT**
- **COMFORT**
- **WAITING_TIME**
- **PRODUCT**
- **PRODUCT_AVAILABILITY**
- **PRICE**
- **PRODUCT_QUALITY**
- **COMPLIMENT**
- **NONE**
- **INTERESTS**
- **FINANCIAL_PRODUCTS**

A propriedade `category` no objeto será preenchida pela IA após a análise do comentário.


## Resumo geral

- Este código cria uma API Flask com uma rota /categorization.
- A lógica da categorização está separada no módulo controller.


## Configuração de Ambiente e Inicialização da Aplicação

### Pré-requisitos: 

- Python 3.9+
- Obter uma api-key no site da OpenAI - https://platform.openai.com/api-keys


### 1. Crie e ative o ambiente virtual

```
  python3 -m venv venv
  source venv/bin/activate  # Windows: `venv\Scripts\activate`
```

### 2. Instale as dependências

```
  pip install -r requirements.txt
```

### 3. Inicie a aplicação 

```
python app.py
```

### 4. Acesse a rota

Acesse a rota `/categorization` para realizar a categorização dos comentários:

Request (with cURL):

```
curl --location 'http://127.0.0.1:5000/categorization' \
--header 'api-key: xxx' \
--header 'model: gpt-4o' \
--header 'Content-Type: application/json' \
--data '{
    "categories": ["ATTENDANCE", "PAYMENT", "COMFORT", "WAITING_TIME", "PRODUCT", "PRODUCT_AVAILABILITY", "PRICE", "PRODUCT_QUALITY", "COMPLIMENT", "NONE", "INTERESTS", "FINANCIAL_PRODUCTS"],
    "comments": [
        {
            "id": 1,
            "comment": "Fui muito bem atendido pelos vendedores, todos simpáticos e prestativos."
        },
        {
            "id": 2,
            "comment": "A loja é bem organizada e confortável, gostei do espaço amplo."
        },
        {
            "id": 3,
            "comment": "Comprei um sapato que veio com defeito, mas foi trocado rapidamente."
        }
    ],
    "instructions": "Você é um especialista em classificar comentários. Classifique cada comentário com sua respectiva categoria."
}'
```

corpo da request (JSON):

```
{
    "categories": ["ATTENDANCE", "PAYMENT", "COMFORT", "WAITING_TIME", "PRODUCT", "PRODUCT_AVAILABILITY", "PRICE", "PRODUCT_QUALITY", "COMPLIMENT", "NONE", "INTERESTS", "FINANCIAL_PRODUCTS"],
    "comments": [
        {
            "id": 1,
            "comment": "Fui muito bem atendido pelos vendedores, todos simpáticos e prestativos."
        },
        {
            "id": 2,
            "comment": "A loja é bem organizada e confortável, gostei do espaço amplo."
        },
        {
            "id": 3,
            "comment": "Comprei um sapato que veio com defeito, mas foi trocado rapidamente."
        }
    ],
    "instructions": "Você é um especialista em classificar comentários. Classifique cada comentário com sua respectiva categoria."
}
```


Exemplo de resposta:

```
{
    "data": [
        {
            "category": "ATTENDANCE",
            "comment": "Fui muito bem atendido pelos vendedores, todos simpáticos e prestativos.",
            "id": 1
        },
        {
            "category": "COMFORT",
            "comment": "A loja é bem organizada e confortável, gostei do espaço amplo.",
            "id": 2
        },
        {
            "category": "PRODUCT_QUALITY",
            "comment": "Comprei um sapato que veio com defeito, mas foi trocado rapidamente.",
            "id": 3
        }
    ],
    "ok": true
}
```

## Observações

Arquivo de Dados Mock: Mais exemplos podem ser encontrados no arquivo mockdata.json.

Headers Necessários: Certifique-se de incluir os headers api-key e model com valores adequados.

Personalização: A lista de categorias e os comentários podem ser adaptados conforme a necessidade do projeto.
