## Git- projektin aloittaminen ##

GIT-projekti on tietokoneella oleva kansio, joka sisältää  tiedostoja. Tiedostot muodostavat yhdessä projektin. Projekti voi olla esim. tietokoneohjelma. 

### Yksi mahdollinen hakemistorakenne ###

Tietokoneelle tulevat koodikansiot kannattaa tehdä samaan koodien juurikansioon (alla "git-data"). Tömön voi tehdä Windows- koneessa Tiedostot- kansioon. Esim. 

```
Tiedostot
│ 
└─ git-data
   │ 
   └─ python
   │  └─ .git
   │  └─ koti
   │     │
   │     └─ hilavitkutin
   │     │     paaohjelma.py
   │     └─ koulu
   │     │     opiskelijalista.py
   │     │     naytto_o45.py
   │     └─ mooc    
   │           tehtava 15.py
   │ 
   └─ dokumentit  
   │     └─ .git
   │     └─ harjoituksia
   │     │     lujuuskerroin.txt
   │     │     happamuuden_mittaus.md
   │     └─ oppaita
   │           sahkopostin_hakemins.DOCX
   │           kulkukortti.md
   │   
   └─ git-kurssi

```

Kaaviossa näkyy kansiot **python**, **dokumentit** ja **git-kurssi**. Kahden ensimmäisen sisällä on kansio nimeltä **.git**. Se on piilotettu kansio. Tämä kansio muodostuu siinä vaiheessa, kun tämä kansio muutetaan Git- projekstiksi. Tästä tarkemmin vähän myöhemmin.

Jos tietokoneen kansiorakenne on niinkuin tuossa kuvassa, olisi koneessa kaksi git-projektia: python ja dokumentit. Niiden sisällä olisi sitten muita kansiota.

Kolmas kansio, git-kurssi, ei olisi vielä määritelty git-projektiksi.

### Piilotetut kohteet ###
Sinun kannatta ottaa Windowsissa käyttöön piilotettujen kansioiden näyttäminen. 
* Avaa jokin tiedostohallinnan tiedostokansio. 
* Valitse otsikkoriviltä **näytä** ja  **näytä** ja **piilotetu kohteet**. 

## Komentokehotteen käyttö ##
Git- komentoja on helppo käyttää **komentokehotteessa**. Se on Windows- koneissa oleva merkkipohjainenympäristö. Se muistuttaa alun perin kaikissa MsDos- koneissa ollutta käyttöjärjestelmäympäristöä.

1) Avaa Windowsin resurssienhallinta. Siirry Tiedostot- välilehdelle 
2) Klikkaa osoiterivillä näkyvää **Tiedostot >** - tekstiä
3) Kirjoita CMD ja paina enter. Komentokehoiteympäristö aukeaa. Ruudulla lukee Windows versio ja kansion polku, joka voi olla esim. **C:\Users\kaaleppi\Documents>**
4) Luo tähän kansioon **git-data**- kansio komennolla `mkdir git-data`. Paina enter. Enter tulee jokaisen komennon jälkeen.
5) Siirry luomaasi kansioon komennolla `cd git-data`. Voit myös kirjoittaa `cd gi` ja painaa tabulaattoria. Silloin Windows ehdottaa Unix- tyyliin mahdollisia koodin jatkoja
6) Enterin painamisen jälkeen on uudessa kansiossasi. Kirjoita `dir`, sillä näet kansion sisällön. Se on tyhjä.

```bat
 Directory of C:\Users\kaaleppi\Documents\git-data

01.02.2025  12.34    <DIR>          .
01.02.2025  12.34    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)   12 345 678 90 bytes free

C:\Users\Omistaja\Documents\git-data>
```
Ylläolevassa kuvassa näkyy, että kansiossa ei ole tiedostoja mutta on kaksi kansiota. Nämä kansiot ovat nykyinen kansio `(.)`  ja ylempi kansiotaso `(..)`.

Luo tähän kansioon vielä (ellet ole sitä jo tehnyt) yksi kansio. Se tulee tämän kurssin harjoituksia varten. Anna kansiolle nimeksi **git-kurssi** (`mkdir git-data`).

Siirry kansioon `cd git` ja **tab** ja **enter**.

Luo tästä kansiosta Git-projekti ajamalla siellä komento `git init`. Tämän jälkeen siellä voi käyttää git-komentoja. 

Koska kansiossa on piilotettuja tiedostoja, sinun pitää tarkastella sen sisältöä komennolla `dir /a:h`. Kokeile!

```bat
 Directory of C:\Users\Omistaja\Documents\git-data\git-kurssi

01.06.2025  20.29    <DIR>          .git
               0 File(s)              0 bytes
               1 Dir(s)  260 751 056 896 bytes free

C:\Users\Omistaja\Documents\koodaus\git_kurssi>
```

Jos nyt katsot kansion sisältöä huomaat, että sinne on syntynyt alikansio **.git**. Piste tiedoston nimen edessä tarkoittaa sitä, että sen näkyminen on estettynä tavanomaisissa hauissa. Tähän  kansioon git säilöö tietoa kyseisestä projektista. Jos poista tämän kansion, git-projkti poistuu.

Tässä vaiheessa kannattaa ottaa käyttöön komento `git status`. Kokeile sitä git-kurssi -kansiossa.

```bat
C:\Users\Omistaja\Documents\git-data\git-kurssi>git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```
Kaikki kunnossa. 


## Commit ##
Tietoa tallennetaan Git-projektiin **committeina**. Commit on eräänlainen paketti, johon talletetaan projektin tiedostoihin tehtyjä muutoksia. Muutos voi olla esimerkiksi se, että tiedostoon lisättiin tai poistettiin tekstiä. 

**Committia** voi ajatella uutena askeleena kohti valmista projektia. Jokaisessa commitissa tehdään edelliseen committiin jotain muutoksia. Esimerkiksi, kun tietokoneohjelmaan koodataan uusi ominaisuus, se muuttunut tiedosto paketoidaan uuteen committiin.

> ***Gitin "kerrokset"***
> 
>*Otetaan tähän väliin vähän git- käsitteitä. Alla listattu erilaisia "tiloja", jotka tiedosto saa git-käsittelyn aikana. Nämä eivät ole fyysisiä paikkoja. Ne ovat tiedoston saamia tiloja. Näitä tiloja voi havainnollistaa vaikkapa näin:*
```
┌─────────────────────────────────────────────────┐
│ working directory (tietokoneen tiedostokansio)  │
├─────────────────────────────────────────────────┤
│ stagign area (stagign-tila)                     │
├─────────────────────────────────────────────────┤
│ local repository (paikallinen repository)       │
├═════════════════════════════════════════════════┤
│ remote repo                                     │
└─────────────────────────────────────────────────┘
```
>*Tiedosto saa listassa olevat kolme ylintä tilaa paikallisessa tietokoneessa. Alin tila, **remote repo** on, kuten nimestä voi päätelläkin, Githubissa tai muussa vastaavassa talletuspaikassa.*
>
>*Kun teet editorilla koodia ja talletat sen kansioon, jossa on mahdollistettu git- toiminnat (`git init`), se tallettuu working directoryyn. Eli fyysiseti yleensä paikalliselle kovalevylle.*

