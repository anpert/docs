# 00 harjoitustietokanta

* 01 tietokannan luominen
* 02 henkilo-taulun luominen
* 03 indeksit
* 04 tiettueiden lisääminen


# 01 Tietokannan luominen:

```SQL
CREATE DATABASE IF NOT EXISTS opetuskanta
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;
```

Jos käytössä on MySQL 5.7 tai MariaDB, voi olla, että   ``utf8mb4_0900_ai_ci`` ei ole olemassa. Silloin tuosta edellisestä tulee virheilmoitus. Käytä silloin tätä seuraavaa

```SQL
CREATE DATABASE IF NOT EXISTS opetuskanta
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE opetuskanta;
```

* ``COLLATE utf8mb4_0900_ai_ci`` muokkaa tietokantaa niin, että siihen talletettavat "ääkköset" (åäö) ja muutkin Unicode- merkit toimivat oikein

# 02 Henkilö- taulun luominen

* seuraavaksi luodaan ensimmäin taulu tietokantaan
* tietokantataulun (table) tärkeimmät osat ovat tietueet (records). Siksi taulun nimi kannattaa antaa yksikkömuodossa. Esim. tässä "henkilo"
* käytä nimessä vain kirjaimia A...Z
* älä käytä välilyöntejä. Jos välilyöntiä tarvitset, kirjoita alaviiva ( _ )

* tämän alla on koodi, jolla taulu tehdään
* taulun luova koodi on ```CREATE TABLE```.
* koodirivillä mainitaan 
* ``henkilo_id INT UNSIGNED NOT NULL AUTO_INCREMENT``: tämän luo jokaiselle tietueelle (eli riville) yksilöllisen ja automaattisen tunnuksen. Voit käyttää sitä linkittäessäsi tietuetita toisiinsa 
* taulussa on kenttä ```luotu``` johon tallettuu tietueen talletushetki ja ```muokattu```, johon tallettuu (päivittyy)tietueen muokkaushetki
* tauluun on määritelty se, että kahta samaa sähköpostiosoitetta ei voida syöttää (```CONSTRAINT uq_henkilo_sahkoposti UNIQUE (sahkoposti)```)

Luodaan "henkilö"- taulu




```SQL
CREATE TABLE IF NOT EXISTS henkilo (
    henkilo_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    etunimi VARCHAR(100) NOT NULL,
    sukunimi VARCHAR(100) NOT NULL,
    sahkoposti VARCHAR(255) NOT NULL,
    puhelin VARCHAR(30) NULL,
    syntymaaika DATE NULL,
    aktiivinen BOOLEAN NOT NULL DEFAULT TRUE,
    luotu DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    muokattu DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT pk_henkilo PRIMARY KEY (henkilo_id),
    CONSTRAINT uq_henkilo_sahkoposti UNIQUE (sahkoposti)

) ENGINE=InnoDB;
```



# 03 Indeksit
Indeksit tehostavat tiedonhakua. Siksi ne kentät, joita esim. haetaan useimmiten, kannatta indeksoida.
Indeksit kannattaa lisätä taulun luontivaiheessa.
Näet indeksit phpMyAdminissa tietokannan "Rakenne"- välilehdellä.

```SQL
CREATE INDEX idx_henkilo_sukunimi_etunimi
    ON henkilo (sukunimi, etunimi);

CREATE INDEX idx_henkilo_aktiivinen
    ON henkilo (aktiivinen);
```




# 04 Tietueiden lisääminen
Lisää tietueita. Alla koodi, jolla sen voit tehdä. Keksi lisää!

```SQL
INSERT INTO henkilo (
    etunimi, sukunimi, sahkoposti, puhelin,
    syntymaaika, aktiivinen
)
VALUES
    ('Maija', 'Meikäläinen', 'maija.meikalainen@example.com', '0401234567', '1990-05-12', TRUE)
```

# 05 Harjoituksia tietokannalla 1

