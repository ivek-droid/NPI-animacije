# Generator: LEGO programiranje, uvodna stran
exec(open('/home/claude/npi-animacije/orodja/lekcije_pomocniki_in_ivep.py').read())
L = 'https://npi.splet.arnes.si/'
kaj = H2 + 'Kaj potrebuješ</h2>\n' + ul([
    'robota LEGO EV3: vozilo z dvema motorjema,',
    'računalnik s programom EV3 Classroom (vmesnik je v angleščini),',
    'merilni trak in lepilni trak.'])
robot = H2 + 'Kje je kaj priključeno</h2>\n' + ul([
    'levi motor: vrata <strong>B</strong>, desni motor: vrata <strong>C</strong>,',
    'vrata <strong>1</strong>: senzor dotika, vrata <strong>2</strong>: žiroskop,',
    'vrata <strong>3</strong>: barvni senzor, vrata <strong>4</strong>: ultrazvočni senzor.']) + '\n<p>Ko je robot povezan, so vrednosti na vseh vratih vidne v vrstici na vrhu programa.</p>'
kako = H2 + 'Kako delaš</h2>\n' + ol([
    'Preberi vajo.',
    'Sestavi program v EV3 Classroom.',
    'Preizkusi program na robotu in izmeri, kaj je naredil.',
    'Popravi program in reši »Preveri se«.']) + '\n' + box('primer', 'Robot je samo eden', '<p style="margin-top:0">Program najprej pripravi na računalniku in ga preizkusi v animaciji. Na robotu preizkusiš šele potem. Tako je čakanje krajše.</p>', '16px 0 0')
vaje = H2 + 'Vaje</h2>\n' + ul([
    f'Vaja 1: <a href="{L}lego-spoznaj-robota/">Spoznaj robota in program</a>',
    f'Vaja 2: <a href="{L}lego-voznja-naravnost/">Vožnja naravnost</a>',
    f'Vaja 3: <a href="{L}lego-zavoji/">Zavoji</a>',
    'Vaja 4: Ponavljanje (pripravljamo)',
    'Vaja 5: Zvok, zaslon in lučka (pripravljamo)',
    'Vaja 6: Senzor dotika (pripravljamo)',
    'Vaja 7: Barvni senzor (pripravljamo)',
    'Vaja 8: Ultrazvočni senzor (pripravljamo)',
    'Vaja 9: Končni izziv (pripravljamo)'])
out = sec(
    row(col('4_4', text(cilj('LEGO programiranje', ['sestaviti blokovni program v EV3 Classroom,', 'prenesti program na robota in ga preizkusiti,', 'izmeriti, kaj je robot naredil, in program popraviti.']))))
  + row(col('1_2', text(kaj) + text(robot)) + col('1_2', text(kako)), '1_2,1_2')
  + row(col('4_4', text(vaje))))
write('lego-uvod', out)