## Commitin luominen
Commitin luominen tapahtuu niin, että siihen haluttavat muutokset (eli tiedostot)lisätään `git add`- kommennolla **staging-tilaan**. 

Kun kaikki halutut muutokset ovat kyseisessä tilassa, ajetaan commitin luova komento (`commit`), joka **yhdistää** kaikki stagingissa olevat muutokset yhdeksi commitiksi.

Tarkastellaan seuraavaksi commitin luomista esimerkin kautta.

1. Siirry komentotilassa sinne aikaisemmmin tekemääsi **git-kurssi**- projektikansioon, ellet jo ole siellä.
2. Luodaan nyt Git-projektikansio komentotilassa. Käytä komentoa `mkdir testikansio1`. 
3. Siirry tähän uuteen kansioon komennolla `cd testikansio1`. 
4. Lisätään sinne tyhjä tiedosto *lapio_vko2.txt*. Voi tehdä sen Windowsin komentotilassa komennolla `echo > lapio_vko2.txt`. Tarkista, että tiedosto ilmestyi kansioon. Komento on `dir`.
5. Muodosta `testikansio1` -kansiosta git-projekti komennolla `git init`.
6. Tarkista projektin tila komennolla `git status`.

Tiedosto **lapio_vko2.txt** in nyt talletettuna tietokoneen tiedostokansioon
```
┌─────────────────────────────────────────────────┐
│ working directory (tietokoneen tiedostokansio)  │
└─────────────────────────────────────────────────┘
```
## Muutosten eri tilat ##
Muutoksia voidaan lisätä seuraavaan committiin komennolla `git add`. Komennolle annetaan argumenttina tiedosto, jonka sisältämät muutokset siirrettään **staging**-tilaan. Ennen kuin tiedosto on lisätty Gitin tietoon, on se otsikon Untracked files alla. Tällöin tiedoston sisältämiä muutoksia ei myöskään olla lisäämässä seuraavaan committiin.

Lisätään nyt lapio-tiedoston muutokset seuraavaan committiin ajamalla `git add lapio_vko2.txt`. Tiedosto on nyt staging- tilassa.
```
┌─────────────────────────────────────────────────┐
│ working directory (tietokoneen tiedostokansio)  │
├─────────────────────────────────────────────────┤
│ stagign area (stagigng-tila)                    │
└─────────────────────────────────────────────────┘
```
Lisätään tiedostoon sen jälkeen hieman tekstiä komennolla `echo "tämä on lapion toinen osa" >> lapio_vko2.txt` . 

Ajetaan sen jälkeen git status:


===================================================


### Commitit

Tietoa tallennetaan Git-projektiin committeina. Commit on eräänlainen paketti projektin tiedostoihin tehtyjä _muutoksia_. Käytännössä muutokset tarkoittavat esimerkiksi sitä, että tekstiä lisättiin tai poistettiin jostain projektin tiedostosta.

Committia voi ajatella uutena askeleena kohti valmista projektia. Jokaisessa commitissa lisätään edelliseen committiin jotain muutoksia. Esimerkiksi ohjelmaa koodattaessa uuden toiminnallisuuden lisääminen voitaisiin luontevasti paketoida yhteen committiin.

Commitin luominen tapahtuu niin, että siihen haluttavat muutokset lisätään _staging_\-tilaan. Kun kaikki halutut muutokset ovat kyseisessä tilassa, ajetaan commitin luova komento, joka yhdistää kaikki stagingissa olevat muutokset yhdeksi commitiksi.

Tarkastellaan seuraavaksi commitin luomista esimerkin kautta.

Komento `git status` on erittäin hyödyllinen, sillä se antaa tietoa Git-projektin ja sen sisältämien muutosten tämänhetkisestä tilasta.

Luodaan nyt Git-projektikansio, ja lisätään sinne tyhjä tiedosto `lapio_vko2.txt` vaikka komennolla `touch`. Kun ollaan vasta luotu Git-projekti, lisätty sinne tiedosto, ja ajetaan `git status`, tulostuu

    On branch main
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
    	lapio_vko2.txt
    
    nothing added to commit but untracked files present (use "git add" to track)
    

Pureskellaan seuraavaksi hieman tulostuksen sisältöä.

### Muutosten eri tilat

Muutoksia voidaan lisätä seuraavaan committiin komennolla `git add`. Komennolle annetaan argumenttina tiedosto, jonka sisältämät muutokset siirrettään staging-tilaan. Ennen kuin tiedosto on lisätty Gitin tietoon, on se otsikon `Untracked files` alla. Tällöin tiedoston sisältämiä muutoksia ei myöskään olla lisäämässä seuraavaan committiin.

Lisätään nyt lapio-tiedoston muutokset seuraavaan committiin ajamalla `git add lapio_vko2.txt`. Lisätään tiedostoon sen jälkeen hieman tekstiä komennolla `echo "tämä on lapion toinen osa" >> lapio_vko2.txt`. Ajetaan sen jälkeen `git status`:

    On branch main
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)
    
    	new file:   lapio_vko2.txt
    
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)
    
    	modified:   lapio_vko2.txt
    

Lisätään tämän jälkeen projektikansioon vielä yksi tiedosto, nimeltään `tyhja_tiedosto.txt`. Ajetaan sen jälkeen uudelleen `git status`. Nyt tulostuu:

    On branch main
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)
    
    	new file:   lapio_vko2.txt
    
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)
    
    	modified:   lapio_vko2.txt
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
    	tyhja_tiedosto.txt
    

Tutkitaan jälleen tulostusta.

Ensimmäisenä on `Changes to be committed.` Tämän otsikon alla olevat muutokset ollaan nyt siirtämässä seuraavaan committiin.

`Changes not staged for commit` tarkoittaa muutoksia, jotka ovat Gitin tiedossa, mutta joita **ei** olla siirtämässä seuraavaan committiin.

Lopuksi `Untracked files` tarkoittaa sellaisia tiedostoja, jotka eivät ole Gitin tiedossa, ja joissa tapahtuvia muutoksia ei siis seurata. Niistä ei voida silloin esimerkiksi kertoa, mitä muutoksia tiedostossa on tehty. Näitä muutoksia ei myöskään siis lisätä seuraavaan committiin.

Tulostuksessa on siis tiedosto `lapio_vko2` kahdesti, sillä Git seuraa _muutoksia_. Gitille on lisätty ensin tiedoston muutos, jossa tiedosto `lapio_vko2` luotiin. Vasta tämän jälkeen tiedostoon lisättiin tekstiä. Committiin ollaan nyt lisäämässä vain muutos, jossa tiedosto luotiin, ei muutos, jossa tiedostoon lisättiin tekstiä. Tulkintaa helpottaa se, että committiin lisättävät muutokset tulostuvat oletuksena vihreinä, ja tiedoston nimen vieressä näkyy, mitä tiedostolle on tehty (esimerkiksi `new file`, `modified`, `deleted`).

