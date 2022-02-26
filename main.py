'''
3. Feladat
A megadott halmazok alapján a program értékelje ki, és az eredményt jelenítse meg a képernyőn az alábbiakat vizsgálva:
- hány olyan étel van, amit mind a két gyerek szeret, és melyek ezek,
- melyek azok az ételek, amiket Peti szeret, de Kriszti nem,
- melyek azok az ételek, melyeket csak egyikük szeret!
'''
Peti_kedvencei = {'halászlé', 'bécsi szelet', 'bukta', 'rakott krumpli', 'almás rétes' }

Kriszti_kedvencei = {'borsóleves', 'bécsi szelet', 'túrós tészta', 'lecsó', 'almás rétes' }

mindketto = set(Peti_kedvencei & Kriszti_kedvencei)

print(f'Ennyi ételt szeretnek mindketten: {len(mindketto)}')
print(f'Mindkettelyük szereti: {mindketto}')

print()

csakpeti = set(Peti_kedvencei ^ Kriszti_kedvencei)

csakkriszti = set(Kriszti_kedvencei ^ Peti_kedvencei)

print(f'Ennyi ételt szeret Peti, de Kriszti nem: {len(csakpeti)}')
print(f'Csak Peti szereti: {csakpeti}')

print()

unio = set(csakpeti | csakkriszti)
print(f'Ennyi ételt nem szeret egyikük sem: {len(unio)}')
print(f'Ételek melyeket nem szeret egyikük sem: {unio}')
'''
# metszet
    print(reggeli & ebed)
    # unio
    print(reggeli | ebed)
    # különbség
    print(reggeli - ebed)
    # csak az egyikben, vagy csak a másikban
    print(reggeli ^ ebed)
'''