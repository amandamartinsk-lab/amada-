# 90 Dias de Vida Bonita: kit de vendas

Produto: workbook digital em PDF (A4, 105 páginas, com links internos), para imprimir ou usar no GoodNotes, Notability ou no computador.
Arquivo: `workbook/dist/90-dias-de-vida-bonita.pdf`
Imagens para o anúncio: `workbook/dist/previews/`

---

## 1. O que vem no caderno (confira no PDF)

| Seção | Páginas |
|---|---|
| Capa, sumário com links, boas-vindas e "como usar" | 3 |
| Minhas intenções (quem eu quero ser em 31/12) | 1 |
| Mapa dos 90 dias (pintar cada dia cumprido) | 1 |
| Os 90 rituais, um por dia, com data (uma página por mês) | 3 |
| Calendários de outubro, novembro e dezembro | 3 |
| 13 semanas, cada uma com planner semanal, tracker de hábitos e cardápio com lista de compras | 39 |
| Diário de 90 dias (2 dias por página, com o ritual do dia) | 45 |
| Checkpoints nos dias 30, 60 e 90 | 3 |
| Carta para 2027 | 1 |

Datas: dia 1 = sábado, 3 de outubro de 2026. Dia 90 = quinta, 31 de dezembro de 2026.

---

## 2. Página de vendas (texto pronto)

**Título:** Não espere janeiro. Chegue em 2027 já vivendo a vida que você quer.

**Subtítulo:** Um desafio de 90 dias para romantizar a sua rotina. Começa em 3 de outubro e termina exatamente em 31 de dezembro.

**Texto:**
Todo ano é igual: a gente promete que em janeiro vai ser diferente. E se, dessa vez, você chegasse em janeiro já diferente?

*90 Dias de Vida Bonita* é um caderno digital que te guia, dia após dia, até o fim do ano. Não tem dieta nem rotina impossível. São pequenos rituais, como tomar café sem o celular, pôr a mesa para uma refeição comum ou caminhar sem fones, que deixam os seus dias mais bonitos.

**Você recebe:**
- 90 rituais diários, um para cada dia do desafio
- Diário guiado com "três pequenas alegrias" e "hoje foi bonito porque…"
- Planner semanal, tracker de hábitos e cardápio com lista de compras para as 13 semanas
- Calendários de outubro, novembro e dezembro já com as datas
- Checkpoints nos dias 30, 60 e 90 para ajustar a rota
- Mapa visual dos 90 dias e carta para você mesma em 2027
- PDF com links: toque e navegue no iPad ou no celular. Se preferir, imprima.

**Para quem é:** para quem sente que o ano passou rápido demais e quer terminar 2026 com mais presença, mais cuidado e menos culpa.

**Perguntas frequentes**
- *Comprei depois de 3 de outubro. E agora?* Comece no dia de hoje. O desafio é sobre voltar, não sobre ser perfeita.
- *É físico?* Não. É um PDF enviado na hora, por e-mail.
- *Posso imprimir?* Sim, em A4. Imprima tudo ou só as páginas que quiser.
- *Funciona no GoodNotes?* Sim. Importe o PDF, e os links do sumário e do mapa funcionam.

---

## 3. Plano dos seus 100 dias (29/09/2026 a 07/01/2027)

| Fase | Datas | O que fazer |
|---|---|---|
| Pré-lançamento | 29/09 – 02/10 | Cadastrar o produto na plataforma. Postar os bastidores ("estou criando algo para a gente terminar o ano bem"). Montar uma lista de espera pelo direct. |
| Lançamento | 03/10 – 10/10 | Abrir as vendas no dia 1. Postar o seu próprio "dia 01" usando o caderno. |
| Vender durante o desafio | 11/10 – 30/11 | Mostrar o seu uso real: um ritual por dia nos stories. Vender com o gancho "entre agora, ainda dá tempo". |
| Presente de Natal | 01/12 – 24/12 | Posicionar o caderno como presente digital para uma amiga. |
| Relançamento de Ano Novo | 26/12 – 07/01 | Gerar a edição 2027 (ver seção 5) e vender como "90 dias para começar o ano". |

---

## 4. Legendas prontas (Instagram / TikTok)

1. Todo mundo espera janeiro para mudar. Eu vou começar dia 3 de outubro, e são exatamente 90 dias até o fim do ano. Vem comigo?
2. Dia 01: arrumar a cama como se fosse de hotel. Parece bobo, mas muda o seu dia inteiro.
3. Romantizar a vida não é fingir que está tudo perfeito. É escolher prestar atenção.
4. 90 rituais pequenos, um por dia. Nenhum leva mais de 30 minutos.
5. POV: você chega em 31 de dezembro sem aquela sensação de que o ano passou e você não viveu.
6. Tour pelo caderno: planner semanal, tracker de hábitos, cardápio e diário, tudo num PDF só.
7. Ainda dá tempo. Comece hoje e pule os dias que já passaram. O desafio é sobre voltar.
8. Checkpoint do dia 30: o que mudou na minha rotina em um mês. (Mostre a sua página.)
9. Presente de Natal que chega na hora, por e-mail: 90 dias de vida bonita para quem você ama.
10. Não deixe tudo para 2027. Começa hoje.

---

## 5. Como editar o caderno

O caderno é gerado pelo script `workbook/build.py`:
- **Marca:** troque `MARCA = "AMADA"` pelo nome da sua marca.
- **Nova edição (ex.: janeiro de 2027):** troque `INICIO = dt.date(2026, 10, 3)` pela nova data. Todas as datas, calendários e semanas se recalculam. Revise os rituais de datas especiais (dias 83 e 84 = véspera e dia de Natal) em `workbook/content.py`.
- **Textos dos rituais:** `workbook/content.py`.
- Depois rode `python3 workbook/build.py`.

---

## 6. O que eu não sei (decida você)

- **Preço:** R$ 27 (definido por você). Pagamento único.
- **Plataforma:** Hotmart e Kiwify entregam o PDF automaticamente. A Etsy alcança compradoras fora do Brasil, mas aí o produto precisaria de uma versão em inglês.
- **Registro de marca:** "AMADA" foi um nome provisório que eu escolhi a partir do nome do seu repositório. Confirme se o nome está livre antes de usar.
