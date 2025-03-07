import google.generativeai as genai
import typing_extensions as typing
from typing import List, Optional
import json


class Product(typing.TypedDict):
    nome: Optional[str] = None
    subtitulo: Optional[str] = None
    marca: Optional[str] = None
    resumo: Optional[str] = None
    descrição: Optional[str] = None
    acabamento_cores: Optional[str] = None
    aplicações: Optional[str] = None
    capacidades_desempenho: Optional[str] = None
    composição: Optional[str] = None
    desempenho: Optional[str] = None
    dimensões_peso: Optional[str] = None
    normas_certificados: Optional[str] = None
    sustentabilidade: Optional[str] = None
    uso_aplicações: Optional[str] = None
    vantagens: Optional[str] = None


class Products(typing.TypedDict):
    products: List[Product]


api_key = ""

genai.configure(api_key=api_key)

file_path = "100boletim-aditivo-plastificante-quartzolit.pdf"

sample_file = genai.upload_file(
    path=file_path,
)

model = genai.GenerativeModel("gemini-1.5-flash")

context_text = """
Tarefa:
- Extraia o texto do PDF em anexo e estruture as informações dos produtos conforme as instruções abaixo.

Instruções:
- Gere um resumo conciso baseado exclusivamente nas informações presentes no texto.
- O conteúdo será utilizado em um portal de e-commerce.
- Não invente informações nem preencha lacunas com suposições. Utilize apenas os dados claramente identificáveis no texto.
- Se um produto não possuir informações suficientes para um anúncio claro e atrativo, ignore-o.
- Identifique corretamente a marca do produto:
- Não inclua o nome do fabricante, a menos que fabricante e marca sejam a mesma entidade.
- Se a marca estiver no nome do produto, utilize somente essa marca no campo "Marca".
- Não altere o nome do produto sob nenhuma circunstância.
- Categorize os produtos nas seguintes categorias: Eletrônicos, vestuário, livros.
- Extraia os seguintes atributos para cada produto: tamanho, cor, material, voltagem.
- Extraia informações de preço e disponibilidade no formato R$ 0,00.
- Padronize as unidades de medida para: cm, mm, kg, g.
"""

prompt_parts = [context_text, sample_file]

config = genai.GenerationConfig(
    response_mime_type="application/json",
    response_schema=Products,
)

response = model.generate_content(prompt_parts, generation_config=config)


products = Products(json.loads(response.text))
print(products.products)
