def issamenetwork(ipa:str, ipb:str):
    if not isinstance(ipa, str): raise TypeError("ipa must be a string of the form : a.b.c.d/m")
    if not isinstance(ipb, str): raise TypeError("ipb must be a string of the form : a.b.c.d/m")

    try:
        ipa, ipb = ipa.replace("\\", "/"), ipb.replace("\\", "/")
        ipa, ipb = ipa.strip(), ipb.strip()

        ipa, maska = ipa.split("/")
        ipb, maskb = ipb.split("/")

        ipa_liste, ipb_liste = [int(ipa.split(".")[i]) for i in range(4)], [int(ipb.split(".")[i]) for i in range(4)]

        print(ipa_liste, ipb_liste)

        if maska != maskb: return False

        maska, maskb = int(maska),int(maskb)
        maska = sum([2**i for i in range(31, 31-maska, -1)])
        maskb = sum([2**i for i in range(31, 31-maskb, -1)])

        ipa = (ipa_liste[0] * 16**3) + (ipa_liste[1] * 16**2) + (ipa_liste[2] * 16**1) + (ipa_liste[3] * 16**0)
        ipb = (ipb_liste[0] * 16**3) + (ipb_liste[1] * 16**2) + (ipb_liste[2] * 16**1) + (ipb_liste[3] * 16**0)

        return ipa & maska == ipb & maskb
    except: raise SyntaxError("The ips must be strings of the form : a.b.c.d/m")

if __name__ == "__main__":
    print(issamenetwork("192.168.1.1/16", "192.168.2.1/16"))