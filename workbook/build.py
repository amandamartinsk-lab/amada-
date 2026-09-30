"""Gera o workbook "90 Dias de Vida Bonita" como HTML e PDF (A4).

Uso:  python3 workbook/build.py
Saída: workbook/dist/90-dias-de-vida-bonita.pdf

Para mudar a marca, o ano ou a data de início, edite as constantes abaixo.
"""
import datetime as dt
import html
import os
import subprocess

from content import RITUAIS

MARCA = "AMADA"
TITULO = "90 Dias de Vida Bonita"
SUBTITULO = "um desafio para romantizar a sua rotina"
INICIO = dt.date(2026, 10, 3)
DIAS = 90

AQUI = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(AQUI, "dist")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

SEMANA_CURTA = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
SEMANA_LONGA = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]

FIM = INICIO + dt.timedelta(DIAS - 1)
e = html.escape


def dia(n):
    return INICIO + dt.timedelta(n - 1)


def curta(d):
    return f"{SEMANA_CURTA[d.weekday()]} {d.day}/{d.month}"


def longa(d):
    return f"{SEMANA_LONGA[d.weekday()]}, {d.day} de {MESES[d.month - 1]}"


def pagina(corpo, classe="", ancora=None, rodape=True):
    id_attr = f' id="{ancora}"' if ancora else ""
    pe = ""
    if rodape:
        pe = (f'<div class="rodape"><span>{e(MARCA)}</span>'
              f'<span>{e(TITULO.lower())}</span>'
              f'<a href="#sumario">sumário</a></div>')
    return f'<section class="page {classe}"{id_attr}><div class="inner">{corpo}</div>{pe}</section>'


def cabecalho(titulo_normal, titulo_italico, direita=""):
    return (f'<div class="cab"><h2>{e(titulo_normal)}<em>{e(titulo_italico)}</em></h2>'
            f'<span class="rotulo">{direita}</span></div>')


def linhas(n, classe="linha"):
    return "".join(f'<div class="{classe}"></div>' for _ in range(n))


def bolinhas(n, classe="bol"):
    return "".join(f'<span class="{classe}"></span>' for _ in range(n))


# ---------------------------------------------------------------- semanas
def semanas():
    """Divide os 90 dias em blocos de 7 (o último fica com 6)."""
    out = []
    n = 1
    while n <= DIAS:
        out.append(list(range(n, min(n + 7, DIAS + 1))))
        n += 7
    return out


SEMANAS = semanas()


# ---------------------------------------------------------------- páginas fixas
def capa():
    corpo = f"""
    <div class="capa-moldura">
      <div class="rotulo capa-topo">um caderno de {e(MARCA)}</div>
      <div class="capa-centro">
        <div class="capa-num">90</div>
        <h1>dias de<br><em>vida bonita</em></h1>
        <div class="fio"></div>
        <p class="capa-sub">{e(SUBTITULO)}</p>
        <p class="capa-datas">3 de outubro — 31 de dezembro de {INICIO.year}</p>
      </div>
      <div class="capa-nome">
        <span class="rotulo">este caderno pertence a</span>
        <div class="linha"></div>
      </div>
    </div>"""
    return pagina(corpo, "capa", rodape=False)