Gitin avulla voidaan myös perua muutoksia. Jos haluaisimme perua `lapio_vko2.txt`\-tiedostoon lisäämämme tekstin, voitaisiin ajaa `git checkout -- lapio_vko2.txt`. Kun tämän jälkeen avaa kyseisen tiedoston, se on tyhjä, eli muutos, jossa lisättiin tekstiä, peruttiin. Komento `git checkout --` mahdollistaa siis seuratuista tiedostoista muutosten perumisen.

Ajamalla `git add -p`, voit valita muutos kerrallaan, haluatko lisätä sen Gitin committiin (y=lisää, n=älä lisää). Komento ottaa huomioon vain muutokset tiedostoissa, _jotka on jo kertaalleen lisätty Gitiin_. Näin ollen esimerkiksi uusia tiedostoja ei voi lisätä Gitiin komennon `git add -p` avulla. Pelkkä `git add tiedosto` lisää kaikki tiedoston muutokset Gitiin. Samalla komennolla on myös mahdollista lisätä kerralla kokonaisen kansion sisältämät muutokset.

##### Varjele salaisuuksiasi

Jos pidät mahdollisena, että haluat jakaa projektin joskus muille, älä lisää sen commiteihin mitään salaista. Vaikka poistaisit tiedon seuraavassa commitissa, se jää Gitin projekti-historiaan, ja on löydettävissä GitHubista julkaisun jälkeen.

Huomioi myös että GitHub on pilvipalvelu, ja muut kuin valitsemasi henkilöt saattavat saada pääsyn myös yksityiseksi merkittyihin projekteihin.

Komennon `git status` avulla kannattaa jatkuvasti tarkistaa, missä tiedostoissa sijaitsevat muutokset olet lisäämässä committiin. Sen jatkuva ajaminen on hyvä tapa, joka kannattaa omaksua.

### Commitin paketointi

Kun ollaan valittu, mitä muutoksia halutaan lisätä committiin, paketoidaan se komennolla `git commit`. Jokaisella commitilla on otsikko, joka kuvaa siinä tehtyjä muutoksia. Otsikko voidaan lisätä komennolla `git commit -m "kuvaava otsikko"`, jossa kuvaava otsikko kertoo, mitä muutoksia tehtiin suhteessa edelliseen committiin. Jos komennosta jättää vivun `-m` ja viestin sen jälkeen pois, tekstieditori aukeaa, ja voit kirjoittaa otsikon, sekä pidemmän viestin sen alle. Committi luodaan tällöin, kun tallennat viestin ja poistut editorista.

[Täältä](https://github.com/erlang/otp/wiki/writing-good-commit-messages) löytyy nopeat ohjeet hyvän commit-viestin kirjoittamiseksi.

Jatketaan edellistä esimerkkiä. Lisätään seuraavaan committiin kaikki muutokset, paitsi tiedoston `tyhja_tiedosto` luonti. Ennen komennon `git commit` ajamista, komennon `git status` tulostus on seuraava:

    On branch main
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)
    
    	new file:   lapio_vko2.txt
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
    	tyhja_tiedosto.txt
    

Ajetaan seuraavaksi `git commit -m "Lisää uusi lapio-tiedosto"`

Nyt `git status` tulostaa :

    On branch main
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
    	tyhja_tiedosto.txt
    
    nothing added to commit but untracked files present (use "git add" to track)
    

Commitoidut muutokset eivät siis enää näy statuksessa. Ne eivät kuitenkaan ole hävinneet - ne on siirretty committiin. Komennolla `git log` pystyt tarkastelemaan luotuja committeja:

    commit 51bf544c786a671c28f70713b6cb33d87cc38
    Author:
    Date:
    
        Lisättiin lapio_vko2.txt -tiedosto
    

