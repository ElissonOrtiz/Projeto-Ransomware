
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

# Localizacao do projeto
BASE_DIR = Path(__file__).parent

# Diretorios do laboratorio
CRIPTOGRAFADOS = BASE_DIR / "laboratorio" / "criptografados"
RECUPERADOS = BASE_DIR / "laboratorio" / "recuperados"
CHAVE_FILE = BASE_DIR / "laboratorio" / "chave_teste.key"

# Arquivos autorizados para recuperacao
ARQUIVOS_TESTE = [
    "documento.txt",
    "relatorio.txt",
    "informacoes.txt"
]


def main():
    print("=== LABORATORIO DE RECUPERACAO ===")

    # Verificar se a chave existe
    if not CHAVE_FILE.is_file():
        print("Chave de recuperacao nao encontrada.")
        return

    # Carregar a chave
    chave = CHAVE_FILE.read_bytes()
    fernet = Fernet(chave)

    # Criar diretorio de recuperacao
    RECUPERADOS.mkdir(parents=True, exist_ok=True)

    for nome in ARQUIVOS_TESTE:
        origem = CRIPTOGRAFADOS / f"{nome}.enc"
        destino = RECUPERADOS / nome

        if not origem.is_file():
            print(f"Arquivo criptografado nao encontrado: {nome}")
            continue

        # Evitar sobrescrever arquivos recuperados
        if destino.exists():
            print(f"Arquivo ja recuperado: {nome}")
            continue

        try:
            conteudo = origem.read_bytes()
            resultado = fernet.decrypt(conteudo)

            destino.write_bytes(resultado)

            print(f"Arquivo recuperado: {nome}")

        except InvalidToken:
            print(f"Falha na recuperacao: {nome}")

    print("\nDemonstracao de recuperacao concluida.")
    print("Os arquivos criptografados foram preservados.")


if __name__ == "__main__":
    main()