def boas_vindas():
    corpo = f"""
    {cabecalho("boas-", "vindas", "antes de começar")}
    <div class="texto">
      <p class="abre">Romantizar a vida não é fingir que está tudo perfeito.
      É escolher prestar atenção.</p>
      <p>Nos próximos 90 dias, você não vai virar outra pessoa. Você vai fazer
      pequenas coisas, todos os dias, que deixam a rotina um pouco mais bonita:
      um café tomado com calma, uma mesa posta para uma refeição comum, uma
      caminhada sem fones, uma noite sem telas.</p>
      <p>Somadas, essas pequenas escolhas mudam a forma como você vive o
      seu dia. E você termina o ano sabendo exatamente como chegou até aqui.</p>
      <p>Não existe jeito errado de usar este caderno. Se perder um dia, vire a
      página e continue. O desafio é sobre voltar, não sobre ser perfeita.</p>
    </div>
    <h3 class="sub">como usar</h3>
    <ol class="passos">
      <li><b>Comece pelas intenções.</b> Escreva quem você quer ser em 31 de dezembro.</li>
      <li><b>Planeje a semana.</b> Todo começo de semana tem um planner semanal,
      um tracker de hábitos e um cardápio.</li>
      <li><b>Viva um ritual por dia.</b> Cada dia do diário traz um pequeno ritual
      para romantizar a sua rotina.</li>
      <li><b>Pare nos checkpoints.</b> Nos dias 30, 60 e 90 há uma página para
      olhar para trás e ajustar a rota.</li>
    </ol>
    <p class="nota">Dica: este PDF tem links. No GoodNotes, Notability ou
    no computador, toque em “sumário” no rodapé para navegar.</p>
    """
    return pagina(corpo, ancora="boas-vindas")


def sumario():
    itens = [("boas-vindas", "Boas-vindas e como usar"),
             ("intencoes", "Minhas intenções"),
             ("mapa", "Mapa dos 90 dias"),
             ("rituais", "Os 90 rituais"),
             ("mes-10", "Outubro"), ("mes-11", "Novembro"), ("mes-12", "Dezembro")]
    fixos = "".join(f'<li><a href="#{a}">{e(t)}</a></li>' for a, t in itens)
    sem = ""
    for i, s in enumerate(SEMANAS, 1):
        a, b = dia(s[0]), dia(s[-1])
        sem += (f'<li><a href="#semana-{i}">semana {i:02d}</a>'
                f'<span>{a.day}/{a.month} – {b.day}/{b.month}</span></li>')
    corpo = f"""
    {cabecalho("o ", "sumário", "toque para navegar")}
    <div class="sum-cols">
      <div><h3 class="sub">começo</h3><ul class="sum">{fixos}</ul>
        <h3 class="sub">checkpoints</h3>
        <ul class="sum">
          <li><a href="#checkpoint-30">Dia 30</a><span>{curta(dia(30))}</span></li>
          <li><a href="#checkpoint-60">Dia 60</a><span>{curta(dia(60))}</span></li>
          <li><a href="#checkpoint-90">Dia 90</a><span>{curta(dia(90))}</span></li>
          <li><a href="#carta-final">Carta para 2027</a></li>
        </ul></div>
      <div><h3 class="sub">as 13 semanas</h3><ul class="sum">{sem}</ul></div>
    </div>"""
    return pagina(corpo, ancora="sumario")


def intencoes():
    corpo = f"""
    {cabecalho("minhas ", "intenções", "dia 00")}
    <p class="pergunta">Em 31 de dezembro, eu quero ser uma pessoa que…</p>
    {linhas(4)}
    <p class="pergunta">Três sentimentos que eu quero ter mais nos próximos 90 dias</p>
    <div class="tres">{"".join('<div class="caixa-p"></div>' for _ in range(3))}</div>
    <p class="pergunta">O que eu quero deixar de fazer</p>
    {linhas(3)}
    <p class="pergunta">Os hábitos que vou acompanhar</p>
    <div class="habitos-lista">{"".join(f'<div class="h-item"><span>{i}</span><div class="linha"></div></div>' for i in range(1, 7))}</div>
    <p class="pergunta">Por que isso importa para mim</p>
    {linhas(3)}
    <div class="assinatura"><div><div class="linha"></div><span class="rotulo">assinatura</span></div>
    <div><div class="linha"></div><span class="rotulo">data</span></div></div>
    """
    return pagina(corpo, ancora="intencoes")