1. Lisää tauluun muutamia tietueita SQL- lauseena
2. Lisää tauluun muutamia tietueita PHPMyAdminilla
3. Tee SQL- haku, jolla saat listattua kaikki ne, joiden etunimi alkaa tietyllä kirjaimella
4. Tee haku, jolla saat listattua kaikki ne, joiden etunimi alkaa tietyllä kirjaimella ja joiden sukunimen viimeinen kirjain on jokin valitsemasi.




# 06 Lisää tauluja

Seuraavaksi teemme listää tauluja.

### A. Teemme ```yritys``` - taulun
 Teit aikaisemmin henkilo- taulun. Miten sen koodia pitää muuttaa, että saadaan yritys- taulu?<br>
 * pienellä muutoksella:
   * <span style="color:yellow">CREATE TABLE IF NOT EXISTS</span>  ~~henkilo~~~  <span style="color:yellow">yritys</span>**<br>
   * ~~henkilo_id~~ <span style="color:yellow">yritys_id INT UNSIGNED NOT NULL AUTO_INCREMENT,</span><br>
   * ~~etunimi~~ <span style="color:yellow">nimi VARCHAR(100) NOT NULL,</span><br>
 * omia kenttiä:
   * Y- tunnus on tärkeä <span style="color:yellow">y_tunnus VARCHAR(20) UNIQUE,</span>
   * puhelin samalla tavalla kuin henkilo- taulussakin: <span style="color:yellow">puhelin VARCHAR(30),</span>
   * yrityksen sähköposti, samalla tavalla kuin henkilo- taulussakin: <span style="color:yellow">sahkoposti VARCHAR(255),</span>
 * samalla tavalla kuin henkilo- taulussakin: 
   * <span style="color:yellow">luotu DATETIME DEFAULT CURRENT_TIMESTAMP,</span>
   * <span style="color:yellow">muokattu DATETIME DEFAULT CURRENT_TIMESTAMP </span>
   * <span style="color:yellow">ON UPDATE CURRENT_TIMESTAMP,</span>

 * loppuun vielä avainten määrittelyt
   * <span style="color:yellow">CONSTRAINT</span> ~~pk_henkilo~~ <span style="color:yellow">pk_yritys PRIMARY KEY</span> (~~henkilo_id~~ <span style="color:yellow">yritys_id),</span>
   * jos haluat laittaa yrityksen sähköpostiosoitteen uniikiksi, lisää vielä tämä:
   * CONSTRAINT</span> ~~uq_henkilo_sahkoposti~~ uq_yritys_sahkoposti UNIQUE (sahkoposti)</span>
  * loppuun vielä
    * <span style="color:yellow">) ENGINE=InnoDB;</span>


### B. Teemme viitteen henkilo- tauluun. 
Viite on uusi kenttä. Siihen kenttää kirjoitetaan henkilön yrityksen id- numero. Yrityksen nimeä ei siis kirjoitata henkilo- tauluun.

``` SQL
ALTER TABLE henkilo
ADD COLUMN yritys_id INT UNSIGNED NULL;
```

Tuossa määritellään, että kentän sisältö voi olla myös tyhjä (eli NULL). Onhan olemassa paljonkin tilanteita, joissa henkilöllä ei ole työpaikkaa.

Tämän jälkeen muokkaamme tuon kentän ns. vierasavaimeksi. Se tarkoittaa sitä, että henkilo- ja yrityst- taulujen välille syntyy yhteys (relaatio).

``` SQL
ALTER TABLE henkilo
ADD CONSTRAINT fk_henkilo_yritys
FOREIGN KEY (yritys_id)
REFERENCES yritys (yritys_id)
ON DELETE SET NULL
ON UPDATE CASCADE;
```

Sitten lisäämme vielä indeksin henkilo- tauluun. Sen nimi on idx_henkilo_yritys.

``` SQL
CREATE INDEX idx_henkilo_yritys
ON henkilo (yritys_id);
```