Komento `git log` siis tulostaa commitin tekijän, luontiajan, sekä commitille annetun otsikon. Jokaisella commitilla on sen identifioiva merkkijono eli id, joka on [SHA-1](https://en.wikipedia.org/wiki/SHA-1)\-muodossa. Komennon `git log` tulostuksessa id näkyy pitkänä merkkijonona, esimerkiksi tässä tapauksessa se on `51bf544c786a671c28f70713b6cb33d87cc38`.

##### Ajatusleikki

Commitin luominen voi aluksi tuntua epäintuitiiviselta. Seuraava ajatusleikki saattaa auttaa: Kuvittele, että commit on lahjapaketti. Istut lattialla. Muutokset ovat puupalikoita, jotka on levitetty lattialle viereesi. `Changes to be commited`\-tila on eteesi levitetty käärepaperi. Komennolla `git add` lisäät muutoksia käärepaperin päälle, ja komennolla `git commit` sidot käärepaperin muutosten ympärille.

### Haarat

Komennon `git status` tulosteen yläreunassa näkyy: `On branch main`. Haarat, eli englanniksi _branchit_, mahdollistavat joidenkin committien eriyttämisen toisistaan. Näin ollen on mahdollista kehittää uuden haaran sisältöä ilman, että menetetään toimiva versio ohjelmasta. Tavanomaisesti jokaisella projektilla on päähaara, joka on oletuksena nimeltään `main`, ja jossa pidetään senhetkistä toimivaa ja käytössä olevaa versiota.

##### Oletushaaran nimi on muuttunut hiljattain

Perinteisesti git on käyttänyt oletuspäähaarasta nimitystä _master_, mutta vuosien 2020 ja 2021 aikana moni palvelu, ja lopulta myös GitHub, on luopunut master-sanan käytösä. Tämä päätös on osa suurempaa liikettä luopua master- ja slave-sanojen käytöstä avoimen lähdekoodin ohjelmistoissa.

Usein haaroja käytetään niin, että päähaarasta erotetaan uuden toiminnallisuuden testaamiseksi toinen haara, jossa koodataan lisäominaisuuksia. Haarat eivät vaikuta toistensa tiloihin, eli uudella koodilla voidaan leikkiä huolimatta päähaarasta. Kun ollaan todettu uusi koodi toimivaksi, voidaan se lisätä päähaaraan, ja poistaa kehitystyössä käytetty haara. Tässä osassa ei käsitellä haaroja sen enempää: riittää ymmärtää, että käytämme nyt vain main-, eli päähaaraa.

Tehtävä:

Committien harjoittelua


-------------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

1.  Luo kansio komentorivillä ja tee siitä Git-projekti.
2.  Luo projektikansioosi tiedosto nimeltä `tarina.txt`. Lisää sinne jokin pitkä pätkä tekstiä.
3.  Lisää projektiin tiedosto `ostoslista.txt`, jonne kirjoitat, mitä tarvitset kaupasta, tai muuten vaan paljon rivejä.
4.  Lisää sen jälkeen vielä alikansio `kouluprojektit`, ja lisää sinne ainakin yksi tiedosto `lapio.txt`. Tulet tarvitsemaan näitä tiedostoja tulevissa tehtävissä.
5.  Kun olet tehnyt kaikki edellä mainitut muutokset, tee yhteensä kolme committia: yksi, jossa lisäät tarinan, toinen, jossa lisäät ostoslistan, ja kolmas, jossa lisäät kouluprojektikansion sisällön. Kirjoita commiteille kuvaavat otsikot.
6.  Tarkista komennolla `git log`, että olet luonut kolme committia.
7.  Muuta ostoslistalta jokin ostos, ja tee vielä yksi commit. Käytä muutoksen lisäämisessä komentoa `git add -p`.
8.  Tarkista, että kaikki commitit näkyvät `git log`\-komennolla.

##### Oletuseditorin väärä konfiguraatio

Jos committia luodessa tulostuu virheviesti `error: cannot run : No such file or directory error: unable to start editor`, varmista, että olet konfiguroinut oletuseditorin oikein (tämä tehtiin tehtävässä 2).

Tehtävä:

Muutosten poistaminen


-----------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

1.  Selvitä, miten saat poistettua muutoksen tilasta, jossa olet lisäämässä sitä committiin (näkyy vihreänä tulostuksessa), ja siirrettyä muutoksen otsikon `Changes not staged for commit` alle? Vinkki: `git status` auttaa.
2.  Lisää uusia tuotteita ostoslistaan, ja aseta muutokset lisättäväksi seuraavaan committiin (`Changes to be commited`). **Älä kuitenkaan paketoi committia.**
3.  Poista sen jälkeen muutokset seuraavasta commitista.
4.  Poista sen jälkeen muutokset Gitin avulla niin, että kun avaat ostoslistan, uusimmat tuotteet puuttuvat.

Koodin jakaminen GitHubissa
---------------------------

Käsitellään seuraavaksi, miten GitHubia voidaan käyttää yhdessä Gitin kanssa koodin jakamiseksi ja julkaisemiseksi.

### Etärepositorion luominen

Jotta projektin voi jakaa GitHubin kautta, sille pitää luoda oma repositorio (kavereille repo) GitHubiin, ja tämä repositorio pitää liittää oman koneen Git-projektiin. Tämä tapahtuu lisäämällä repo Git-projektin etärepositorioksi, eli _remoteksi_. Kun Git-projektille lisätään etärepositorio, on mahdollistä siirtää tietoa sen ja omalla koneella olevan projektin välillä. Tällöin projektista on olemassa kaksi versiota: paikallinen (_local_), eli “omalla koneella” oleva projekti ja etärepositorion versio (_remote_), eli GitHubissa säilöttävä versio.

Tässä siis näkyy, miten GitHubia voidaan käyttää varmuuskopiona: kun projektin tila päivitetään GitHubiin, pääsee tietoon käsiksi internetin kautta, ja projektia voi jatkaa, vaikka paikalliselle versiolle tapahtuisikin jotain.

GitHubissa saa luotua repositorion oikeasta yläkulmasta:

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/jw1V7H4mj81dKGbBUqulkZyp9dHQ9d.png)

Avautuu näkymä, jossa lisätään repolle nimi ja kuvaus. Repositorio voi olla joko julkinen tai yksityinen. Julkisen repostorion näkee kuka vaan, yksityisen vain omistajan valitsemat käyttäjät.

GitHub myös tarjoaa mahdollisuuden luoda projektille _README:n_, _lisenssin_ ja _.gitignore_\-tiedoston. Ohjelmistotuotannossa on tapana, että ohjelmistoprojektiin lisätään README-niminen tiedosto, joka sisältää yleishyödyllistä tietoa koko projektista. Hyvä README sisältää esimerkiksi lyhyen kuvauksen projektista, asennusohjeet ja linkin mahdolliseen dokumentaatioon. Lisenssi tarkoittaa dokumenttia, jossa määritellään, mitkä ovat ohjelman tekijän ja käyttäjän vastuut ja vapaudet. Tiedosto `.gitignore` on erittäin hyödyllinen tiedosto, jonka avulla Gitiä voi pyytää jättämään joitain tiedostoja huomiotta committeja tehdessä. `.gitignore`:n käytöstä voit lukea esimerkiksi [täältä](https://www.atlassian.com/git/tutorials/saving-changes/gitignore).

##### Ei kannata aina antaa GitHubin luoda repositorioosi oletussisältöä

Kun halutaan siirtää valmiiksi luotu projektikansio GitHubiin, ei kannata antaa GitHubin luoda tiedostoja automaattisesti. Tämä johtaisi vaikeuksiin, sillä tällöin GitHubissa olisi tiedosto, jota lokaalissa versiossa ei ole. Tällaisen tilanteen ongelmallisuus selviää myöhemmin tässä osassa.

Nappi `Create repository` lisää projektin omaan profiiliin. Kun projektiin navigoi, tarjoaa GitHub hyödyllisiä ohjeita koodin sinne lisäämiseksi. Projektiin löytää käyttäjän profiilista, tai suoraan osoitteella `https://www.github.com/kayttajanimi/projektinnimi`.

### Etärepositorion lisääminen

Etärepositorio yhdistetään paikalliseen projektiin komennolla `git remote add`.

Komento ottaa argumentikseen lisättävän etärepositorion nimen sekä osoitteen. GitHub tarjoaa kaksi vaihtoehtoa etärepositorion lisäysprotokollaksi: SSH ja https. Ensimmäisen vaihtoehdon pitäisi olla tuttu ensimmäisestä osasta, toisen selaimen osoitekentästä. SSH on siis sama yhteystyyppi, jolla vierailtiin laitoksen koneilla komennolla `ssh`. Tätä yhteystyyppiä on mahdollista käyttää myös GitHubissa, jos koneella on luotu yksityinen ja julkinen avainpari, joista julkinen on lisätty GitHubiin.

Jos käyttää https-yhteyttä, autentikointi tapahtuu GitHub-käyttäjänimellä ja salasanalla. SSH-yhteyden käyttö on siis paljon vaivattomampaa, sillä jos yksityisen avaimen lisää ssh-agentille, ei salasanaa tarvitse kirjoittaa jatkuvasti. SSH-avaimia käsiteltiin [ensimmäisessä osassa](https://tkt-lapio.github.io/komentorivi#SSH-avainpari).

Valitaan GitHubin ohjeista SSH-osoite projektille, jotta siihen voidaan muodostaa SSH-yhteys:

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/PgforTbHctWpTHM3uLXBilhVXBmQM2.png)

Uusi origin-niminen etärepositorio lisätään SSH-yhteyttä käyttäen ajamalla projektikansiossa komento `git remote add origin git@github.com:kayttaja/projekti.git`. Https-osoite olisi melkein sama, kuin selaimen osoiterivillä. Etärepositorion nimi voi olla muutakin kuin “origin”, mutta se on yleinen valinta. Yhdelle projektille voi lisätä useita etärepositorioita, jolloin niiden järkevä nimeäminen on oleellista.

Tehtävä:

SSH-avain GitHubiin


---------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

Jos et ole luonut koneellesi ssh-avainparia, tee se ensin. Ohjeet löytyvät tämän kurssin ensimmäisestä osasta.

Tehtävä:

Etärepositorion luominen Githubissa


-------------------------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

Luo aikaisemmin tekemällesi projektille vastapari, eli repositorio GitHubiin.

**Älä luo projektille GitHubissa valmiiksi lisenssiä, READMEtä tai .gitignore-tiedostoa, muuten kohtaat myöhemmin ongelmia.**

Liitä GitHubin repo projektisi etärepositorioksi. Jos teit edellisen tehtävän, käytä SSH-osoitetta, muuten käytä https-osoitetta.

### Julkaiseminen

Kun projekti on liitetty johonkin GitHubin repositorioon, voidaan committeja julkaista _puskemalla_. Muutokset voi puskea tietyn etärepositorion tiettyyn haaraan seuraavasti: `git push remotennimi haarannimi`. Tässä osassa käytämme vain main-haaraa. Jos lisäät sanan `push` jälkeen vivun `-u`, riittää ensi kerralla ajaa `git push`, jolloin muutokset pusketaan automaattisesti samaan paikkaan. Tämän vivun käyttö on suositeltavaa.

Pusketaan `lapio_vko2.txt`\-tiedostoon tekemämme muutokset komennolla `git push -u origin main`, sillä lisäsimme etärepositorion nimellä `origin`, ja käytämme `main`\-haaraa. Navigoidaan GitHubissa projektisivulle. Tiedosto `lapio_vko2.txt` näkyy nyt GitHubissa.

Tehtävä:

Commitin julkaiseminen


------------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

1.  Puske tekemäsi kolme committia etärepositoriosi `main`\-haaraan.
2.  Käy tarkistamassa GitHubissa, että kyseiset commitit näkyvät etärepositoriossa.

### Koodin hakeminen GitHubista

Samasta projektista on nyt siis olemassa kaksi tilaa kahdessa paikassa: paikallinen ja etärepositorio. Katsotaan seuraavaksi, mitä käy, kun nämä kaksi tilaa eivät ole aina täysin samat.

Aloitetaan tekemällä muutoksia projektiin GitHubin kautta. GitHubissa pääsee muokkaamaan tiedostoja painamalla niiden nimeä, ja oikealla olevaa kynä-ikonia.

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/VgS6LiQ6F9jDnnkyqcI4FYPZtoXv0h.png)