def mapa():
    casas = ""
    for n in range(1, DIAS + 1):
        d = dia(n)
        marca = " cp" if n in (30, 60, 90) else ""
        casas += (f'<a class="casa{marca}" href="#dia-{n}"><b>{n:02d}</b>'
                  f'<span>{d.day}/{d.month}</span></a>')
    corpo = f"""
    {cabecalho("o ", "mapa", "pinte um dia cumprido")}
    <p class="nota">Cada dia que você viver o seu ritual, pinte a casa.
    Os dias 30, 60 e 90 são checkpoints. Toque numa casa para ir até o dia.</p>
    <div class="mapa">{casas}</div>
    <div class="legenda"><span><i class="lg"></i> ritual feito</span>
    <span><i class="lg meio"></i> feito pela metade</span>
    <span><i class="lg vazio"></i> amanhã eu volto</span></div>
    """
    return pagina(corpo, ancora="mapa")


def rituais_paginas():
    """Uma página por mês, com as linhas dividindo a altura igualmente."""
    por_mes = {}
    for n in range(1, DIAS + 1):
        por_mes.setdefault((dia(n).year, dia(n).month), []).append(n)
    out = []
    for k, ((ano, m), ns) in enumerate(por_mes.items()):
        itens = ""
        for n in ns:
            d = dia(n)
            cp = " cp" if n in (30, 60, 90) else ""
            itens += (f'<li class="{cp.strip()}"><a class="rn" href="#dia-{n}">{n:02d}</a>'
                      f'<span class="rt">{e(RITUAIS[n - 1])}</span>'
                      f'<span class="rd">{SEMANA_CURTA[d.weekday()]} · {d.day:02d}/{d.month:02d}</span>'
                      f'<i class="rc"></i></li>')
        faixa = f"dias {ns[0]:02d} a {ns[-1]:02d}"
        titulo = cabecalho("os rituais de ", MESES[m - 1], faixa)
        corpo = (f'{titulo}<div class="rit-cols rotulo"><span>dia</span><span>ritual</span>'
                 f'<span>data</span><span>feito</span></div>'
                 f'<ol class="rituais" style="grid-template-rows: repeat({len(ns)}, 1fr)">{itens}</ol>')
        out.append(pagina(corpo, ancora="rituais" if k == 0 else None))
    return out


def mes(ano, m):
    primeiro = dt.date(ano, m, 1)
    prox = dt.date(ano + (m == 12), m % 12 + 1, 1)
    celulas = ['<div class="cel vazia"></div>'] * primeiro.weekday()
    d = primeiro
    while d < prox:
        n = (d - INICIO).days + 1
        if 1 <= n <= DIAS:
            tag = f'<a class="dn" href="#dia-{n}">dia {n:02d}</a>'
            cls = "cel desafio"
        else:
            tag, cls = "", "cel"
        celulas.append(f'<div class="{cls}"><span class="num">{d.day}</span>{tag}</div>')
        d += dt.timedelta(1)
    while len(celulas) % 7:
        celulas.append('<div class="cel vazia"></div>')
    cab = "".join(f'<div class="dsem">{s}</div>' for s in SEMANA_LONGA)
    corpo = f"""
    {cabecalho(MESES[m - 1] + " ", "", str(ano))}
    <div class="cal">{cab}{"".join(celulas)}</div>
    <div class="mes-base">
      <div><h3 class="sub">intenção do mês</h3>{linhas(3)}</div>
      <div><h3 class="sub">datas importantes</h3>{linhas(3)}</div>
      <div><h3 class="sub">um momento que quero viver</h3>{linhas(3)}</div>
    </div>"""
    return pagina(corpo, "mensal", ancora=f"mes-{m}")


