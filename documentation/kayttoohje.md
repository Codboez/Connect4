# Käyttöohje
## Ohjelman käynnistys
1. Asenna projektin riippuvuudet komennolla
```
poetry install
```
2. Käynnistä ohjelma pakettina komennolla
```
poetry run python -m src
```

## Ohjelman käyttö
Ohjelman käyttö on erittäin helppoa. Pelaat Connect Four peliä ohjaamalla keltaista pelaajaa. Aluksi on sinun vuorosi. Kun on sinun vuorosi, tiputa kolikko yhteen sarakkeista painamalla hiiren vasenta näppäintä, kun hiiresi leijuu sarakkeen yläpuolella. Siinä kaikki.

## Connect Four pelin säännöt
Kaksi pelaajaa tiputtavat vuorotellen kolikoita yhteen sarakkeista. Peli päättyy, kun jompikumpi pelaajista on saanut neljä peräkkäistä oman väristä kolikkoa riviin. Rivi voidaan tehdä vaaka-, pysty- tai vinottaissuuntaisesti. Ensimmäinen pelaaja, joka saa neljä kolikkoa riviin voittaa pelin.
