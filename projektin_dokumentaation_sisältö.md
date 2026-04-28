# Projektin dokumentaation sisältö GitHub:ssa
Tässä on ehdotus projektin dokumentaation sisällöstä, joka auttaa käyttäjiä ja kehittäjiä ymmärtämään projektin tarkoituksen, asennuksen, käytön ja ylläpidon.

## 1. README.md
- **README.md** on yleensä ensimmäinen tiedosto, jonka käyttäjät näkevät projektin GitHub-repossa.
- sen alaotsikoita:
  ### Projektin nimi
  Lyhyt kuvaus projektista: mitä ohjelma tekee ja miksi se on hyödyllinen

  ### Asennus
  Ohjeet riippuvuuksien asentamiseen ja projektin käynnistämiseen. Miten ympäristö pystytetään.
  Esim. Python-projektissa riippuvuuksien asentaminen (````pip install -r requirements.txt````).<br>

  Viittaus **requirements.txt**-tiedostoon. Esimerkkikomennot, miten ohjelma käynnistetään.

  ### Käyttö
  Esimerkkejä siitä, miten ohjelmaa käytetään. Esim:
  - Komentoriviesimerkkejä:
    ```bash
    #Käynnistä ohjelma näin:
    python main.py --option value
    ```
  - Jos ohjelma käyttää CLI:tä voisi siinä lukea näin:
    ```bash
    mytool --help
    mytool run --input data.csv
    ````
  - voit selittää parametrejä ja asetuksia:
    ```bash
    #Esim. parametrit:
    --input: syötetiedosto
    --output: tulostiedosto
    --verbose: lisää tulostusta
    ```

  - Selitä tärkeimmät komennot ja niiden parametrit.
  - Kuvakaappauksia käyttöliittymästä tai tuloksista.
    - Lyhyt kuvaus tärkeimmistä toiminnoista.
    - Linkit lisädokumentaatioon, jos tarpeen.
    - Ohjeet konfigurointitiedoston (config.ini) muokkaamiseen.
    - Käyttöesimerkkejä.
    - Yleiset virheilmoitukset ja niiden ratkaisut.
    - FAQ-osio.
    - Ohjeet, miten käyttäjät voivat raportoida ongelmia tai ehdottaa parannuksia (esim. GitHub Issues).
    - Ohjeet, miten käyttäjät voivat osallistua projektiin (esim. CONTRIBUTING.md).
  
   - tai sitten pitempi esimerkki:
     
     ```
     ## Ohjelman käyttö
     1 #Kun olet asentanut riippuvuudet, voit ajaa ohjelman näin:
     2
     3 python main.py --input data.csv --output result.json```


  ### Arkkitehtuuri
  Lyhyt kuvaus ohjelman rakenteesta ja komponenteista.<br>
  esim. mitä osia ohjelmassa on: Python-skripti + nettisivu

  ### Lisenssi
    Tiedot ohjelman lisenssistä.
    
    esim.:
    ```
    ## Lisenssi
    Tämä projekti on lisensoitu MIT-lisenssillä. Katso LICENSE-tiedosto lisätiedoista.
    ```

  ### Yhteystiedot
    Kuka on projektin ylläpitäjä tai kehittäjä.
  
  ### Lisätiedot
    Linkit lisädokumentaatioon.


## 2. requirements.txt
- Lista kaikista riippuvuuksista ja niiden versioista.
- Tiedoston nimi on yleensä **requirements.txt**.
- "Riippuvuudet" tarkoittaa ohjelmistokehityksessä kirjastoja, paketteja tai muita ohjelmia, joita projektisi tarvitsee toimiakseen oikein.
- Esimerkiksi Python-projektissa riippuvuudet voivat olla:
  - Ulkoisia kirjastoja (esim. NumPy, Pandas, APScheduler), jotka asennetaan pip-komennolla.
  - Tietokantayhteyksiä (esim. MariaDB), jos ohjelma tallentaa dataa.
  - Konfiguraatiotiedostoja tai muita resursseja, joita ohjelma käyttää.
- Ne listataan yleensä tiedostossa requirements.txt, jotta kuka tahansa voi asentaa ne yhdellä komennolla:
```pip install -r requirements.txt```<br>
esimerkkisisältö:

```APScheduler==3.6.3
Flask==1.1.2
mysql-connector-python==8.0.23
requests==2.24.0
```
tuo tarkoittaa, että projekti tarvitsee seuraavat riippuvuudet(ohjelmat ym. ) ja versiot toimiakseen oikein:
* APSchedulerin version 3.6.3 tai uudempaa, 
* Flaskin version 1.1.2 tai uudempaa, 
* mysql-connector-pythonin version 8.0.23 tai uudempaa, ja 
* requestsin version 2.24.0 tai uudempaa


## 3. LICENSE
- tiedoston nimi isolla kirjaimilla LICENSE tai LICENSE.txt
- tiedoston sisältönä on ainoastaan lisenssi, ei muuta tekstiä.

- Valitse avoimen lähdekoodin lisenssi (esim. MIT, GPL, Apache 2.0). Tämä on tärkeää, jos jaat koodin julkisesti.
- Ohjelman lisenssi kannattaa kuvata selkeästi niin, että lukija ymmärtää mitä saa tehdä ja mitä ei saa tehdä koodilla. Yleensä tämä tehdään lisäämällä LICENSE-tiedosto GitHub-repoon ja mainitsemalla lisenssi myös README.md:ssä.
- Hyvä käytäntö lisenssin kuvaamiseen:
  - Valitse lisenssi. Yleisimmät avoimen lähdekoodin lisenssit:
    - MIT – hyvin salliva, saa käyttää, muokata ja jakaa, kunhan alkuperäinen tekijä mainitaan.
    - Apache 2.0 – salliva, mutta sisältää patenttisuojausta.
    - GPL v3 – vaatii, että johdannaiset projektit pysyvät avoimina.
  - Jos projekti on sisäiseen käyttöön, voit käyttää proprietary-merkintää tai yrityksen omaa lisenssiä.
 - Lisää LICENSE-tiedosto: Kopioi valitun lisenssin virallinen teksti (esim. MIT-lisenssi löytyy https://opensource.org/licenses/MIT).

## 4. CONTRIBUTING.md

Ohjeet, miten muut voivat osallistua projektiin.
Koodityyli, pull request -käytännöt, bugiraportointi.


## 5. CONFIGURATION-ohjeet

Selitä config.ini-tiedoston rakenne ja merkitys.
Kerro, mitä asetuksia voi muuttaa (esim. näytteenottoväli, raja-arvot).


## 6. Käyttöesimerkit

Esimerkkikoodia tai kuvakaappauksia Grafana-näkymästä.
Näytä, miltä tulokset näyttävät.


## 7. Dokumentaatio funktioista

Voit käyttää docstringejä koodissa ja generoida niistä dokumentaation (esim. Sphinx tai MkDocs).
Selitä tärkeimmät funktiot ja luokat.

Docstring-esimerkki Pythonissa (tähän oppaaseen liittyvät kommentit hakasulkeissa):
```python
def laske_summa(a, b):                  [funktion nimi ja parametrit]
    """                                 [käytä triple-quote merkkijonoa docstringissä]
    Laskee kahden luvun summan.         [tyhjä rivi]
    Args:                               [parametrit-osio]
        a (int): Ensimmäinen luku.      [parametri ja sen tyyppi, poikkeukset]
        b (int): Toinen luku.           [parametri ja sen tyyppi, poikkeukset]
                                        [tyhjä rivi]
    Returns:                            [palautusarvon kuvaus]
        int: Lukujen summa.             [palautusarvon tyyppi ja merkitys]
    """                                 [lopeta docstring]
    return a + b                        [funktion toteutus]