# ---------------------------------------------------------------- páginas semanais
def planner_semanal(i, s):
    caixas = ""
    for n in s:
        d = dia(n)
        caixas += (f'<div class="dia-box"><div class="db-cab"><span>{SEMANA_LONGA[d.weekday()]}</span>'
                   f'<span class="rotulo">{d.day}/{d.month} · dia {n:02d}</span></div></div>')
    if len(s) < 7:
        caixas += '<div class="dia-box extra"><div class="db-cab"><span>celebrar</span><span class="rotulo">fim do desafio</span></div></div>'
    a, b = dia(s[0]), dia(s[-1])
    corpo = f"""
    {cabecalho("a semana ", "planejada", f"semana {i:02d} · {a.day}/{a.month} – {b.day}/{b.month}")}
    <div class="sem-grid">{caixas}
      <div class="dia-box notas"><div class="db-cab"><span>prioridades</span></div>
        {"".join('<div class="check"><i></i><div class="linha"></div></div>' for _ in range(5))}
      </div>
    </div>
    <div class="sem-base">
      <div><h3 class="sub">o ritual que mais quero viver</h3>{linhas(2)}</div>
      <div><h3 class="sub">notas</h3>{linhas(2)}</div>
    </div>"""
    return pagina(corpo, "semanal", ancora=f"semana-{i}")


def tracker(i, s):
    cab = '<div class="tr-h">hábito</div>' + "".join(
        f'<div class="tr-d">{SEMANA_CURTA[dia(n).weekday()]}<br><small>{dia(n).day}/{dia(n).month}</small></div>'
        for n in s) + '<div class="tr-d">total</div>'
    cols = len(s) + 2
    fila = ""
    for _ in range(12):
        fila += '<div class="tr-nome"><div class="linha"></div></div>' + \
            "".join('<div class="tr-c"><span class="bol"></span></div>' for _ in s) + \
            '<div class="tr-c tot">/' + str(len(s)) + '</div>'
    humor = "".join(f'<div class="hm"><span class="rotulo">{SEMANA_CURTA[dia(n).weekday()]}</span>'
                    f'<div class="hm-bol">{bolinhas(5, "bol peq")}</div></div>' for n in s)
    agua = "".join(f'<div class="hm"><span class="rotulo">{SEMANA_CURTA[dia(n).weekday()]}</span>'
                   f'<div class="hm-bol">{bolinhas(8, "gota")}</div></div>' for n in s)
    corpo = f"""
    {cabecalho("o tracker de ", "hábitos", f"semana {i:02d}")}
    <div class="tracker" style="grid-template-columns: 34% repeat({cols - 1}, 1fr)">{cab}{fila}</div>
    <div class="tr-base">
      <div><h3 class="sub">humor <small>(1 a 5)</small></h3>{humor}</div>
      <div><h3 class="sub">água <small>(copos)</small></h3>{agua}</div>
    </div>
    <h3 class="sub">o que funcionou esta semana</h3>{linhas(3)}
    <h3 class="sub">o que vou ajustar na próxima</h3>{linhas(2)}
    """
    return pagina(corpo, "tracker")


def cardapio(i, s):
    refeicoes = ["café da manhã", "almoço", "jantar", "lanche"]
    cab = '<div class="cd-h"></div>' + "".join(f'<div class="cd-h">{r}</div>' for r in refeicoes)
    fila = ""
    for n in s:
        d = dia(n)
        fila += f'<div class="cd-d">{SEMANA_CURTA[d.weekday()]}<small>{d.day}/{d.month}</small></div>'
        fila += '<div class="cd-c"></div>' * 4
    compras = "".join('<div class="check"><i></i><div class="linha"></div></div>' for _ in range(14))
    corpo = f"""
    {cabecalho("o ", "cardápio", f"semana {i:02d}")}
    <div class="cardapio">{cab}{fila}</div>
    <div class="cd-base">
      <div><h3 class="sub">lista de compras</h3><div class="compras">{compras}</div></div>
      <div><h3 class="sub">preparar com antecedência</h3>{linhas(5)}
        <h3 class="sub">uma receita nova para testar</h3>{linhas(2)}</div>
    </div>"""
    return pagina(corpo, "cardapio")


