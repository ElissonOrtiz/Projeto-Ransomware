# Projeto Ransomware em Python

## 1. Sobre o projeto

Este projeto foi desenvolvido como atividade prática de estudos em Segurança da Informação, utilizando a linguagem Python para demonstrar conceitos de criptografia e recuperação de arquivos.

A proposta consiste em apresentar, em ambiente controlado, como funciona a criptografia de arquivos e como a utilização de uma chave criptográfica permite recuperar os dados originais.

Todos os testes foram realizados com arquivos fictícios, exclusivamente para fins educacionais.

## 2. Objetivos

- Compreender o funcionamento da criptografia simétrica.
- Conhecer a biblioteca Cryptography do Python.
- Demonstrar o processo de criptografia e descriptografia.
- Entender a importância do gerenciamento de chaves.
- Validar a integridade dos arquivos utilizando SHA-256.

## 3. Tecnologias utilizadas

- Python 3.13.5
- PyCharm
- Biblioteca Cryptography 50.0.2
- Algoritmo Fernet
- SHA-256
- Windows

## 4. Estrutura do projeto

```text
Projeto-Ransomware/
│
├── Encrypter.py
├── Decrypter.py
├── Validar_recuperacao.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── laboratorio/
│   ├── originais/
│   ├── criptografados/
│   └── recuperados/
│
└── images/
```

## 5. Funcionamento

### Encrypter.py

Responsável por gerar uma chave criptográfica e utilizar o mecanismo Fernet para criptografar arquivos fictícios previamente definidos.

Os arquivos originais são preservados, enquanto os resultados são armazenados em um diretório separado.

### Decrypter.py

Responsável por utilizar a chave gerada anteriormente para descriptografar os arquivos de teste e armazenar os resultados em outro diretório.

### Validar_recuperacao.py

Realiza a comparação dos arquivos originais com os arquivos recuperados utilizando o algoritmo SHA-256.

A igualdade dos hashes confirma que os conteúdos dos arquivos são idênticos.

## 6. Resultados obtidos

Durante os testes realizados, foram utilizados três arquivos fictícios:

- documento.txt
- relatorio.txt
- informacoes.txt

Os três arquivos foram criptografados e posteriormente recuperados com sucesso.

A validação de integridade apresentou resultados positivos para todos os arquivos.

## 7. Segurança e cuidados

O projeto foi desenvolvido exclusivamente para fins educacionais, em ambiente isolado e com arquivos fictícios.

Os arquivos originais foram preservados durante todo o experimento.

A chave criptográfica utilizada nos testes não deve ser compartilhada publicamente.

## 8. Conclusão

O desenvolvimento deste projeto permitiu compreender, na prática, conceitos importantes de criptografia simétrica, gerenciamento de chaves e integridade de dados.

Também foi possível observar a importância de manter mecanismos adequados de recuperação e proteção das informações, especialmente no contexto de ameaças como ransomware.

A atividade contribuiu para ampliar os conhecimentos em Python e Segurança da Informação.