# Ohjeita

## Sisällys
- WINGET – pohdintaa  
  - Winget – syväluotaus  
  - 1. Mikä Winget oikeastaan on?  
  - 2. Vahvuudet  
  - 3. Heikkoudet ja kipupisteet  
  - 4. Vertailu muihin vaihtoehtoihin  
  - 5. Ammattilaisen käyttötapauksia  
  - 6. Mitä tällä tekee käytännössä?  
  - 7. Loppupohdinta  
- WINGET-ohjeita  
  - 1. Onko Winget jo asennettuna?  
  - 2. Sovellusten etsiminen  
  - 3. Sovelluksen asentaminen  
  - 4. Sovellusten päivittäminen  
  - 5. Sovelluksen poistaminen  
  - 6. Hyödyllisiä komentoja  
- Yhteenveto  
- GIT:n asennus Wingetillä  
- Ensimmäiset GIT-harjoitukset  

---

## WINGET – pohdintaa

### Winget – syväluotaus

#### 1. Mikä Winget oikeastaan on?
- **Winget = Windows Package Manager**
- Käyttää Microsoftin omaa pakettivarastoa sekä Microsoft Storea.
- Taustalla se lataa usein suoraan ohjelmien viralliset asennusohjelmat (MSI/EXE), ajaa ne hiljaisessa tilassa ja seuraa tulosta.

> **Huom.** Winget ei ole aivan yhtä “paketoitu” kuin Linuxin `apt` tai macOS:n `brew` – se ei aina hallitse pakettien sisältöä täysin itse, vaan toimii välillä enemmän automaattiasentajana.

#### 2. Vahvuudet
- ✅ **Yksinkertainen peruskäyttö:** yksi komento asentaa ohjelman.  
- ✅ **Yhteensopivuus:** toimii komentorivillä, PowerShellissä, CI/CD-skripteissä.  
- ✅ **Päivitykset helposti:** `winget upgrade --all` pitää ohjelmistot ajan tasalla.  
- ✅ **Integroitu Windowsiin:** ei tarvita kolmannen osapuolen paketinhallintaa kuten Chocolatey tai Scoop.  
- ✅ **Store-integraatio:** sama työkalu hoitaa myös Store-sovellukset.

#### 3. Heikkoudet ja kipupisteet
- ⚠️ **Ei aina deterministinen**  
  - Sama `winget install` voi eri aikaan hakea eri version (repo päivittyy).  
  - Heikompi skriptattavuus, jos tarvitset täysin saman ympäristön toistettavasti (esim. build-server).
- ⚠️ **Asennukset eivät aina ole täysin hiljaisia**  
  - Jotkin paketit avaavat silti asennusikkunan (jos pakettikuvauksessa hiljaisen tilan argumentit puuttuvat/virheelliset).
- ⚠️ **Päivitysten laatu**  
  - Winget-repo on osin yhteisön ylläpitämä. Kaikki paketit eivät päivity automaattisesti.  
  - Joskus `winget upgrade` ilmoittaa “ei päivityksiä”, vaikka uudempi versio olisi olemassa.
- ⚠️ **Rajoitettu konfiguroitavuus**  
  - Ekosysteemi ei ole yhtä monipuolinen kuin `brew` tai `apt`.  
  - Tietyn version ja asetusvalintojen/kohdekansiön tarkka määrittely ei aina onnistu helposti.

#### 4. Vertailu muihin vaihtoehtoihin
- **Chocolatey**
  - Vanhin ja monipuolisin Windowsin pakettimanageri.  
  - Hyvä yrityskäyttöön (enterprise-ominaisuuksia).  
  - Haittapuoli: monet paketit vaativat admin-oikeuksia.
- **Scoop**
  - Kevyt ja “nörttimäinen”. Asentaa usein ilman rekisteriä (ZIP-paketeista).  
  - Helppo hallita eri versioita (`scoop install git@2.42`).  
  - Sopii, jos haluat softat eristyksiin ja helposti poistettaviksi.
