ombrellone = float(12)
lettino = float(5)
sdraio = float(6.50)

ngiorni = input("Inserisci il numero di giorni: ")
nombrelloni = input("Inserisci il numero di ombrelloni che vuoi prenotare: ")
nlettini = input("Inserisci il numero di lettini che vuoi prenotare: ")
nsdraio = input("Inserisci il numero di sdraio che vuoi prenotare: ")

ngiorni = int(ngiorni)
nombrelloni = float(nombrelloni)
nlettini = float(nlettini)
nsdraio = float(nsdraio)

costo = (ombrellone * nombrelloni + lettino * nlettini + sdraio + nsdraio)*ngiorni

costo = float(costo)

print(f"Il costo totale è di: {costo}€")
