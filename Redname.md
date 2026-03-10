# Chat Cliente-Servidor com Criptografia AES

## Descrição

Este projeto implementa um sistema de chat utilizando arquitetura **cliente-servidor** com comunicação via **sockets TCP** e **criptografia AES**.

O objetivo é demonstrar na prática conceitos de redes e segurança, incluindo:

- Arquitetura cliente-servidor
- Comunicação via sockets
- Uso do protocolo TCP
- Criptografia de mensagens
- Manipulação de múltiplos clientes utilizando threads

Todas as mensagens transmitidas entre cliente e servidor são **criptografadas antes do envio** e **descriptografadas ao serem recebidas**.

---

## Linguagem utilizada

Python 3

---

## Bibliotecas utilizadas

- `socket` → comunicação em rede
- `threading` → suporte a múltiplos clientes
- `pycryptodome` → criptografia AES
- `base64` → codificação segura para transmissão

### Instalação da biblioteca necessária:

```bash
pip install pycryptodome
```

---

## Estrutura do Projeto

crypto_utils.py  
Responsável pela criptografia e descriptografia das mensagens usando AES.

echo_server.py  
Implementa o servidor que aceita conexões de múltiplos clientes utilizando threads.

echo_client.py  
Implementa o cliente que se conecta ao servidor e permite enviar mensagens.

---

## Arquivos do Projeto

### crypto_utils.py

Arquivo responsável pela implementação da criptografia e descriptografia das mensagens utilizando AES.

Funções principais:

- `criptografar(mensagem)`  
  Recebe uma mensagem em texto, aplica padding, criptografa utilizando AES e converte para Base64.

- `descriptografar(mensagem)`  
  Recebe uma mensagem criptografada, decodifica Base64, descriptografa e remove o padding.

---

### echo_server.py

Implementa o servidor do sistema.

Responsabilidades:

- Criar socket TCP
- Aguardar conexões de clientes
- Receber mensagens criptografadas
- Descriptografar mensagens
- Exibir mensagens no console
- Permitir que o operador responda manualmente
- Enviar resposta criptografada ao cliente

O servidor utiliza **threads** para permitir múltiplos clientes conectados simultaneamente.

---

### echo_client.py

Implementa o cliente que se conecta ao servidor.

Funções principais:

- Conectar ao servidor via TCP
- Ler mensagens digitadas pelo usuário
- Criptografar mensagens antes do envio
- Enviar mensagens ao servidor
- Receber resposta criptografada
- Descriptografar e exibir a resposta

---

## Criptografia

Foi utilizada criptografia simétrica AES (Advanced Encryption Standard).

As mensagens são:

1. Convertidas para bytes
2. Aplicado padding
3. Criptografadas com AES
4. Codificadas em Base64 para envio pela rede

A mesma chave secreta é utilizada pelo cliente e pelo servidor.

### Chave utilizada

A criptografia utiliza uma chave simétrica compartilhada entre cliente e servidor:

```python
KEY = b'chave_secreta123'
```

Esta chave possui **16 bytes**, sendo adequada para criptografia **AES-128**.

---

## Como executar

Instalar dependência:

pip install pycryptodome

Executar o servidor:

python echo_server.py

Executar o cliente em outro terminal:

python echo_client.py

---

## Arquitetura

Cliente → envia mensagem criptografada → Servidor

Servidor → descriptografa mensagem → processa

Servidor → criptografa resposta → envia para cliente

---

## Fluxo de funcionamento

1. O servidor inicia e aguarda conexões.
2. O cliente se conecta ao servidor via TCP.
3. O usuário digita uma mensagem no cliente.
4. A mensagem é criptografada usando AES.
5. O cliente envia a mensagem criptografada ao servidor.
6. O servidor descriptografa a mensagem e exibe no terminal.
7. O operador do servidor digita uma resposta.
8. A resposta é criptografada e enviada ao cliente.
9. O cliente descriptografa e exibe a mensagem.