"""Gera uma ilustração com a API de imagens da OpenAI (chave em ~/.config/ia-imagens.env).

python gerar_imagem.py <saida.png> "<descrição>" [--tamanho 1536x1024] [--qualidade medium]

Regra do canal: as imagens NUNCA levam texto (rótulos são desenhados pelo motor por cima)
e mapas de verdade vêm de _ferramentas/mapas.py, não da IA.
"""
import argparse, base64, json, sys, urllib.request, urllib.error
from pathlib import Path

ENV = Path.home() / ".config" / "ia-imagens.env"
ESTILO = (" Style: clean modern flat illustration with soft shading, bright and friendly, light warm off-white palette, "
          "simple shapes, no clutter. Absolutely no text, letters, numbers, logos or labels anywhere in the image.")


def chave():
    for ln in ENV.read_text(encoding="utf-8").splitlines():
        if ln.strip().startswith("OPENAI_API_KEY="):
            return ln.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("OPENAI_API_KEY não encontrada em " + str(ENV))


def gerar(saida, descricao, tamanho="1536x1024", qualidade="medium", modelo="gpt-image-1"):
    corpo = json.dumps({"model": modelo, "prompt": descricao + ESTILO, "size": tamanho, "quality": qualidade, "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=corpo, method="POST",
                                 headers={"Authorization": "Bearer " + chave(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            dados = json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"erro {e.code}: {e.read().decode(errors='replace')[:400]}")
    Path(saida).parent.mkdir(parents=True, exist_ok=True)
    Path(saida).write_bytes(base64.b64decode(dados["data"][0]["b64_json"]))
    print("ok", saida, dados.get("usage", ""))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("saida"); ap.add_argument("descricao")
    ap.add_argument("--tamanho", default="1536x1024"); ap.add_argument("--qualidade", default="medium")
    ap.add_argument("--modelo", default="gpt-image-1")
    a = ap.parse_args()
    gerar(a.saida, a.descricao, a.tamanho, a.qualidade, a.modelo)
