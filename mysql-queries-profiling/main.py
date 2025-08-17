import mysql.connector
import os
import time

def connect_to_database():
    """Connect to MySQL database with retry logic"""
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                database=os.getenv('DB_DATABASE', 'mydb'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', 'root'),
                port=os.getenv('DB_PORT', '3306')
            )
            print("Successfully connected to MySQL database")
            return connection
        except mysql.connector.Error as err:
            retry_count += 1
            print(f"Connection attempt {retry_count} failed: {err}")
            if retry_count < max_retries:
                print("Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("Max retries reached. Could not connect to database.")
                raise

def read_product_names():
    """Read and print all product names from the produtos table"""
    connection = None
    cursor = None
    
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        
        # Query to select all product names
        query = "SELECT name FROM produtos ORDER BY id"
        cursor.execute(query)
        
        # Fetch all results
        products = cursor.fetchall()
        
        if products:
            print("\n=== Product Names ===")
            for i, (product_name,) in enumerate(products, 1):
                print(f"{i}. {product_name}")
            print(f"\nTotal products: {len(products)}")
        else:
            print("No products found in the database.")
            
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("\nDatabase connection closed.")

def main():
    print("Starting product name reader...")
    read_product_names()

if __name__ == "__main__":
    main()