# Függvény, amely egy sor szöveget készít a diagramhoz adott nap és hőmérséklet alapján
def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)              # Átalakítja a hőmérsékletet egész számmá, ez lesz a csillagok száma
    csillagok = '*' * csillagok_szama               # Ennyi darab '*' karaktert készít
    sor = f"{nap_szama:>2}. nap: {csillagok} ({homerseklet}°C)"  # Sor formázása, nap száma, csillagok és hőmérséklet kiírásával
    return sor                                       # Visszatér az elkészített sorral

# Függvény, amely kiírja a diagramot a konzolra
def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérsékletek diagram (°C)")    # Címsor kiírása
    print("-" * 40)                                  # Vízszintes elválasztó vonal

    for i in range(len(homersekletek)):              # Végigmegy az összes hőmérsékleten
        nap = i + 1                                   # A nap sorszáma (1-től kezdve)
        sor = keszit_diagram_sort(nap, homersekletek[i])  # Diagram sor elkészítése adott naphoz
        print(sor)                                    # A sor kiírása

# Minta hőmérséklet adatok: egyheti átlaghőmérséklet Celsius-fokban
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

# A diagram kiíratása a konzolra
rajzolj_diagram(napi_atlaghomersekletek)
