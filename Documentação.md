**Documentação da API**

**Introdução**

Esta documentação descreve a API do aplicativo QuilOn, que fornece acesso a recursos de inserção, edição, remoção e busca para comunicação com o sistema.

**Versão da API:** 1.0

**Data de lançamento:** 2023-09-27

**Base URL:** https://quilon-api.onrender.com/

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

**Exemplo de uso da API**
