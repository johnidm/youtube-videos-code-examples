import sqlite3

def configurar_e_buscar_fts5():
    conn = sqlite3.connect(':memory:') # Banco de dados em memória para o exemplo
    cursor = conn.cursor()

    # Habilitar o FTS5 criando uma tabela virtual
    # content_rowid é a PK da tabela original se você quiser vincular
    cursor.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS artigos USING fts5(titulo, texto, palavras_chave);
    """)

    # Inserir alguns dados de exemplo
    dados_artigos = [
        ("Clientes Contas a Pagar: Dicas Essenciais", "Este artigo detalha como otimizar o processo de contas a pagar para seus clientes.", "contas pagar clientes finanças"),
        ("Gestão de Contas a Receber para Pequenas Empresas", "Aprenda a gerenciar as contas a receber e o fluxo de caixa.", "contas receber gestão empresas"),
        ("Como Organizar suas Contas Pessoais", "Um guia simples para o orçamento e contas pessoais.", "contas pessoais orçamento finanças"),
        ("Guia Completo para o Fluxo de Caixa da sua Empresa", "Entenda o fluxo de caixa e sua importância.", "fluxo caixa empresa finanças"),
        ("Otimizando o Processo de Contas a Pagar", "Melhore a eficiência do seu setor de contas a pagar.", "contas pagar otimização processo")
    ]

    cursor.executemany("INSERT INTO artigos (titulo, texto, palavras_chave) VALUES (?, ?, ?);", dados_artigos)
    conn.commit()

    print("Tabela FTS5 criada e dados inseridos.")

    # Exemplo de busca básica no FTS5
    termo_busca = "clientes contas pagar"
    print(f"\nBuscando por: '{termo_busca}' (busca OR implícita)")
    cursor.execute(f"SELECT rank, titulo, texto FROM artigos WHERE artigos MATCH '{termo_busca}';")
    resultados = cursor.fetchall()
    for rank, titulo, texto in resultados:
        print(f"  Rank: {rank:.2f}, Título: '{titulo}', Trecho: '{texto[:50]}...'")

    # Exemplo de busca por proximidade (NEAR)
    termo_busca_proximidade = "contas NEAR pagar"
    print(f"\nBuscando por: '{termo_busca_proximidade}' (palavras próximas)")
    # O NEAR sem número significa que as palavras devem estar adjacentes ou próximas.
    # Você pode especificar um limite: "termo1 NEAR/N termo2" (N é o número máximo de palavras entre eles)
    cursor.execute(f"SELECT rank, titulo, texto FROM artigos WHERE artigos MATCH '{termo_busca_proximidade}';")
    resultados_proximidade = cursor.fetchall()
    for rank, titulo, texto in resultados_proximidade:
        print(f"  Rank: {rank:.2f}, Título: '{titulo}', Trecho: '{texto[:50]}...'")

    # Exemplo de busca com prefixo (aproximada no início da palavra)
    termo_busca_prefixo = "cli*" # Busca por "cli", "clientes", "clima", etc.
    print(f"\nBuscando por prefixo: '{termo_busca_prefixo}'")
    cursor.execute(f"SELECT rank, titulo, texto FROM artigos WHERE artigos MATCH '{termo_busca_prefixo}';")
    resultados_prefixo = cursor.fetchall()
    for rank, titulo, texto in resultados_prefixo:
        print(f"  Rank: {rank:.2f}, Título: '{titulo}', Trecho: '{texto[:50]}...'")

    # Exemplo de busca combinada (termo obrigatório + termo opcional)
    termo_busca_combinada = '"contas a pagar" OR clientes' # "contas a pagar" como frase exata OU "clientes"
    print(f"\nBuscando por frase exata OU termo: '{termo_busca_combinada}'")
    cursor.execute(f"SELECT rank, titulo, texto FROM artigos WHERE artigos MATCH '{termo_busca_combinada}';")
    resultados_combinada = cursor.fetchall()
    for rank, titulo, texto in resultados_combinada:
        print(f"  Rank: {rank:.2f}, Título: '{titulo}', Trecho: '{texto[:50]}...'")


    conn.close()

# Executa a função de exemplo do FTS5
configurar_e_buscar_fts5()