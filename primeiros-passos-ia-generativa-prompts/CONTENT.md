## Take 1 – Objetivo
Treinamento para Desenvolvedores: Resolvendo Problemas Cotidianos com IA Generativa

Neste treinamento, vamos demonstrar como aplicar a Inteligência Artificial Generativa para resolver desafios comuns do dia a dia na rotina de desenvolvimento de software.

## Take 2 – O que você precisa entender antes de começar

Explorando o OpenAI Playground - https://platform.openai.com/playground/prompts

Antes de tudo, é importante entender alguns conceitos fundamentais do Playground:

System Prompt: Define o comportamento da IA. Ex: "Você é um assistente que resume contratos de aluguel."

User Prompt: É o conteúdo enviado pelo usuário. Ex: "Texto do contrato: [conteúdo aqui]"

Temperatura: Controla a criatividade da resposta. Valores mais baixos geram saídas mais objetivas.

Modelo: Define qual versão do modelo será usada (ex: gpt-4o-mini, gpt-3.5-turbo, etc.).

#### Exemplo de Código

```
String systemPrompt = """
Você é um assistente que faz resumo de contratos de aluguel.
""";

String userPrompt = """
Texto do contrato:

LOCAÇÃO RESIDENCIAL

(NOME), (CPF), (IDENTIDADE), (ENDEREÇO), doravante denominado LOCADOR; (NOME), (CPF), (IDENTIDADE), (ENDEREÇO), doravante denominado LOCATÁRIO, celebram o presente contrato de locação residencial, com as cláusulas e condições seguintes: 

...
""";

Double temperatura = 0.0;

String model = "gpt-4o-mini";

String resposta = OpenAI.call(systemPrompt, userPrompt, temperatura, model);

```

Resultado

```O documento trata de um contrato de locação residencial celebrado entre duas partes: o LOCADOR e o LOCATÁRIO, devidamente identificados por nome, CPF, identidade e endereço.
```

## Take 3 – Mudando a Forma de Pensar: Prompts e Saídas Estruturadas

Nós, desenvolvedores, estamos acostumados a resolver problemas com classes e funções. Com a IA Generativa, essa lógica muda — passamos a trabalhar com prompts como principal ferramenta de solução.

Isso exige uma mudança de mentalidade: de “escrever código” para “escrever instruções”.

Além disso, as saídas estruturadas oferecem um enorme benefício: elas permitem controlar o formato da resposta da LLM, possibilitando que o resultado seja facilmente convertido em objetos, salvos em bancos de dados ou retornados por APIs.

Demonstração prática no Playground.

## Take 4 – Bibliotecas e Frameworks

Para integrar modelos generativos ao seu código, estas bibliotecas são ótimos pontos de partida:

- Python: openai/openai-python
- Java: spring-projects/spring-ai
- C#: microsoft/semantic-kernel

## Take 5 – Caso de Uso: Extração de Dados de um Boleto
Desmistificando a Complexidade da Extração com LLMs

Até pouco tempo atrás, implementar projetos de NER (Reconhecimento de Entidades Nomeadas) era uma tarefa complexa e limitada. Hoje, com o uso de LLMs — inclusive multimodais — conseguimos resolver esse tipo de problema com muito mais agilidade e menos código.

Demonstração prática no Playground.

## Take 6 – Caso de Uso: RAG de Uma Página
