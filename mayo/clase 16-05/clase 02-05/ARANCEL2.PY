desc=0
arancel=200000
comuna=(int(input("en que comuna vive \n1-la florida   2-pintana \n3-puente alto    4-san joaquin")))
if comuna==1:    
    desc+=0.2
elif comuna==2:
    desc+=0.3
elif comuna==3:
    desc+=0.25
elif comuna==4:
    desc+=0.15
np=int(input("cuantas personas hay"))
if np==1:
        desc+=0.01
        print(f"su descuento es de %{desc} \n usted debe pagar {arancel-arancel*desc} de arancel")
elif np>1 and np<5:
        desc+=0.03
        print(f"su descuento es de {desc} \n usted debe pagar {arancel-arancel*desc} de arancel")
else:
        desc+=0.04
        print(f"su descuento es de {desc} \n usted debe pagar {arancel-arancel*desc} de arancel")