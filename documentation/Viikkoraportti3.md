# Viikkoraportti 3
Tämän viikon aikana sain tehtyä Minimax algoritmille pelitilanteiden hyvyyden arvioinnin alustavasti valmiiksi. Tämän on kuitenkin vielä puutteellinen, sillä se etsii pelkästään 4 pituisia jonoja. Tämän vuoksi teköäly saa tulokseksi usein samoja arvoja eri sarakkeille, eikä teköäly siis löydä kaikista parhaimpia ratkaisuja, vaan ottaa samanarvoisista vasemmanpuoleisen. Teköäly osaa kuitenkin arvioida varmasti voittavia ja varmasti häviäviä siirtoja ja pelata niiden mukaan.

Tämän lisäksi alpha-beta karsinta on tehty valmiiksi. Alpha-beta karsinta näyttää toimivan oikein (suuri suorituskyvyn parannus), mutta sitä ei ole vielä testattu. Teköälyä ja sen käyttämiä pelilaudan metodeja on yksikkötestattu. Näiden lisäksi suuri osa tämän viikon ajasta on käytetty Minimaxin bugien korjaamiseen.

Tutustuin tällä viikolla tarkemmin alpha-beta karsintaan ja sen toteutukseen, ja opin soveltemaan sitä Connect Four peliin.

Seuraavaksi aion parantaa aiemmin mainittua pelitilanteiden hyvyyden arviointia etsimään myös 3 pituisia rivejä (mahdollisesti myös 2 pituisia rivejä). Aion myös tehdä lisää testejä tekoälylle, ja tehdä suorituskykytestejä alpha-beta karsinnalle. Näiden lisäksi voin myös aloittaa kahta viimeistä puuttuvaa optimaatiota (iteratiivinen syveneminen, siirtojen järjestäminen).

Tämän viikon aikana käytin noin 17 tuntia.
