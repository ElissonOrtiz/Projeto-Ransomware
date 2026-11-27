
from pathlib import Path
import hashlib

BASE_DIR = Path(__file__).parent

ORIGINAIS = BASE_DIR / "laboratorio" / "originais"
RECUPERADOS = BASE_DIR / "laboratorio" / "recuperados"

ARQUIVOS_TESTE = [
    "documento.txt",
    "relatorio.txt",
    "informacoes.txt"
]


def calcular_hash(caminho):
    conteudo = caminho.read_bytes()
    return hashlib.sha256(conteudo).hexdigest()


print("=== VALIDACAO DE INTEGRIDADE ===")

for nome in ARQUIVOS_TESTE:
    original = ORIGINAIS / nome
    recuperado = RECUPERADOS / nome

    if not original.is_file() or not recuperado.is_file():
        print(f"ARQUIVO AUSENTE: {nome}")
        continue

    hash_original = calcular_hash(original)
    hash_recuperado = calcular_hash(recuperado)

    if hash_original == hash_recuperado:
        print(f"OK - Conteudo identico: {nome}")
    else:
        print(f"ERRO - Conteudo diferente: {nome}")

print("\nValidacao finalizada.")
