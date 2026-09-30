"""Gera o PDF do ebook a partir do HTML do Claude Design.

Uso: python3 ebook/ferramentas/gerar_pdf.py
Antes de imprimir, troca as linhas de escrever (feitas com
repeating-linear-gradient, que o Chrome imprime com falhas) por traços reais.
"""
import os
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.dirname(AQUI)
HTML = os.path.join(PASTA, "90_Dias_Romantizando_Minha_Vida.html")
PDF = os.path.join(PASTA, "90_Dias_Romantizando_Minha_Vida.pdf")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

TROCAR_LINHAS = r"""
() => {
  let n = 0;
  document.querySelectorAll('section.page *').forEach(el => {
    const bg = getComputedStyle(el).backgroundImage;
    if (!bg.startsWith('repeating-linear-gradient')) return;
    const px = [...bg.matchAll(/(-?[\d.]+)(px|pt)/g)].map(m => parseFloat(m[1]) * (m[2] === 'pt' ? 4 / 3 : 1));
    const cor = [...bg.matchAll(/rgba?\([^)]*\)/g)].map(m => m[0]).pop();
    const inicio = px[2], periodo = px[3];
    if (!(periodo > 0)) return;
    const h = el.getBoundingClientRect().height;
    el.style.backgroundImage = 'none';
    if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
    for (let y = inicio; y + (periodo - inicio) <= h + 0.5; y += periodo) {
      const l = document.createElement('div');
      l.style.cssText = `position:absolute;left:0;right:0;top:${y}px;height:${periodo - inicio}px;background:${cor}`;
      el.appendChild(l); n++;
    }
  });
  return n;
}
"""


def main():
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME)
        pg = nav.new_page(viewport={"width": 1200, "height": 1250})
        pg.goto("file://" + HTML)
        pg.wait_for_timeout(6000)
        pg.emulate_media(media="print")
        pg.wait_for_timeout(1500)
        print("linhas trocadas:", pg.evaluate(TROCAR_LINHAS))
        pg.pdf(path=PDF, prefer_css_page_size=True, print_background=True)
        nav.close()
    print("PDF:", PDF)


if __name__ == "__main__":
    main()
