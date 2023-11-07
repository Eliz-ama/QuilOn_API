from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para criar a tabela de produtos no banco de dados SQLite
def create_table():
    connection = sqlite3.connect('Banco_products')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            production_time INTEGER NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Rota para criar um novo produto
@app.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    connection = sqlite3.connect('Banco_products')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO products (title, category, description, production_time, price, stock)
        VALUES (:title, :category, :description, :production_time, :price, :stock)
    ''', {
        'title': data['title'],
        'category': data['category'],
        'description': data['description'],
        'production_time': data['production_time'],
        'price': data['price'],
        'stock': data['stock']
    })
    connection.commit()
    connection.close()
    return 'Produto criado com sucesso', 201

# Rota para listar todos os produtos
@app.route('/products', methods=['GET'])
def get_products():
    connection = sqlite3.connect('Banco_products')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    connection.close()
    return jsonify({'products': products})

# Rota para atualizar um produto
@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    connection = sqlite3.connect('Banco_products')
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE products
        SET title = :title, category = :category, description = :description, production_time = :production_time, price = :price, stock = :stock
        WHERE id = :product_id
    ''', {
        'title': data['title'],
        'category': data['category'],
        'description': data['description'],
        'production_time': data['production_time'],
        'price': data['price'],
        'stock': data['stock'],
        'product_id': product_id
    })
    connection.commit()
    connection.close()
    return 'Produto atualizado com sucesso'

# Rota para excluir um produto
@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    connection = sqlite3.connect('Banco_products')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM products WHERE id = :product_id', {'product_id': product_id})
    connection.commit()
    connection.close()
    return 'Produto excluído com sucesso'

if __name__ == '__main__':
    create_table()  # Certifica-se de que a tabela existe antes de iniciar o aplicativo
    app.run(debug=True)