Lisätään tiedostoon `lapio_vko2.txt` uusi rivi tekstiä, ja luodaan commit sivun alalaidasta vihreästä napista. Muutokset eivät kuitenkaan näy omalla koneella heti.

Ajetaan seuraavat komennot:

`git fetch` hakee projektin uusimman tilan GitHubista, mutta ei tee muutoksia paikalliseen työhön. **Jos `git status` ei jatkossa näytä ajankohtaista tietoa etärepositorion tilasta, aja ensin `git fetch`**.

Muutokset eivät vieläkään näy. Jos puskit committisi etärepositorioon vivun `-u` kanssa, Git osaa kertoa, että GitHubissa on muutoksia, joita paikallisessa versiossa ei ole: status-komento tulostaa yläreunaan `Your branch is behind 'origin/main'`.

Nyt voidaan hakea muutokset paikalliseen versioon komennolla `git pull`. Jos aikaisemmin oltiin ajettu `push` vivulla `-u`, ei etärepositoriota tai haaran nimeä tarvitse kirjoittaa. Ajetaan `git pull`, jolloin tulostuu jotain seuraavan kaltaista:

    remote: Counting objects: 3, done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (3/3), done.
    From github.com
     * branch            main       -> FETCH_HEAD
       8793615..c661629  main       -> origin/main
    Updating 8793615..c661629
    Fast-forward
     lapio_vko2.txt | 1 +
     1 file changed, 1 insertion(+)
    

Nyt muutokset näkyvät myös paikallisesti.

Tehtävä:

Koodin hakeminen etärepositoriosta


------------------------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

Luo GitHubissa kouluprojektit-alikansioon uusi tiedosto, ja hae se sitten omaan projektiisi.

Käytännössä tämä tilanne vastaa sitä, että tehdään yhteisprojektia, ja joku muu on lisännyt projektiin koodia. Tällöin uuden ominaisuuden lisännyt julkaisee koodinsa puskemalla sen GitHubiin, jolloin muut projektin tekijät voivat hakea ne komennolla `git pull`.

Stash
-----

Kokeillaan seuraavaksi mitä käy, jos GitHubissa on jotain tietoa, mitä paikallisesti ei ole, ja paikallisesti jotain, mitä GitHubissa ei.

Muutetaan tiedoston `lapio_vko2.txt` ensimmäistä riviä GitHubin kautta. Tästä syntyy siis yksi commit. Lisätään paikallisesti saman tiedoston loppuun uusi rivi, **mutta ei tehdä paikallisesta muutoksesta committia**.

Jos nyt kokeillaan hakea uusimmat muutokset komennolla `git pull`, tulostuu:

    From github.com:
     * branch            main     -> FETCH_HEAD
    Updating 061ca96..6920cd0
    error: Your local changes to the following files would be overwritten by merge:
    	lapio_vko2.txt
    Please, commit your changes or stash them before you can merge.
    Aborting
    

Pullaus ei toimi, koska paikallisessa versiossa on muutoksia samaan tiedostoon, kuin etärepositoriossa, eikä paikallisia muutoksia ole commitoitu.

Tällaisessa tilanteessa voidaan laittaa paikalliset muutokset syrjään _stashiin_ komennolla `git stash`. Kun ajetaan `git stash`, paikallisesti lisätyt muutokset Gitin seuraamissa tiedostoissa laitetaan syrjään. Tämä siis tarkoittaa, että tehdyt muutoksen poistuvat näkyvistä, mutta niitä ei ole menetetty kokonaan. Laittaaksesi syrjään myös muutokset Gitiin vielä lisäämättömissä tiedostoissa (`untracked`), aja komento vivulla `-u`, eli `git stash -u`. Saat muutokset takaisin käskyllä `git stash pop`.

Tehtävä:

Stashin käyttäminen pullatessa


--------------------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