Jos menet PhphMyAdminin tietokanta-tasolle ja valitset sietlä **suunnittelija**- välilehden, näettietokannan rakenteen ERD- muodossa.






=============================================================

osoite
ryhmä
henkilö_ryhmä
rooli



















# xx Lisää tietueita
## Macaroo tekee demoarvoja
* Yksi keino täyttää tietokantaa demoarvoilla on [macaroo.com](https://www.mockaroo.com/) - palvelu. 
* Voit määritellä, millaisia demoarvo haluat. Kuvailen tässä asetukset, joilla voi täyttää tämän tehtävän esimerkkitietokantaa.
* Alla lista kentistä (Field Mame), niiden tyypeistä (Type) ja asetuksista (Options).
* laita Macaroo'n kenttien nimet samoiksi kuin omassa tietokanta-taulussasi on. Silloin saat demoarvot suoraan oikeassa muodossa.
* Listietoja kentistä allaolevan listan jälkeen.


| Kenttä      | Type                  | Mockaroo-asetukset                          | Esimerkki                  |
|--------     |------                 |--------------------                         |-----------                 |
| etunimi     | First Name (European) |                                             | Antti                      |
| sukunimi    | Last Name             |                                             | Virtanen                   |
| sahkoposti  | Email Address         |                                             | antti.virtanen@example.com |
| puhelin     | Regular Expression    | `+358 (40\|41\|44\|45\|46\|50) \d{3} \d{4}` | +358 40 123 4567           |
| syntymaaika | Datetime              | Format: `yyyy-MM-dd`                        | 1987-03-14                 |
| aktiivinen  | Custom List           | 0,1 ; weighted                              |

* **etunimi** ja **sukunimi**: Macaroo'sta saat eurooppalaisia nimiä mutta et suomalaisia. Tässä se ei varmaankaan haittaa mitään
* **puhelin**:
  * macaroo:ssa saat suomalaisia puhelinnumeroita esim. näit: valitse Type'ksi ```Regular Expression``` ja Options'ksi ```\+358 4[0-9] \d{3} \d{4}```
  * määrittelin niin, 5%:ssa tietoja ei ole annettu puhelinnumeroa. Laitoin riville **blank**- tekstin jälkeen 5%
* **syntymäaika** on muodossa ```vvvv-kk-pp```. Valitse tämä format- alasvedosta.
* **aktiivinen**: 
  * tämä on TRUE/FALSE- tieto. MySql ymmärtää luvun 0 FALSE:ksi ja luvun 1 TRUE:ksi.
  * **aktiivinen**: ajatteli niin, että 80%:ssa demoarvoja käyttäjä on aktiivisia ja loput eivät.<br>Tämä säädetään Mocaroo'ssa esim. niin, että siihen "weighted"- napin oikealla puolella olevaan valintaan laitetaan 0:n kohdalle esim. 2 ja 1:n kohdalle 8. 

## Demoarvojen tulostaminen
Asetukset tehdään field Name- osion jälkeen. 
* #Rows- kohta: haluamasi määrä. Ilmaisessa versiossa max. 1000
* Format: SQL: silloin saat tiedot suoraan SQL-koodina
* Table Name: voit laittaa siihen suoraan oman taulusi nimen (tässä: ```henkilo```)
* **Jätä create table pois!**

Aluksi kannattaa välita **PREVIEW**. Kun olet varma, että tiedot tulostuvat oikein, jatka eteenpäin.
Valmiin demoarvo-tiedoston voit liittää tietokantaan Henkilo - taulun Tuonti- valinnan kautta.

Nyt sinulla on olemassa testikanta. Seuraavat harjoitukset voit tehdä siinä.

Esimerkkirivillä näkyvät maijan tiedot. Viimeinen kenttä, ```aktiivinan```, on esimerkki ```TRUE/FALSE```- kentästä.
Lisää tietueita esim. 100 kpl. Voit käyttää apuna esim. mockaroo.com- sivustoa. Muista, että ```id```- kenttään ei saa laittaa arvoa!
