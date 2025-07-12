import database
import fuzzy


def main():
    database.setupdb()
    query = "Comercial Pró-Vendas Clientes"
    rows = database.search_using_near(query)
    fuzzy.fuzzy_search(query, rows)


if __name__ == "__main__":
    main()
