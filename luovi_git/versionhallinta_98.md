GIT-perusteet

* ver. 
  * 1.1/2.6.2025        MD- format
  * 1.0/11.1.2022

By: 
* Kristian Ollikainen (TVT C)
* Aino Kortelainen (TVT C) 
* Jyri Lempinen (DATA B) 

- Ohjelmointi 45
- Kevät 2022 
- Tieto- ja viestintätekniikan perustutkinto 
- Ammattiopisto Luovi


# 1. GIT

## Mikä on Git? 

Git on hajautettu versionhallintajärjestelmä, jonka avulla moni henkilö voi työskennellä saman projektin parissa. Git perustuu tiedostojen muutoksiin ja niiden historiaan. 

## Miten Gitiä käytetään? 

Gitiä käytetään joko Git-komentojen kautta tai graafisen sovelluksen (esim. GitHub Desktop) avulla.Käsitteet ja työkalut 

## Repository 

Repository on Gitin käytön perusta, se sisältää tiedostot, versiohistorian ja muita tietoja. Repositoryn tiedot ovat .git kansiossa, jonka poistaminen poistaisi itse repositoryn, lisäksi voi olla muita tiedostoja kuten .gitignore jossa kerrotaan erikseen mitkä tiedostot ja kansiot jätetään pois repositoryn muutoksista, sekä .gitmodules joka sisältää tiedot alimoduuleista. 

## Commit 

Commit tarkoittaa muutosta tiedostoon, esimerkiksi tiettyyn koodiriviin. Git pitää muutoksista historiaa, joka mahdollistaa sen, ettei jokaisesta eri versiosta tarvitse pitää täydellistä kopiota, myöskin voidaan palata takaisin edelliseen muutokset, jos esimerkiksi uusin muutos toi ongelmia tai vikoja mukanaan. 

## Branch 

Branchejä käytetään kehitysversioiden erittelyyn. Yleensä on ainakin julkaisu-branchi, jossa on ohjelmiston uusin stabiili versio; ja kehitys-branchi, jossa päivitetään ja lisätään ominaisuuksia. 

Branchien nimet eivät välttämättä ole samat joka projektissa. Joissakin on master/develop, muissa stable/master. On tärkeää, että projektin branchien nimet eivät muutu projektin elämän aikana, sillä tämä tekee versiohistoriasta hyödytöntä. Jos nimi muutetaan, bisect-komento ei enää toimi. 

Branchit voidaan luokitella muuttuvuusasteikolla; kehitys-branchit muuttuvat nopeammin kuin julkaisu-branchi. Suurille ominaisuuksille (esim. ”pelifysiikka” tai ”uusi tietokantamuoto”) voi olla oma kehitys-branchi. 

## Tag 

Tagi on erityinen nimi projektin tietylle versiolle, joiden avulla tärkeät versiot eivät huku muuhun versiohistoriaan. Tagit yleensä viittaavat julkaisuversioihin. Jos käyttäjällä kohtaa ohjelmistossa häiriön, tagin nimellä voidaan selvittää että onko vika jo korjattu uudemmassa versiossa. 

## Bisect 

Bisect on hakutyökalu, jolla voi löytää ominaisuuden tai vian alkuperän. Komennolle annetaan vanha versio ilman muutosta, ja uusi versio, jossa on muutos. Komento sitten käyttää puolitushakua löytämään version, jossa vika ensiksi ilmaantuu. 

## Merge 

Yhdistäminen (“merge”) tarkoitta kahden eri branchin liittämistä toisiinsa. Yhdistämisristiriita (“merge conflict”) tapahtuu silloin, kun liitettävät branchit sisältävät samanlaisia muutoksia, jota ei voida automattisesti ratkaista. Ristiriitojen selvityksessä (“conflict resolution”) ihminen valitsee muutoksista halutut osat. 

## Diff 

Diff-työkalulla voi katsoa, mitä muutoksia eri versioiden välillä on tapahtunut. Sitä voi käyttää löytämään omia vahingollisia muutoksia ennen kuin talletat ne. 

## Submodule 

Git sisältää mahdollisuuden alimoduuleille eli submodule, nämä on tarkoitettu käytettäväksi silloin, jos tarvitaan toinen repository, kuten koodikirjasto riippuvuutena omalle projektille ilman että siitä pidettäisiin täysi kopio projektin repositoryssä, mikä sotkisi versiohistoriaa muun kuin oman koodin muutoksilla. 


# GitHub  #

## Johdanto ##

GitHub on yksi tunnetuimmista ja suosituimmista Git-verkkopalveluista, muita ovat esimerkiksi GitLab ja BitBucket, mutta näissä ohjeissa keskitytään GitHub palveluun. 

GitHub-tili tarvitaan, jos halutaan saada oma repository verkkoon ja työskennellä muiden kanssa. Github opiskelija-etuudet mahdollistavat GitHub Pro ominaisuuksien käytön ja yhteistyökumppaneiden työkalujen käytön (esim. Microsoft Azure). 

## GitHub-tilin luominen ##

1. Siirry osoitteeseen https://github.com. 
2. Klikkaa sivun oikeasta ylänurkasta ”Sign up”. 
3. Seuraa sivuston antamia ohjeita, käytä koulun sähköpostia tilin luomiseen. 
4. Vahvista tili klikkaamalla sähköpostiin tullutta linkkiä. 

