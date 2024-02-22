#   <img src="img/quilon.png" width="150" height="150"> API

 
## 🟡 Documentação da API


Esta API tem como objetivo oferecer funcionalidades essenciais para o cadastro, visualização, exclusão e atualização de informações relacionadas a produtos. Através dessa API, os representantes quilombolas desempenham um papel fundamental no gerenciamento e na manutenção desses dados, permitindo que registrem novos produtos, visualizem informações existentes, removam produtos obsoletos e atualizem detalhes importantes.


### **Versão da API:** 1.0




**Data de lançamento:** 2023-09-27



### URL Base

Nossa API esta sendo executada online e você pode consumi-la pelo link abaixo:

```bash
https://quilon-api.onrender.com
````


URL teste:

```bash
http://127.0.0.1:5000/
```


**Endereços da API**

| Tipo | Caminho | Observação |
|---|---|---|
| GET | /upload/<image_name> | Retorna uma imagem |
| POST | /product | Cria um novo produto |
| GET | /products | Retorna a lista com todos os produtos |
| GET | /product-ids | Lista os ids de todos os produtos |
| GET | /product/<int:product_id> | Busca um produto pelo id |
| PUT | /product/<int:product_id> | Atualiza um produto pelo id |
| DELETE | /product/<int:product_id> | Deleta um produto pelo id |

## 🟡 **Exemplo de requisição da API**

GET
```bash
https://quilon-api.onrender.com/upload/1
```
- 304 Imagem retornada com sucesso
- 404 Imagem não encontrada

<br>

POST
```bash
https://quilon-api.onrender.com/product
```
- 201 Produto criado com sucesso.
  
<br>

GET
```bash
https://quilon-api.onrender.com/products
```
- 200 Lista de produtos retornada com sucesso.
  
<br>

GET
```bash
https://quilon-api.onrender.com/product_ids
```
- 200 Lista de ids retornada com sucesso.

<br>

GET
```bash
https://quilon-api.onrender.com/product/1
```
- 200 Produto encontrado com sucesso.
- 404 Produto não encontrado.

<br>

PUT
```bash
https://quilon-api.onrender.com/product/1
```
- 200 Produto atualizado com sucesso.

<br>

DELETE
```bash
https://quilon-api.onrender.com/product/1
```
- 200 Produto excluido com sucesso.