*   Tee muutoksia paikallisesti jo kertaalleen Gittiin lisäämiisi tiedostoihin (eivät ole `untracked`\-otsikon alla komennon `git status` tulostuksessa).
*   Laita sen jälkeen juuri tekemäsi muutokset syrjään stashiin.
*   Avaa sen jälkeen muokkaamasi tiedosto, näetkö tekemiäsi muutoksia?
*   Muokkaa GitHubin kautta `tarina.txt`\-tiedoston _ensimmäistä_ lausetta ja tee siitä commit.
*   Muokkaa sitten paikallisesti saman tiedoston _viimeistä_ lausetta, mutta **älä tee committia**.
*   Hae sen jälkeen etärepositoriossa `tarina.txt`\-tiedoston ensimmäiseen lauseeseen tekemäsi muutokset projektin paikalliseen versioon. Käytä apuna stashia.
*   Kun olet saanut haettua muutokset, tee viimeiseen lauseeseen tekemistäsi muutoksista uusi commit.
*   Puske tämän jälkeen lopputulos GitHubiin.
*   Varmista, että sekä ensimmäiseen, että viimeiseen lauseeseen tekemäsi muutokset ovat näkyvillä Githubissa.

##### Merge-konflikti

Jos edellisessä tehtävässä terminaaliin tulostuu "CONFLICT", saat apua hieman alempaa tältä sivulta.

Merge
-----

Jatketaan vielä kahden rinnakkaisen tilan kanssa.

Äskeisessä tilanteessa etärepositoriossa ja paikallisesti vallitsivat eri tilat, sillä molemmissa oli tietoa, jota toisella ei ollut. Koska paikallisia muutoksia ei oltu commitoitu, voitiin ne piilottaa stashiin. Mitä olisi tapahtunut, jos paikallisesti oltaisiin ehditty commitoida?

Tilanne voidaan ratkaista _mergellä_, eli yhdistämällä kaksi rinnakkaista tilaa. Sellaiset haarat, jotka eivät ole ristriidassa keskenään, eli toisin sanoen eivät tee päällekkäisiä muutoksia, Git osaa yhdistää automaattisesti. Tällöin Git luo uuden merge-commitin.

Oikeastaan komento `git pull` sisältää jo valmiiksi merge-toiminnallisuuden. Riittää siis ajaa komento `git pull`, ja antaa tekstieditorin avautuessa commitille otsikko, jotta saadaan yhdistettyä paikallinen main-haara etärepositorion main-haaraan. GitHub ehdottaa valmiiksi viestiä, jota voi halutessaan muokata mieleisekseen. Merge on valmis, kun merge-commitin viestin tallentaa.

Lisätään sekä paikallisesti että etärepositorioon uudet, keskenään erinimiset tiedostot ja commitoidaan. Kun sen jälkeen ajaa `git status` (aja ensin `git fetch`, jos `git status` ei näytä uusinta tilaa), tulostuu:

    On branch main
    Your branch and 'origin/main' have diverged,
    and have 1 and 1 different commit each, respectively.
      (use "git pull" to merge the remote branch into yours)
    nothing to commit, working directory clean
    

Git siis huomauttaa, että sekä etärepositorioon että paikallisesti on luotu committeja.

Jos yritetään puskea commit, se ei onnistu:

    To git@github.com:kayttaja/repo.git
     ! [rejected]        main -> main (non-fast-forward)
    error: failed to push some refs to 'git@github.com:kayttaja/repo.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Integrate the remote changes (e.g.
    hint: 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    

Git antaa jälleen vihjeen, miten kuuluu toimia. Haetaan ja yhdistetään siis etärepositorion uusin tila paikalliseen versioon komennolla `git pull`. Annetaan commitille tekstieditorin auetessa otsikko, ja tallennetaan. Tällöin tulostuu:

    From github.com:kayttaja/repo
     * branch            main     -> FETCH_HEAD
    Merge made by the 'recursive' strategy.
     new_file.txt | 1 +
     1 file changed, 1 insertion(+)
     create mode 100644 new_file.txt
    

Nyt komennon `git status` mukaan ollaan tehty 2 committia (`ahead by 2 commits`). Ensimmäinen niistä on se, joka luotiin paikallisesti. Toinen on uusi, automaattisesti luotu merge-commit. Nämä kaksi committia voitaisiin puskea GitHubiin ongelmitta.

Tehtävä:

Mergeäminen


-------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

*   Luo etärepositorioon GitHubissa ja paikallisesti sellaiset commitit, että niissä tapahtuvat muutokset eivät ole ristiriidassa keskenään, eli eivät muokkaa samoja rivejä. Toimi esimerkiksi seuraavasti: muokkaa ostoslistan ensimmäistä tuotetta GitHubissa, ja tee commit. Lisää sitten paikallisesti ostoslistan loppuun uusi tuote ja tee uusi commit.
*   Kokeile puskea paikallinen committisi etärepositorioon. Minkä virheviestin saat?
*   Hae sen jälkeen GitHubin muutos paikalliseen versioon, ja kirjoita commit-viestiksi "Ensimmäinen mergeni".
*   Puske lopuksi tekemäsi muutokset GitHubiin.

Merge-konflikti
---------------

Tehtäessä yhteistyötä aina välillä käy niin, että kaksi koodaria muokkaavat samoja rivejä. Miten Git tietää mergeä tehdessään, kumpi muutos halutaan pitää? No, ei se tiedäkään, eli joskus automaattinen merge ei onnistu. Kahden commitin version ristiriitaista tilaa mergettäessä kutsutaan _merge-konfliktiksi_. Esimerkki merge-konfliktista on tilanne, jossa etärepositoriossa ja lokaalisti on toisensa poissulkevia muutoksia sisältävät commitit. Silloin jonkun täytyy käsin valita pidettävät muutokset, eli ratkottava merge-konflikti.

Kirjoitetaan GitHubissa tiedostoon `lapio_vko2.txt` jollekin riville “terveisiä GitHubista”, ja tehdään muutoksesta commit. Muokataan sitten _täsmälleen_ samaa riviä paikallisessa versiossa kirjoittamalla “terveisiä mun koneelta” ja tehdään commit.

Nyt kun yritetään yhdistää etärepositoriosta uusin tila paikalliseen versioon komennolla `git pull`, tulostuu:

    Auto-merging ...
    CONFLICT (content): Merge conflict in lapio_vko2.txt
    Automatic merge failed; fix conflicts and then commit the result.
    

Rivi, joka alkaa sanalla `CONFLICT` kertoo missä tiedostossa päällekkäiset muutokset ovat tapahtuneet. Avataan tämä tiedosto. Siellä näkyy:

    <<<<<< HEAD
    terveisiä mun koneelta
    ======
    terveisiä GitHubista
    >>>>>> baaf2c96cw031e11138d42c1a35065b9bf8b4400b
    

Toisensa poissulkevat commitit on siis eroteltu <, > ja = -merkkien avulla. HEAD tarkoittaa tämänhetkistä committia (eli nykyisen haaran viimeisintä committia), ja kirjain-numero-yhdistelmä on toisen etärepositoriossa tehdyn commitin id. Hienostuneemmat editorit, kuten VSCode mahdollistavat konfliktien ratkaisemisen yhdellä klikkauksella, mutta muuten ainoa vaihtoehto on poistaa sen ne rivit, joita ei haluta pitää jatkossa.

