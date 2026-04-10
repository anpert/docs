# 🤝 Yhteistyö – TVTC:n ohje avoimeen repositoryjen käsittelyyn

Tervetuloa mukaan! Tämä repo noudattaa **PR-virtausta**: älä puske suoraan `main`-haaraan, vaan tee työsi omassa haarassa ja avaa **Pull Request** (PR).

---
### 0. Jos sinulla ei ole vielä tarvittavaa repoa omalla koneellasi, tässä ohjeet
---
 _(huom. tämä tehdään yleensä vain kerran per repository)_:
* siirry koodikansioosi
* luo sinne kansio, jolle annat nimeksi repositoryn nimen
* (voit tarkistaa, että se ei ole jo repo: __git status__. Hyppää seuraavan kohdan yli) 
* anna koodi: 
```bash
git init -b main
```
* (voit käydä kopioimassa etärepon osoittee. Se on 
  * (HTTPS-muodossa): https://github.com/kayttaja/projekti.git tai
  * (SSH:muodossa): SSH: git@github.com:kayttaja/projekti.git
* hae etärepon sisältö omaan koneeseesi (tässä https- muoto, voit vaihtaa myös SSH- muodon):
```bash
git remote add origin https://github.com/kayttaja/projekti.git
git pull origin main
```


## 1. Päivitä main (tee nämä omassa työasemassasi).
Tästä työ yleensä alkaa. Eli että sinulla on käytössäsi tuorein versio. Tee tämä siinä kansiossa, joka on omalla työasemallasi. Samat ohjeet kouluun ja kotiin.

```bash
git checkout main
git pull origin main
```

## 2. Luo oma haara (branch):

Anna nimeksti _oma_githubtunnus_tiedoston_nimi_. Alla näkyy tuo __heebo_tietokanta.py__ esimerkkinä

```bash
git checkout -b feat/heebo_tietokanta.py
```
Huom. anna omille oksille (branch) luokittelu näin:
* __feat__: uusi ominaisuus käyttäjälle (ei uusi ominaisuus build-skriptiin)
* __fix__: käyttäjää koskeva bugikorjaus (ei build-skriptin korjaus)
* __docs__: muutoksia dokumentaatioon
* __style__: koodin ulkoasun tai muotoilun muutos (puuttuvat puolipisteet jne.; ei vaikutusta tuotantokoodiin)
* __refactor__: tuotantokoodin uudelleenjärjestely (esim. muuttujan uudelleennimeäminen)
* __test__: testien lisääminen tai muokkaaminen (ei vaikutusta tuotantokoodiin)
* __chore__: ylläpitotehtävä, kuten automaatiotyökalujen päivitys (ei vaikutusta tuotantokoodiin)

## 3. add ja commit
Tee muutokset tiedostoon. Muista tallettaa.
Aja add. Laita committiin lyhyt viesti siitä, mitä olet tehnyt:
```bash
git add .
git commit -m "Korjattu tekstiä kohdasta..."
```
_korvaa (lainausmerkkien välissä oleva teksti todellisella asialla :) )_

Pidä commit-viestit lyhyinä ja kuvaavina:
* Imperatiivissa eli käskymuoto: Lisää, Korjaa, Päivitä
    * Esim. Lisää lomakevalidointi sähköpostille
    * Korjaa virheellinen polku asetuksissa


## 4. push
MAINIIN EI SAA PUSKEA!<br>
Tee Push omaan branch, jonka aiemmin teit (<mark>ei siis mainiin</mark>)<br> 
Käytä tuolla aikaisemmin antamaasi nimeä:
```bash
git push origin feat/heebo_tietokanta.py
```

## 5. github.com
Siirry Github.com:iin. Aloitetaan Pull Request. Tarkoituksena saada tekemäsi muutokset tarkistettua ja liitettyä yhteiseen koodiin. Tai sitten johonkin vaihtoehtoisene polkuun.

### Pull requestun täydentäminen
* Siirry oikeaan repositoryyn
* Valitse Pull Request (ylävalikossa)
* Etsi oma Pull Requestisi eli muutospyyntösi
* Klikkaa <span style="background-color: green;">Compare & Pull request</span>
* Korjaa tarvittaessa otsikkoa ("Add a title"). Sen pitää olla ytimekäs ja selkeä. Otsikot tyyliin "fix stuff" ei ole hyviä
* Kirjoita description- osaan tarkempaa tietoa. Mitä muuttui, miksi, miten sen voi testata. Oikean koodin kanssa voit kokeilla myös Copilotin esitarkistusta.
* Käytä allaolevaa pohjaa (kopioi ja täydennä. Käytä .md- muotoa):

```
    ### Mitä tehtiin?
    - 

    ### Miksi?
    - 

    ### Miten testata?
    1) 
    2) 

    ### Muuta huomioitavaa
```

* Tarkoitus on, että pyydät jotain toista henkilöä tarkistamaan koodi ja liittämään se main- haaraan. Liitä henkilön tunnus @- merkin avulla. Kirjoita @ ja Github näyttää listan tunnuksista.
* Paina lopuksi "Create pull request"
*Älä jatka PR:n käsittelyä enää itse. Joku toinen ottaa sen käsittelyyn.
*Kun saat tietää, että muutos on hyväksytty, poista tekemäsi haara (tässä esimerkissä oli se hrrbo_tietokanta.py)
* sen jälkeen päivitä oma haara ajantasalle mainista rebase-tyylillä
```
 git checkout feat/oma-nimi-tehtava
 git fetch origin
 git rebase origin/main
```

### Pull requestin (PR) ottaminen käsittelyyn
* Jos sait kutsun tarkistaa PR tai näet listalla aukiolevan PR:n...
* Tarkista koodi. Voit täydentää kommenttiosaa (ruudun alaosassa, "Add a comment") 
* testaa koodi paikallisesti
* voit korjata koodia
* kun kaikki on kunnossa, valitse alasvetovalikosta "Squash and merge"
* kun merge on tehty, käy poistamassa tekemäsi haara (branch)

### Jos syntyy konflikteja, ratkaise → jatka
git add .
git rebase --continue

### Vaihtoehtona merge
git merge origin/main



Vinkki (valinnainen, paikallinen suojavyöhyke): lisää kehittäjien koneille pre-push hook, joka estää pushin mainiin.

🙋 Usein kysyttyä

* Q: Unohdin ja pushasin mainiin – mitä nyt?<br>
A: Ilmoita heti opettajalle/tiimille. Tehdään korjaus PR:llä tai palautetaan commitit ohjeen mukaan.

* Q: PR:ssä on “Conflicting files”.<br>
A: Päivitä haara:
```
    git checkout feat/oma-nimi-tehtava
    git fetch origin
    git rebase origin/main   # tai git merge origin/main
    # Ratkaise konfliktit → add → rebase --continue (tai committaa merge)
    git push -f origin feat/oma-nimi-tehtava  # rebasen jälkeen tarvitaan -f
```

* Q: Kuka hyväksyy PR:n?<br>
A: Reviewerinä toimii opettaja/tiimiläinen. Odota hyväksyntää ennen mergeä.

📜 Koodin laatu & tyyli
* Pidä funktiot ja tiedostot pieninä ja selkeinä.
' Lisää testit, kun korjaat bugeja tai lisäät uusia ominaisuuksia.