```
käytä triple-quote merkkijonoa docstringissä.

Lisää docstringistä: 
* https://peps.python.org/pep-0257/
* https://www.geeksforgeeks.org/python/python-docstrings/
* https://realpython.com/documenting-python-code/

## 8. CHANGELOG.md

Versiohistoria ja muutokset (helpottaa ylläpitoa).
Käytä selkeää rakennetta, esim. Keep a Changelog -tyyliä.

```
# Changelog
Kaikki merkittävät muutokset tähän projektiin dokumentoidaan tässä tiedostossa.

## [1.2.0] - 2025-11-27
 ### Lisätty
- Uusi ominaisuus X
### Korjattu
- Bugikorjaus Y
### Muutettu
- Päivitetty dokument
```

Älä dumppaa gitin logia tähän, vaan kirjoita tiivistetysti tärkeimmät muutokset.
käytä semanttista versionumeroa (MAJOR.MINOR.PATCH).

Pienessä projektissa voit lisätä CHANGELOGin myös README.md:hen.
```
## Versiohistoria
  * v1.2.0 (2025-11-27)**: Lisätty ominaisuus X, korjattu bugi Y.
  * v1.1.0 (2025-10-10)**: Parannettu suorituskykyä
  * v1.0.0 (2025-09-01)**: Ensimmäinen julkaisu
```
GitHub Releases

Luo tagit ja julkaisut GitHubissa jokaiselle versiolle.<br>
Lisää julkaisuun release notes, jotka kuvaavat muutokset.<br>
Tämä on hyvä tapa yhdistää automaattinen versiohallinta ja dokumentointi, mutta UX voi olla hankala pelkästään Releases-sivun kautta

* Työkalut ja automaatio
  * Versioiden kirjaamisen automaation voi hoitaa esim. GitHub Actionsilla tai muulla CI/CD-työkalulla. 
  * GitHub Changelog Generator: Luo changelogin tageista, PR:istä ja issueista.

## 9. Issues & Wiki
GitHubin omat työkalut: Wiki lisätietoon, Issues bugiraportointiin.
 
* GitHub Wiki
  * **Mikä se on?** Wiki on erillinen dokumentaatioalue GitHub-repositoriossa, jossa voit kirjoittaa laajempia ohjeita, oppaita ja projektin taustatietoja.
  * **Mihin sitä käytetään?** Käyttöohjeet ja tutoriaalit, projektin arkkitehtuurikuvaus, FAQ, kehitysohjeet...
  * **Hyödyt:** Markdown-tuki, Helppo linkittää eri sivuja, Hyvä paikka pitkäkestoiselle dokumentaatiolle, jota ei haluta pitää README.md:ssä
* GitHub Issues
  * **Mikä se on?** Issue tracker, jossa käyttäjät ja kehittäjät voivat raportoida bugeja, ehdottaa uusia ominaisuuksia ja keskustella projektista.
  * **Miten käyttää?** Luo issue jokaisesta bugista tai parannusehdotuksesta. Käytä tageja (labels) luokitellaksesi issuet (esim. bug, enhancement, question).
  * **Hyödyt:** Keskitetty paikka bugiraportoinnille ja kehitysehdotuksille, Helppo seurata projektin tilaa ja priorisoida tehtäviä.