def bloco_dia(n):
    d = dia(n)
    return f"""
    <div class="bloco-dia" id="dia-{n}">
      <div class="bd-cab">
        <div><span class="bd-num">dia {n:02d}</span><span class="bd-data">{longa(d)}</span></div>
        <div class="bd-humor"><span class="rotulo">humor</span>{bolinhas(5, "bol peq")}</div>
      </div>
      <div class="bd-ritual"><span class="rotulo">ritual de hoje</span>
        <p>{e(RITUAIS[n - 1])}</p><span class="feito"><i></i> feito</span></div>
      <div class="bd-grid">
        <div><span class="rotulo">três pequenas alegrias</span>
          {"".join(f'<div class="num-linha"><span>{k}</span><div class="linha"></div></div>' for k in (1, 2, 3))}</div>
        <div><span class="rotulo">hoje foi bonito porque…</span>{linhas(3)}</div>
      </div>
      <div class="bd-momento"><span class="rotulo">um momento que quero lembrar</span>{linhas(3)}</div>
    </div>"""


def diario(s):
    out = []
    for k in range(0, len(s), 2):
        par = s[k:k + 2]
        corpo = "".join(bloco_dia(n) for n in par)
        out.append(pagina(corpo, "diario"))
        for n in par:
            if n in (30, 60, 90):
                # o checkpoint vem logo depois da página do seu dia
                out.append(checkpoint(n))
    return out


def checkpoint(n):
    perguntas = {
        30: ["O que mudou na minha rotina desde o dia 1?",
             "Qual ritual eu quero repetir para sempre?",
             "O que está difícil — e o que posso ajustar?",
             "Minha intenção para os próximos 30 dias"],
        60: ["Do que eu mais me orgulho até aqui?",
             "Quais hábitos já parecem naturais?",
             "Onde eu estou sendo dura demais comigo?",
             "Como eu quero viver os últimos 30 dias do ano?"],
        90: ["Quem eu era no dia 1 — e quem eu sou hoje?",
             "Os três rituais que vou levar para 2027",
             "O que eu aprendi sobre mim",
             "Como eu vou celebrar este fechamento?"],
    }[n]
    blocos = "".join(f'<p class="pergunta">{e(p)}</p>{linhas(4)}' for p in perguntas)
    corpo = f"""
    {cabecalho("checkpoint ", f"dia {n}", longa(dia(n)))}
    <div class="cp-nota"><span class="rotulo">de 0 a 10, como estou me sentindo?</span>
      <div class="escala">{"".join(f"<span>{k}</span>" for k in range(11))}</div></div>
    {blocos}"""
    return pagina(corpo, "checkpoint", ancora=f"checkpoint-{n}")


def carta_final():
    corpo = f"""
    {cabecalho("uma carta para ", "2027", "para ler em janeiro")}
    <p class="nota">Escreva para a pessoa que você vai ser no próximo ano.
    Conte o que você viveu nestes 90 dias e o que você não quer esquecer.</p>
    <div class="carta">{linhas(22)}</div>
    <p class="fecho">Você fez 90 dias de vida bonita. <em>Continue.</em></p>"""
    return pagina(corpo, "final", ancora="carta-final")


# ---------------------------------------------------------------- montagem
def montar():
    paginas = [capa(), sumario(), boas_vindas(), intencoes(), mapa()]
    paginas += rituais_paginas()
    for m in sorted({dia(n).month for n in range(1, DIAS + 1)}):
        paginas.append(mes(INICIO.year, m))
    for i, s in enumerate(SEMANAS, 1):
        paginas += [planner_semanal(i, s), tracker(i, s), cardapio(i, s)]
        paginas += diario(s)
    paginas.append(carta_final())
    css = open(os.path.join(AQUI, "style.css"), encoding="utf-8").read()
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>{e(TITULO)}</title>
<link rel="stylesheet" href="../assets/fonts/fonts.css">
<style>{css}</style></head><body>{"".join(paginas)}</body></html>""", len(paginas)


def main():
    os.makedirs(DIST, exist_ok=True)
    doc, total = montar()
    html_path = os.path.join(AQUI, "workbook.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(doc)
    pdf = os.path.join(DIST, "90-dias-de-vida-bonita.pdf")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=10000",
                    f"--print-to-pdf={pdf}", "file://" + html_path],
                   check=True, capture_output=True)
    print(f"{total} páginas -> {pdf}")


if __name__ == "__main__":
    main()
