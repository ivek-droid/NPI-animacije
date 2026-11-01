INK='#1b1e28'; P='#4b1585'; PD='#36105f'; A='#f2b705'; SKIN='#f3c9a5'; SKIN_D='#e0a982'; W='#ffffff'
def character(think=True):
    s=[]
    # telo (delovna jakna)
    s.append(f'<path d="M48 240 C52 196 78 182 120 182 C162 182 188 196 192 240 Z" fill="{P}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    # ovratnik
    s.append(f'<path d="M100 184 L120 206 L140 184" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    # žep z izvijačem
    s.append(f'<rect x="146" y="206" width="26" height="22" rx="4" fill="{PD}" stroke="{INK}" stroke-width="4"/>')
    s.append(f'<rect x="153" y="190" width="9" height="20" rx="3" fill="{A}" stroke="{INK}" stroke-width="3.5"/>')
    # vrat
    s.append(f'<path d="M104 160 L104 186 Q120 194 136 186 L136 160 Z" fill="{SKIN_D}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    # ušesa
    s.append(f'<ellipse cx="72" cy="128" rx="10" ry="14" fill="{SKIN}" stroke="{INK}" stroke-width="5"/>')
    s.append(f'<ellipse cx="168" cy="128" rx="10" ry="14" fill="{SKIN}" stroke="{INK}" stroke-width="5"/>')
    # glava
    s.append(f'<path d="M74 108 C74 82 94 70 120 70 C146 70 166 82 166 108 L166 132 C166 160 146 176 120 176 C94 176 74 160 74 132 Z" fill="{SKIN}" stroke="{INK}" stroke-width="5"/>')
    # čelada
    s.append(f'<path d="M70 104 C70 62 92 44 120 44 C148 44 170 62 170 104 Z" fill="{A}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    s.append(f'<path d="M58 104 L182 104 Q186 112 178 114 L62 114 Q54 112 58 104 Z" fill="{A}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    s.append(f'<path d="M120 46 L120 102" stroke="{INK}" stroke-width="4"/>')
    s.append(f'<path d="M104 50 Q100 76 102 102 M136 50 Q140 76 138 102" fill="none" stroke="{INK}" stroke-width="3" opacity=".5"/>')
    # obrvi (ena dvignjena)
    s.append(f'<path d="M92 126 Q100 120 108 124" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    s.append(f'<path d="M132 120 Q141 113 150 118" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    # oči – gledajo gor desno
    s.append(f'<ellipse cx="101" cy="136" rx="8" ry="9" fill="{W}" stroke="{INK}" stroke-width="3.5"/><circle cx="104" cy="132" r="4.2" fill="{INK}"/>')
    s.append(f'<ellipse cx="140" cy="134" rx="8" ry="9" fill="{W}" stroke="{INK}" stroke-width="3.5"/><circle cx="143" cy="130" r="4.2" fill="{INK}"/>')
    # nos
    s.append(f'<path d="M121 140 Q116 152 124 153" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    # usta "hmm"
    s.append(f'<path d="M110 164 Q120 160 132 165" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>')
    # roka pod brado
    s.append(f'<path d="M84 240 L96 196 Q100 186 110 188" fill="{P}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    s.append(f'<path d="M98 194 C96 178 106 168 120 170 C132 171 136 180 132 188 C128 196 112 200 104 198 Z" fill="{SKIN}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')
    s.append(f'<path d="M110 180 Q118 178 126 181" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
    if think:
        s.append(f'<circle cx="180" cy="72" r="6" fill="{W}" stroke="{INK}" stroke-width="4"/>')
        s.append(f'<circle cx="194" cy="52" r="9" fill="{W}" stroke="{INK}" stroke-width="4"/>')
        # oblaček
        s.append(f'<path d="M200 36 C192 22 206 6 222 12 C228 -2 252 -2 258 12 C274 8 286 24 278 38 C290 48 280 66 264 62 C258 76 234 76 228 64 C212 70 198 56 204 46 C196 44 196 38 200 36 Z" fill="{W}" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round" transform="translate(0 4)"/>')
        # simbol svetilke (prižgan)
        s.append(f'<circle cx="240" cy="40" r="17" fill="{A}" stroke="{P}" stroke-width="4.5"/>')
        s.append(f'<path d="M229 29 L251 51 M251 29 L229 51" stroke="{P}" stroke-width="4.5" stroke-linecap="round"/>')
    return ''.join(s)
