Versionhallinta
===============
lähteet: Lähteenä on käytetty Heksingin Yliopiston kurssia "Tietokone työvälineenä, luku 2: Versionhallinta" 
(https://courses.mooc.fi/org/uh-cs/courses/tietokone-tyovalineena/chapter-2)
Materiaaliin on lisätty lisää ohjeita ja harjoituksia.

Helsingin Yliopiston palvelussa on kokoelma hyviä tehtäviä. Nämä löytyvät tekstin lomasta. Tehtävien pisteet näet Yliopiston kurssin etusivun kohdasta [Tehtävät tässä luvussa](https://courses.mooc.fi/org/uh-cs/courses/tietokone-tyovalineena/chapter-2). 


Sisällys: (rivin lopussa on kurssitiedoston numero)
- [Kurssin tavoitteet](#kurssin-tavoitteet) (1)
- [Versionhallinta, Git ja Git-hub](#versionhallinta-git-ja-github) (1)
- [Yleisesti Git:stä ja Github:sta](#yleisesti-gitistä-ja-githubista) (1)
- [Git- projektin aloittaminen](versionhallinta_02.md#git--projektin-aloittaminen) (2)
- [Commit](versionhallinta_02.md#commit) (2)


## Kurssin tavoitteet ##
_(älä välitä, jos nämä vaikuttavat oudoilta käsitteiltä...!!)_

Tavoitteena on, että kurssin käytyäsi...
- ymmärrät, mitä hyötyä versionhallinnan käyttämisestä on,
- osaat luoda paikallisen Git-repositoryn ja välittää sen eri välivaiheiden kautta git.hub:iin
- tiedät, mikä on fork ja osaat käyttää sitä,
- osaat kloonata Git-projektin omalle koneellesi,
- osaat käyttää GitHubia SSH-yhteyden kautta,
- ymmärrät, miten Gitiä ja GitHubia voidaan hyödyntää yhteistyössä,
- ymmärrät, miten merge-konflikti muodostuu,
- osaat ratkaista merge-konfliktin,
- osaat hakea tietoa Gitin käytöstä internetistä.


## Versionhallinta: Git ja Github ##
Tässä osassa käsitellään versionhallintaa. Versionhallinta tarkoittaa palvelua, joka säilöö koodia. Sen käyttöön on pääsääntöisesti kaksi motiivia. 
  1) Versionhallinnan avulla voidaan pitää varmuuskopioita sekä ohjelman nykyisestä, että aiemmista versiosta. 
  2) Lisäksi sen avulla voidaan helposti jakaa koodia muille, sekä osallistua muiden projekteihin.

Versionhallintatyökalujen avulla on mahdollista merkitä jokin projektin tila sellaiseksi, että siihen voidaan palata myöhemmin. Näin ollen, jos jotain menee pieleen uusien ominaisuuksien kehityksessä, voidaan palata aikaisempaan, toimivaan versioon. Versionhallinnassa pidetään tallessa kaikkia merkittyjä tiloja. Silloin nähdään, miten ohjelman kehitys on edistynyt, milloin ja millaisia muutoksia ollaan tehty, ja kenen toimesta. Tämä helpottaa myös esimerkiksi suurempien bugien, eli ohjelman toiminnassa esiintyvien virheiden metsästystä.

Koodaaminen tapahtuu useimmiten ryhmässä. Versionhallintatyökalujen avulla ihmisten on mahdollista käyttää ja kehittää toistensa tekemää koodia, jopa tapaamatta koskaan toisiaan fyysisesti. Projekteille on mahdollista antaa  sanallista palautetta, kuten vikailmoituksia. Gi.hubin kautta on myös mahdollista antaa konkreettisia parannusehdotuksia, koodaamalla joku kohta paremmin. Lisäksi kaikki tekijät näkevät koodin kehityskaaren, jolloin on helpompi tehdä yhteistyötä.

Voit lukea versionhallinan hyödyistä Atlassian Bitbucketin sivulta (https://www.atlassian.com/software/bitbucket). 

Git on eräs versionhallintatyökalu. Tässä osassa käsitellään Gitin ja siihen liittyvän GitHub-palvelun käyttöä erityisesti koodiprojektien kontekstissa.

## Yleisesti Gitistä ja Githubista ##
**Gitin** on luonut *Linus Torvalds*. Torvalds tunnetaan luultavasti parhaiten Linux-kernelin kehittäjänä. Tämä kernel toimii “sydämenä” monille erittäin suosituille käyttöjärjestelmille, kuten Googlen Androidille. 

Torvalds kehitti Gitin nimenomaan omiin tarpeisiinsa koodatessaan Linux-kerneliä. Hän tarvitsi työkalun, jolla voi säilyttää eri versioita omasta koodistaan, sekä jakaa sitä muiden kehitykseen osallistuneiden kanssa.

**GitHub** on myöhemmin kehitetty palvelu, jonka avulla voidaan säilyttää ja julkaista Git-projekteja. GitHubiin verrannollisia palveluita on useita. Esimerkiksi **Gitlab**.

Gitiä ja GitHubia käytetään yleisesti työelämässä. Niitä voi käyttää muussakin kuin vain koodin tallenuksessa. Voit esimerkiksi tallettaa omat CV:si ja muut tekstidokumentit Githubiin. 

Tässä osassa keskitytään lähinnä koodin jakamiseen Gitin avulla GitHubissa, ja siinä usein kohdattuihin ongelmiin.

## Gitin asennus ##

Tässä ohjeet git:n asentamiseen.
1. Lataa git:n asenuspaketti osoitteesta https://git-scm.com/downloads.
2. Käynnistä asennus. Seuraa ruudulle tulevia ohjeita.
3. Testaa asennuksen onnistuminen käynnistämällä __Git Bash__.

# 2. Git termejä

## git- hakemisto
Git- hakemisto on omalla koneellasi oleva kansio. Se sisältää tiedostot, versiohistorian ja muita tietoja. 

Kun tietokoneen kansio määritellään git- kansioksi, sinne talletetaan erityinen tiedosto nimeltään __.git__. Jos poistat kansiosta tuon tiedoston, tulee kansiosta jälleen tavallainen tietokoneen kansio. 

Kansiossa voi olla myös muita git:iin liittyviä tiedostoja. Esimerkiksi
* .gitignore: git-hakemistossa oleva tiedosto, jossa kerrotaan mitkä tiedostot ja kansiot jätetään pois repositoryn muutoksista. Huomaa piste tiedoston nimen alussa. Piste estää tiedosto näkymisen normaalissa tiedostoliastauksessa (ls, dir).
* .gitmodules: git- hakemistossa oleva tiedosto, joka sisältää tiedot käytetyistä alimoduuleista

Seuraavassa on lista git:iin liittyvistä käsitteitä. Voit hypätä ne yli ja palata niihin myöhemin.

## 2.2 Repository / "Repo"

"Repository" on Gitin käytön perusta, se sisältää tiedostot, versiohistorian ja
muita tietoja. Repository sijaitsee git-kansiossa. Git- kansion poistaminen poistaisi itse repositoryn.
Lisäksi voi olla muita tiedostoja kuten .gitignore ja .gitmodules

## 2.3 Remote
Git remote on ***repository***, joka sijaitsee jossain muualla kuin .git hakemistosi sisällä. Se voi olla talletettuna git.hubiin. Joissain tilanteissa remotea kutsutaan nimellä origin.

## 2.4 Commit

"Commit" tarkoittaa muutosta repositoryyn, esimerkiksi tiettyyn koodiriviin tai
tiedoston poistoon. Git pitää muutoksista historiaa, joka mahdollistaa sen,
ettei jokaisesta eri versiosta tarvitse pitää täydellistä kopiota. Git myös
mahdollistaa aikaisempaan versioon palaamisen, jos esimerkiksi uusin muutos
aiheuttaa ongelmia tai vikoja.

Commit on myös komento, jolla muutokset toteutetaan. Puhekielessä tätä kutsutaan "committaamiseksi".

## 2.5 Branch

"Branchejä" ("präntsi", "branchi") käytetään kehitysversioiden erittelyyn. Yleensä on ainakin
* julkaisu-branchi, jossa on ohjelmiston uusin stabiili versio ja
* kehitys-branchi, jossa päivitetään ja lisätään ominaisuuksia.

Branchien nimet eivät välttämättä ole samat joka projektissa. Joissakin ne on master/develop, joisasakin muissa stable/master. 

On tärkeää, että projektin branchien nimet eivät muutu projektin elämän aikana, sillä tämä tekee versiohistoriasta hyödytöntä. Jos nimi muutetaan, esim. bisect-komento ei enää toimi. 

Branchit voidaan luokitella muuttuvuusasteikolla; kehitys-branchit muuttuvat nopeammin kuin julkaisu-branchi. 

## 2.5 Tag, "tägi" , "tagi"
Tagi on erityinen nimi projektin tietylle versiolle, joiden avulla tärkeät
versiot eivät huku muuhun versiohistoriaan. Tagit yleensä viittaavat
julkaisuversioihin. Jos käyttäjällä kohtaa ohjelmistossa häiriön, tagin nimellä
voidaan selvittää että onko vika jo korjattu uudemmassa versiossa.

## 2.6 Bisect

Bisect on hakutyökalu, jolla voi löytää ominaisuuden tai vian alkuperän.
Komennolle annetaan vanha versio ilman muutosta, ja uusi versio, jossa on
muutos. Komento sitten käyttää puolitushakua löytämään version, jossa vika
ilmaantuu ensimmäistä kertaa.

## 2.7 Merge

Yhdistäminen (“merge”) tarkoitta kahden eri branchin liittämistä toisiinsa.
Yhdistämisristiriita (“merge conflict”) tapahtuu silloin, kun liitettävät
branchit sisältävät samanlaisia muutoksia, jota ei voida automattisesti
ratkaista. Ristiriitojen selvityksessä (“conflict resolution”) ihminen valitsee
muutoksista halutut osat.

## 2.8 Diff

Diff-työkalulla voi katsoa, mitä muutoksia eri versioiden välillä on tapahtunut.
Sitä voi käyttää löytämään omia vahingollisia muutoksia ennen kuin talletat ne.

## 2.9 Submodule

Git sisältää mahdollisuuden alimoduuleille, nämä on tarkoitettu käytettäväksi
silloin, jos tarvitaan toinen repository, kuten koodikirjasto riippuvuutena
omalle projektille ilman että siitä pidettäisiin täysi kopio projektin
repositoryssä, mikä sotkisi versiohistoriaa muun kuin oman koodin muutoksilla.

## 2.10 Stage

Stage on gitissä alue jonne kerätään muutoksia jotka ollaan lisäämässä
repositoryyn commitilla.


>--------
>Tehtävä 1: [siirry tekemään tehtävä](https://courses.mooc.fi/org/uh-cs/courses/tietokone-tyovalineena/chapter-2#b1a897c8-f0bc-4bb3-8127-cfe16a87b65d)

>--------
>Tehtävä 2: [siirry tekemään tehtävä](https://courses.mooc.fi/org/uh-cs/courses/tietokone-tyovalineena/chapter-2#080acdf1-0f5f-4bf9-88a5-861bc6e64bd3)