## Github- tilin luominen ##

## Github- opiskelijaoiketuukisen hakeminen ##

1. Siirry osoitteeseen https://education.github.com/pack 
2. Klikkaa vihreää laatikkoa jossa lukee ”Sign up for Student Developer Pack” (ks. kuva 1).
3. Klikkaa sinistä laatikkoa jossa lukee ”Get student benefits” (ks. kuva 2). Kuva, joka sisältää kohteen teksti Kuvaus luotu automaattisesti, KuvaTäytä kohta ”How do you plan to use GitHub?”, voit kirjoittaa esim. ”For school use” ja paina vihreää ”Continue” nappia (ks. kuva 3).  

GitHub vaatii kuvan opiskelutodistuksesta, pyydä sellainen opettajaltasi ja täytä muut pyydetyt kohdat. Kohdat voi täyttää näin: 
What is your school’s website? - https://luovi.fi/. 
How would you describe your school? – 
Kuva, joka sisältää kohteen teksti
Kuvaus luotu automaattisesti, KuvaHigh school. 
How many students are enrolled at your school? – 500 – 1000. 
Street address – Nahkatehtaankatu 3. 
City – Oulu. 
Country – Finland. 
Non-US State or CA Province – Pohjois-Pohjanmaa. 

## SSH-avain ##

SSH-avainta tarvitaan yksityisiä repositoryitä varten, eli repository joita muut eivät pääse näkemään ilman lupaasi. 

SSH-avaimen luonti ja lisäys GitHubiin 

Avaa tietokoneesi komentokehote. 

Kirjoita komento ssh-keygen -t ed25519 -C "oma@sposti.fi" käyttämällä omaa koulun sähköpostia ja paina Enter. 

Avaimen luonti kysyy minne avain tallennetaan, käytä oletusta painamalla Enter. 

Kuva 12, KuvaSeuraavaksi avaimen luonti kysyy salasanaa avaimelle. Jos käytät tietokonetta johon vain sinulla on pääsy, voit luoda avaimen ilman salasanaa painamalla Enter. Tee samoin salasanan vahvistukselle. 

Avain on tallennettu kansioon jonka valitsit kohdassa 3 (esim. C:\Users\käyttäjä/.ssh/id_ed25519.pub). 

Kopioi avaimen sisältö leikepöydälle komennolla clip < avaimenSijainti.pub käyttämällä avaimen sijaintia (esim. clip < C:\Users\käyttäjä/.ssh/id_ed25519.pub). 

Siirry osoitteeseen https://github.com/settings/keys. 

Voit päästä avaimien hallintaan myös klikkaamalla ensin GitHubissa profiilikuvaasi ja valitsemalla ”Settings”, josta löydät vasemmalta laidalta ”SSH and GPG keys” osion (ks. animoitu kuva ja kuva 2).  

 

Kuva, joka sisältää kohteen teksti

Kuvaus luotu automaattisesti, KuvaKlikkaa vihreää ”New SSH key” nappia. 

Liitä aikaisemmalla komennolla kopioitu sisältö ”Key” osioon ja aseta otsikoksi GitHub-tilin sähköposti-osoite (ks. kuva 3).  

Kuva, joka sisältää kohteen teksti

Kuvaus luotu automaattisesti, KuvaKlikkaa vihreää ”Add SSH key” nappia. 

Avain on nyt lisätty ja voit käyttää yksityisiä repositoryitäsi. 

 

 

Gist 

GitHub Gist on yksinkertainen tapa jakaa koodinpätkiä ja muita tekstejä toisille. 

Gist voi olla julkinen (näkyvillä kaikille) tai salainen (näkyy kaikille joilla on linkki). 

Gistin voi kopioida ja, jos olet kirjautunut GitHubiin voit myös kommentoida sitä. 

 

Gistin luominen 

Kuva 15, KuvaGistin luominen tapahtuu painamalla GitHub-sivuston oikeassa ylänurkassa olevaa + nappia ja valitsemalla ”New gist” (ks. kuva 1). 

Tämän jälkeen voit nimetä sinun gistin. Kun se on nimetty voit lisätä koodinpätkän tai muuta tekstiä. Kun se on tehty voit tallentaa gistin vihreästä painikkeesta oikeassa alanurkassa (ks. kuva 2): 

”Create secret gist” vaihtoehdolla, joka tekee gististä salaisen. 

Kuva, joka sisältää kohteen teksti

Kuvaus luotu automaattisesti, Kuva”Create public gist” vaihtoehdolla alanuolen kautta, joka tekee gististä julkisen. 

 

 

Gistin muokkaaminen 

Kuva 20, KuvaJos sinulla on tarve muokata sinun gistiä. Klikkaa ”Edit” painiketta (ks. kuva). Sieltä voit täysin muokata sen tekstiä, otsikkoa ja muuttaa salaisen gistin julkiseksi. Muista! Salaisen gistin voi muuttaa julkiseksi, mutta julkista ei takaisin salaiseksi. 

 

 

Gistin jakaminen 

Jos haluat jakaa sinun gistin, kopioi sivun linkki (esim. ”https://gist.github.com/käyttäjä/abc123/”). 