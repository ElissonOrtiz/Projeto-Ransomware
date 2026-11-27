
from pathlib import Path
from cryptography.fernet import Fernet

# Localizacao do projeto
BASE_DIR = Path(__file__).parent

# Diretorios do laboratorio
ORIGINAIS = BASE_DIR / "laboratorio" / "originais"
CRIPTOGRAFADOS = BASE_DIR / "laboratorio" / "criptografados"
CHAVE_FILE = BASE_DIR / "laboratorio" / "chave_teste.key"

# Lista fixa de arquivos ficticios
ARQUIVOS_TESTE = [
    "documento.txt",
    "relatorio.txt",
    "informacoes.txt"
]


def main():
    print("=== LABORATORIO DE CRIPTOGRAFIA ===")

    # Gerar uma chave exclusiva para o laboratorio
    chave = Fernet.generate_key()

    # Guardar a chave para permitir a recuperacao
    CHAVE_FILE.write_bytes(chave)

    # Inicializar o mecanismo de criptografia
    fernet = Fernet(chave)

    # Criar pasta de destino
    CRIPTOGRAFADOS.mkdir(parents=True, exist_ok=True)

    for nome in ARQUIVOS_TESTE:
        origem = ORIGINAIS / nome
        destino = CRIPTOGRAFADOS / f"{nome}.enc"

        if not origem.is_file():
            print(f"Arquivo nao encontrado: {nome}")
            continue

        conteudo = origem.read_bytes()
        resultado = fernet.encrypt(conteudo)

        destino.write_bytes(resultado)

        print(f"Arquivo de teste processado: {nome}")

    print("\nDemonstracao concluida.")
    print("Os arquivos originais foram preservados.")
    print(f"Chave de teste armazenada em: {CHAVE_FILE}")


if __name__ == "__main__":
    main()