Poistetaan kaikki merkeillä <, = tai > alkavat rivit, ja muokataan terveisiä. Konfliktien ratkaisija siis saa päättää, mitä konfliktin sisältämään tiedostoon jää. Jätetään tiedoston sisällöksi seuraava:

    terveisiä mun koneelta ja GitHubista

Kun ajetaan `git status`, Git muistuttaa, että ollaan ratkaisemassa konflikteja tiedostossa `lapio_vko2.txt`:

    On branch main
    Your branch and 'origin/main' have diverged,
    and have 1 and 1 different commit each, respectively.
     (use "git pull" to merge the remote branch into yours)
    You have unmerged paths.
     (fix conflicts and run "git commit")
    
    Unmerged paths:
     (use "git add <file>..." to mark resolution)
    
    	both modified:   lapio_vko2.txt
    
    no changes added to commit (use "git add" and/or "git commit -a")
    

Lisätään ratkaisu Gitiin komennolla `git add` (huomaa, että vivun -p käyttäminen ei toimi). Kun sen jälkeen ajetaan `git status`, tulostuu

    On branch main
    All conflicts fixed but you are still merging.
      (use "git commit" to conclude merge)
    
    Changes to be committed:
    
    	modified:   lapio_vko2.txt
    

Lopetaan siis konfliktin ratkaiseminen tekemällä commit. Pusketaan tämän jälkeen ratkaisu GitHubiin.

Merge-konfliktit ovat raivostuttavia, mutta yleisiä. Helpoiten niiltä välttyy aina hakemalla uusimman tilan etärepositoriosta, ennen kuin jatkaa koodaamista. Aina se ei ole kuitenkaan mahdollista, jolloin on vain kärsivällisesti käytävä konfliktitilanteet läpi.

Merge-konflikteja voi tulla myös, kun muutoksia ottaa pois stashista, jos syrjään asetetut muutokset ovat ristiriidassa nykyisten muutosten kanssa.

Tehtävä:

Merge-konflikti


-----------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

Aiheuta projektissasi merge-konflikti, ja ratkaise se. Puske lopputulos GitHubiin.

Gitin historia
--------------

Kun projekti etenee ja siihen luodaan lisää commiteja, ne synnyttävät yhdessä projektin historian. Gitin historia tarkoittaa siis ketjua, joka syntyy kun committeja on luotu peräjälkeen.

Projektin historian säilyttäminen on yksi versionhallinan suurimmista eduista. Se mahdollistaa esimerkiksi historiassa takaisin palaamisen, jos kehityksessä on lisätty jokin toimimaton ominaisuus.

### Historian tarkasteleminen

Projektin historia näkyy helposti GitHubissa. Tarkastellaan historiaa ensin sitä kautta.

Navigoidessa projektin sivulle yläpalkissa on ensimmäisenä vasemmalla välilehti, josta pääsee tarkastelemaan committeja. Esimerkiksi alla näkyvässä kuvassa kyseisessä välilehdessä lukee “4 commits”.

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/FdVeqUzxm4BNO0LgWNiN7gAfg4eD1X.png)

Kun välilehden avaa, näkee allekkain kaikki tehdyt commitit. Oikeassa reunassa näkyy kolme nappia.

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/75CrbgxrkPJOwxvDQl2x9yiPyuUTTF.png)

Napeista keskimmäisessä näkyy tietyn commitin id:n alkuosa. Kyseistä nappia painamalla on mahdollista nähdä kaikki commitissa tehdyt muutokset. Lisäykset näkyvät vihreällä, ja poistot punaisella.

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/jwKZUuLK5mj9MX1nTY4TFuDzj9RfDm.jpg)

Painamalla seuraavaksi “Browse files”, tai edellisestä näkymästä oikeanpuolimmaista `<>`\-painiketta, pääsee tarkastelemaan _koko projektia_ kyseisessä commitissa. Commit siis sisältää pelkästään muutokset, mutta Git mahdollistaa koko projektin tilan tarkastelemisen tietyn commitin jälkeen. Pääset palaamaan takaisin mainiin, eli päähaaran viimeisempään committiin painamalla vasemmalla olevaa hakemistopuuta kuvaavalla ikonilla varustettua painiketta, jossa lukee tarkastelussa olevan commitin tunniste, ja valitsemalla avautuvasta valikosta `main`.

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/yIWdhn09XOvBL7YtCY7xYkAO7Abkhk.png)

Saman voi tehdä myös komentorivillä. Kun ollaan Git-projektin kansiossa, tiettyyn committiin voidaan siirtyä komennolla `git checkout commitin_id`. Tämä vastaa samaa, kuin GitHubissa koko projektin tilan tarkasteleminen tietyn commitin jälkeen. Samalla tavalla takaisin viimeisimpään committiin pääsee komennolla `git checkout haarannimi`, eli yleisimmässä tapauksessa `git checkout main`. Yksittäisen commitin muutoksia voidaan tarkastella komennolla `git show commitin_id`.

Tehtävä:

Salaisuus


-----------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

1.  Luo projektiisi uusi tiedosto `salaisuus.txt`, ja kirjoita sisään esimerkiksi "tämä on hyvin salainen salaisuus".
2.  Tee commit salaisuuden lisäämisestä.
3.  Poista sen jälkeen tiedosto `salaisuus.txt`, ja tee poistosta uusi commit.
4.  Puske muutoksesi GitHubiin.
5.  Navigoi GitHubissa projektiisi. Etusivulla salaisuutta ei näy. Käy etsimässä salaisuus projektin historiasta. Etsi salaisuus sen jälkeen myös komentoriviltä.

##### Mieti tarkkaan mitä julkaiset

Tämä on muistutus, että etärepositorioon ei pidä puskea mitään salaista: ei salasanoja, henkilökohtaisia API-avaimia, tai opiskelijanumeroa, tai muutakaan, mitä ei halua julkaista koko maailmalle.

GitHubin workflow
-----------------

GitHubin kaltaiset palvelut helpottavat merkittävästi yhteisten projektien kehittämistä. Käyttäjät huomaavat projektien ongelmat parhaiten. Projektille voi tehdä GitHubissa _issuen_, ja kertoa ohjelman vajaavaisuuksista. Tavallisimpia issueiden aiheita ovat bugit ohjelman toiminnassa, ongelmia asennuksessa, tai puuttuvat toiminnallisuudet.

Jos tietää ongelman ratkaisun, voi sitä ehdottaa projektin omistajalle koodin muodossa. GitHubissa sijaitsevan projektin voi kopioida kokonaisuudessaan omalle koneelleen komennolla `git clone`. Komento ottaa argumentiksi repositorion osoitteen, jonka saa projektikansion oikeasta yläkulmasta vihreästä napista.

