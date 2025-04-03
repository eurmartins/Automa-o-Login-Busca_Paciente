# Automacao de Login e Consulta de Paciente

## Descricao
Este script em Python realiza login no portal da SulAmerica Seguros e acessa diversas paginas do sistema, incluindo a consulta de um paciente especifico. Ele utiliza a biblioteca `requests` para gerenciar sessoes HTTP e interagir com a API do portal.

## Requisitos
- Python 3.x
- Biblioteca `requests`

Para instalar a biblioteca `requests`, utilize:
```sh
pip install requests
```

## Como Usar
1. **Configure o payload** com as credenciais de login no arquivo principal do script:
   ```python
   payload = {
       "codigoIndentificacao": "SEU_CODIGO",
       "usuario": "SEU_USUARIO",
       "senha": "SUA_SENHA"
   }
   ```
2. **Defina o identificador do paciente** no payload de busca:
   ```python
   payload_busca = {
       "busca_paciente": "ID_DO_PACIENTE"
   }
   ```
3. **Execute o script:**
   ```sh
   python nome_do_arquivo.py
   ```

## Funcionalidades
- Realiza login no portal da SulAmerica Seguros.
- Acessa paginas importantes para servicos medicos e faturamento.
- Busca um paciente especifico e verifica se foi encontrado.

## Contatos
Email: victormartinssantos.work@gmail.com

Linkedin: https://www.linkedin.com/in/victormartinssantos/