- **Manuaaliasennus (EXE/MSI)**
  - Täysi kontrolli, mutta ei automaatiota.  
  - Hyvä, jos tarvitset tarkan version hallintaa tai ohjelmaa, jota ei ole wingetissä.

#### 5. Ammattilaisen käyttötapauksia
- 💡 **DevOps / CI/CD**
  - Voit skriptata dev-ympäristön pystytyksen Winget-komennoilla.  
  - Hyöty: nopea onboarding uusille kehittäjille.  
  - Haitta: versioiden epädeterministisyys voi rikkoa buildit.
- 💡 **Portable-softien hallinta**
  - Winget ei ole tässä vahvimmillaan (painotus EXE/MSI).  
  - Portable-binaareihin **Scoop** on usein parempi.
- 💡 **Käyttäjä vs. järjestelmänlaajuinen asennus**
  - Wingetillä voi asentaa käyttäjäkohtaisesti tai koko koneelle, mutta kaikki paketit eivät tarjoa valintaa → sekaannuksia.

#### 6. Mitä tällä tekee käytännössä?
1. **Peruskäyttöön:** Winget – integroitu, helppo, nopea.  
2. **Vakaisiin build-ympäristöihin:** usein mieluummin Scoop (tarkka versiohallinta, vähemmän yllätyksiä).  
3. **Yritys-IT:** Chocolatey + keskitetty hallinta.  
4. **Oma läppäri:** Winget yleissoftille + manuaaliasennus erikoisille + tarvittaessa Scoop dev-työkaluille.

#### 7. Loppupohdinta
Winget on loistava peruspakettimanageri Windowsiin, mutta ei vielä yllä Linuxin tai Macin tasolle. Se on hyvä ammattilaiselle, joka haluaa nopeutta ja integraatiota, mutta huono silloin kun tarvitaan täysin toistettavia ja deterministisiä ympäristöjä.  
Moni päätyy hybridiin: **Winget** yleiseen softaan + **Scoop** dev-työkaluille + **manuaaliasennus** kriittisille ohjelmille.

---

## WINGET-ohjeita

Winget on pakettienhallinta Windows 11:ssä. Se on vähän kuin Linuxin `apt` tai `yum`: sillä voi asentaa, päivittää ja poistaa ohjelmia komentoriviltä.

### 1. Onko Winget jo asennettuna?
Windows 11:ssä Winget tulee yleensä valmiina osana *App Installer* -sovellusta.

```powershell
winget --version
```

Jos saat versionumeron, Winget on käytössä. Muussa tapauksessa asenna Microsoft Storesta App Installer.

### 2. Sovellusten etsiminen
```powershell
winget search git
```

Listaa mm. virallisen Git-paketin Git.Git.

### 3. Sovelluksen asentaminen

Kun tiedät paketin tunnisteen (esim. Git.Git):

```powershell
winget install --id Git.Git -e --source winget
```

* --id = tarkka paketin nimi
* -e = exact match (välttää väärät osumat)
* --source winget = käytä virallista lähdettä

Winget ratkaisee ohjelman asennuspolun ja -kansion omatoimisesti. Lähtökohtaisesti näin. <br>Voit vaikuttaa asennuskansioon joissain tapauksissa mutta tässä vaiheessa tähän ei kannata puuttua.

### 4. Sovellusten päivittäminen

Yksittäinen ohjelma:
```powershell
winget upgrade Git.Git
```

Kaikki kerralla:
```powershell
winget upgrade --all
```

### 5. Sovelluksen poistaminen
```powershell
winget uninstall Git.Git
```
### 6. Hyödyllisiä komentoja

Asennettujen listaus:
```powershell
winget list
```

Paketin tiedot:
```powershell
winget show Git.Git
```
### Yhteenveto
1. Tarkista `winget --version`.
2. Hae ohjelma: `winget search <nimi>`.
3. Asenna: `winget install --id <nimi> -e`.
4. Päivitä: `winget upgrade --all`.
5. Poista: `winget uninstall <nimi>`.