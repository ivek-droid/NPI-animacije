"""Smiselni prelomi v rešenih primerih (ol.pg-koraki): z nelomljivimi presledki (U+00A0) veže
število z enoto, operatorje z operandi, »tabela 4«, »1. pogoj«, kljukico s številom.
Prelom ostane možen za relacijskimi znaki (=, ≤, ≥, <, >), za ločili in med besedami.
Idempotentno. Uporaba: python3 orodja/koraki_nbsp.py slog/osnutki/*.txt  (piše datoteke na mestu)
Ob vsakem pisanju osnutka ga samodejno pokliče write() v lekcije_pomocniki_in_ivep.py."""
import re, sys
N = ' '
UNITS = r'(?:mm²|kWh|kW|VA|Hz|°C|mm|W|A|V|Ω|m|s|h)'

def nb_text(t):
    t = re.sub(r'(?<=\d) (?=\d{3}(?!\d))', N, t)                       # 38 000
    t = re.sub(r'(?<=\d) (?=' + UNITS + r'(?![\w²]))', N, t)             # 63 A, 16 mm²
    t = re.sub(r'\b(tabela|tabeli|Tabela|način|Način) (?=[\dA-Z])', r'\1' + N, t)
    t = re.sub(r'(?<=\b\d\.) (?=pogoj)', N, t)                          # 1. pogoj
    t = re.sub(r' ([·/+−×÷]) ', N + r'\1' + N, t)                       # operatorji vezani na obe strani
    t = re.sub(r' (=|≤|≥|&lt;|&gt;|≈|≠|→) ', N + r'\1 ', t)             # prelom šele za relacijo
    t = re.sub(r' ([✓✗✔✘])', N + r'\1', t)
    return t

def nb_html(h):
    return ''.join(p if p.startswith('<') else nb_text(p) for p in re.split(r'(<[^>]+>)', h))

def nb_koraki(doc):
    return re.sub(r'(<ol class="pg-koraki">)(.*?)(</ol>)', lambda m: m.group(1) + nb_html(m.group(2)) + m.group(3), doc, flags=re.S)

if __name__ == '__main__':
    for p in sys.argv[1:]:
        s = open(p, encoding='utf-8').read(); n = nb_koraki(s)
        if n != s: open(p, 'w', encoding='utf-8').write(n); print('popravljeno', p)
