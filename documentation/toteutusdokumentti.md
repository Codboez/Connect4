# Toteutusdokumentti
## Ohjelman yleisrakenne
Ohjelman rakenne on jaettu käyttöliittymään ja sovelluslogiikkaan siten, että käyttöliittymä on riippuvainen sovelluslogiikasta.
#### Käyttöliittymä
Sovelluksessa on graafinen käyttöliittymä. Käyttöliittymässä on kolme pääluokkaa:
* Game: Hallitsee pelisilmukkaa, ikkunaa, ja renderöintiä.
* BoardUI: Vastuussa pelilaudan piirtämisestä näytölle.
* Visualizer: Visualisoi teköälyn toimintaa piirtämällä minimax algoritmin käyttämän puun tekoälyn toiminnan mukaisesti.

#### Sovelluslogiikka
Sovelluslogiikassa on neljä pääluokkaa.
* AI: Tekoäly, jota vastaan voi pelata.
* GameState: Huolehtii tekoälyn käyttämän pelitilanteiden arvioinnista.
* Manager: Huolehtii, että vuoro annetaan pelaajalle tai tekoälylle toisen pelaajan vuoron päätyttyä.
* Board: Vastuussa pelilaudan käytöstä.

## Tekoälyn aika- ja tilavaativuudet
* Aikavaativuus: Saavutettu aikavaativuus on O(n^k), missä k on puun syvyys ja n mahdollisten siirtojen määrä kullakin hetkellä, mutta toteutettujen optimaatioiden avulla päästään usein paljon parempaan aikavaativuuteen.
* Tilavaativuus: Saavutettu tilavaativuus on O(nk)

## Puutteet ja parannusehdotukset
Käyttöliittymää voisi parantaa esimerkiksi siten, että siitä voisi aloittaa uusia pelejä tai, että tekoälyn vaikeustasoa voisi muuttaa (syvyyden avulla).

## Laajojen kielimallien käyttö
En ole käyttänyt mitään laajoja kielimalleja.