![Add alt](https://courses.mooc.fi/api/v0/files/course/a5f7ec37-3848-4392-8d07-13f5dc688181/images/6BTzFQgH4sI2RpxT1MqvCVD7PnSh71.png)

Kyseessä on siis sama osoite, joka annettiin aikaisemmin `git remote add`\-komennolle argumentiksi. Projektin omistaja ei saa ilmoitusta siitä, että hänen projektinsa on kloonattu.

Jatkossa, kun aloitat uuden Git-projektin, on olemassa kaksi vaihtoehtoa etärepositorion linkittämiseksi. Voit joko luoda projektin ensin komentoriviltä komennolla `git init` ja lisätä sen jälkeen projektille etärepositorion. Toinen vaihtoehto on ensin luoda GitHubissa repositorio, ja kloonata sitten tyhjä projekti koneelle.

Jotta kloonaamaansa repositorioon tekemänsä muutokset voi puskea takaisin etärepositorioon, projektin omistajan tulee [lisätä kloonaaja projektin kehittäjäksi](https://help.github.com/articles/inviting-collaborators-to-a-personal-repository/). Muussa tapauksessa komento `git push` ei onnistu. Yhteisissä koodiprojekteissa voidaan siis luoda Git-projekti, jonka etärepositoriossa kaikki osallistujat ovat kehittäjinä, jolloin kaikki voivat vapaasti lisätä projektiin koodia.

On kuitenkin myös toinen tapa ehdottaa muutoksia olemassaolevaan projektiin: _fork_. Kun forkkaa projektin, kopio siitä lisätään käyttäjän omaksi repositorioksi hänen omaan profiiliiinsa. Tästä tulee ilmoitus GitHubin “feediin”, ja projektin omistaja voi nähdä, kuka on forkannut projektin. Kun olet forkannut projektin, voit kloonata oman kopiosi koneellesi tavalliseen tapaan _omasta profiilistasi_, ja puskea muutoksia _omaan kopioosi_.

Jos oman kopioosi tekemäsi muutokset ovat mielestäsi niin hyviä, että haluat ehdottaa niitä myös alkuperäiseen projektiin, sen voi tehdä [pull requestin](https://help.github.com/articles/about-pull-requests/) avulla. Tällöin alkuperäisen projektin omistaja voi halutessaan liittää mergen avulla muutoksesi projektiinsa.

Tehtävä:

Kloonaaminen


--------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

1.  Selvitä ensin Googlen avulla, miten saat selville komentoriviltä Git-projektin etärepositorioiden nimet ja osoitteet. Kyseessä on siis komento, joka ajetaan Git-projektin sisällä, kun sille on asetettu etärepositorio.
2.  Etsi vapaavalintainen [vapaan lähdekoodin](https://en.wikipedia.org/wiki/Open-source_software)\-projekti GitHubista (esim. [VarjoCafe](https://github.com/orfjackal/varjocafe) tai jokin [TKO-älyn projekti](https://github.com/TKOaly)). Kloonaa se ensin koneellesi. Selvitä sitten, minkä nimiseksi etärepositorio asetetaan automaattisesti kloonatessa. Voit tehdä tämän ajamalla edellisessä kohdassa selvittämäsi komennon kloonatun projektin sisällä.

Tehtävä:

Toisen projektin tutkiminen


-----------------------------------------

Kirjaudu sisään, jotta voit vastata tehtävään.

Ohjeet

Tutki sen jälkeen jonkin vapaan lähdekoodin projektin repoa GitHubissa. Etsi, mistä löydät projektin issuet ja pull requestit. Etsi myös projektiin osallistuneet (_contributors_) ja heihin liittyvä statistiikka.

Loppusanat
----------

Vasta-alkajana yhteistyöprojekteissa versionhallinnan avulla hukkaa ja rikkoo helposti koodia. Versionhallinnan käyttäminen koodaamisessa on kuitenkin eräs tärkeimmistä koodarin taidoista. Vaikka työpaikalla ei käytettäisi Gitiä, pätevät versionhallintaohjelmiin usein samat periaatteet.

Jos törmäät outoon virheeseen, kysy rohkeasti apua, äläkä ajele sokkona komentoja. Pitkälle pääsee pitämällä silmällä `git status`\-komennon tulosteita, puskemalla varmuuskopioita ajoittain, ja kommunikoimalla muiden projektilaisten kanssa muuallakin kuin commit-viesteissä. Gitiä oppii parhaiten käyttämällä sitä. Älä siis lannistu ja poista projektia heti epäonnistuessasi. Pahimmassa tapausessa voi aina kloonata projektin uudestaan, kunhan on muistanut siirtää työnsä GitHubiin.

On jälleen aika hengähtää ja pitää tauko. Anna mielesi levätä, ennen kuin palaat materiaaliin ja sen oppimistavoitteisiin.

Lisää Gitistä voi lukea esimerkiksi seuraavista lähteistä:

*   [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
    
    *   Pro Git Book on kohtuullisen raskas, mutta erittäin kattava dokumentaatio Gitistä. Kannattaa käyttää yksittäisen asian opiskelemiseen. Kokonaan läpi rämpiminen voi olla turhan pitkäveteinen operaatio.
    
*   [http://ohshitgit.com/](http://ohshitgit.com/)
    
    *   Apuja yleisiin ongelmatilanteisiin hauskasti puettuna.
    *   Komennot sisältävät jonkin verran Gitin historian ylikirjoittamista, mitä emme tässä osassa käsitelleet, ja saattaa siten joskus viedä ojasta allikkoon. Voi kuitenkin olla nopea apu epätoivon hetkinä, ja erityisesti ensimmäinen komento, `git reflog`, pelastaa tilanteissa, joissa on onnistunut sekoittamaan koko pakan.
    
*   [https://try.github.io/](https://try.github.io/)
    
    *   GitHubin tutoriaali, joka alkaa ihan perusasioista. Käsittelee joitain asioita, joita ei käyty läpi tässä osassa, kuten `git diff` ja komentoriviltä haarojen yhdistäminen.
    
*   Mikäli olet jo tutustunut Gittiin jonkin verran, saatat olla kiinnostunut oppimaan lisää Gitin historiasta. Historian säilyttäminen, jota demonstroitiin esimerkiksi salaisuus-tehtävässä, mahdollistaa myös sen muokkaamisen jälkikäteen. Vanhaa sanontaa mukaillen, _Voittajat kirjoittavat historian, ja mokailijat ylikirjoittavat Gitin historian_. Historian muokkaaminen on kuitenkin varsin vaarallista erityisesti yhteistyöprojekteissa, sillä sen avulla voi pilata muiden ihmisten koneilla olevia versioita. Jos olet kuitenkin edelleen kiinnostunut, Atlassanilla on erikseen tutoriaali [historian ylikirjoittamisesta](https://www.atlassian.com/git/tutorials/rewriting-history), sekä muita [edistyneempiä tutoriaaleja](https://www.atlassian.com/git/tutorials/advanced-overview).

P.S Mikäli olet läsnäoleva opiskelija yliopistossa, kannattaa käydä tarkistamassa GitHub student packin [tarjoukset](https://education.github.com/pack/offers). Tarjolla on krediittejä esimerkiksi DigitalOcean- ja AWS-palveluihin, sekä etuja myös itse GitHubiin.