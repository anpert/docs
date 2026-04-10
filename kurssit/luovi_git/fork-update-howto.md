# FORKIN PÄIVITYS

Oletetaan, että sinulla on:
- oma forkattu repo GitHubissa (esim. joku-tunnus/jokurepo)
- alkuperäinen repo (esim. luovi/jokurepo)
ja haluat päivittää oman forkisi alkuperäisen uusimpaan versioon.

## Vaiheittaiset ohjeet (komentorivillä):

### 1. Siirry paikalliseen forkkiisi:
```
cd polku/kansioosi
```
### 2. Tarkista, että sinulla on alkuperäinen repo lisättynä upstream-etänä:
```
git remote -v
```

Jos näkyy vain esim.
```
origin  https://github.com/joku-tunnus/jokurepo.git
```
niin lisää alkuperäinen repo:
```
git remote add upstream https://github.com/site/jokurepo.git
```

Jos saat virehilmoituksen `error: remote upstream already exists`, voit mennä eteenpäin. Tämä tarkoittaa sitä, että upstream on olemassa ja käytettävissä. Voit mennä eteenpäin. 

Tarkista kuitenkin, että antamasi komento osoitti juuri siihen origiin, johon halusit.

### 3. Hae alkuperäisen repon (upstreamin) uusin sisältö:
```
git fetch upstream
```

Saat vastaukseksi ehkä jotain tyyliin

```
From https://github.com/site
 * [new branch] main -> upstream/main
 ```

### 4. Vaihda omaan päähaaraasi (yleensä main, jossain vanhoissa: master):

```
git checkout main
```

Jos tässä vaiheessa tulee ilmoitus **tiedoston_nimi: needs merge
error: you need to resolve your current index first** tarkoittaa se, että olet "merge/rebase/cherry-pick-operaation" keskellä. Tarkista tilanne komennolla `git status`. 

* Jos lukee **“You are in the middle of a merge”**, olet mergessä. Siellä voi lukea myös **"You have unmerged paths."**. Näiden kahden ilmoituksen hoto tehdään samalla tavalla.
* Jos lukee **“rebase in progress”**, olet rebassa.
* Jos lukee **“You have unmerged paths”**, sinulla on ratkaisemattomia konflikteja.

Jatkoon on kaksi vaihtoehtoa:

#### Vaihtoehto A: Perutaan nykyinen operaatio (helpoin, jos et tarvitse sitä)

**Merge kesken:**
```
git merge --abort
```

**Rebase kesken:**
```
git rebase --abort
```

Sitten vaihda main-haaraan:
```
git checkout main
```
#### Vaihtoehto B: Viimeistellään nykyinen operaatio (jos haluat pitää tehdyn työn)

1. Näytä konfliktit:
```
git status
```

2. Avaa konfliktitiedostot, poista merkit <<<<<<<, =======, >>>>>>> ja tee valinnat. Paikallinen versio on ======= - viivan yläpuolella, upstreamin versio alapuolella

```bash
<<<<<<< HEAD
oma versio
=======
upstreamin versio
>>>>>>> upstream/main
```

3. Merkitse ratkaistuiksi ja tee commit:
```
git add .
# jos kyseessä MERGE:
git commit
# jos kyseessä REBASE:
git rebase --continue
```

Toista kunnes git status kertoo, ettei keskeneräistä operaatiota ole.

Sen jälkeen:

```
git checkout main
```




### 5. Yhdistä (merge tai rebase) upstreamin muutokset omaan haarasi:
* Merge-menetelmä (helpoin ja turvallinen):
```
git merge upstream/main
```

* Tai rebase (siistimpi historia):
```
git rebase upstream/main
```

### 6. Päivitä GitHubiin (oma forkki):

```
git push origin main
```

### 🔍 Tarkista tulos

Nyt GitHubissa näkyvä forkki on päivitetty alkuperäisen repon mukaiseksi.
Voit varmistaa GitHubissa, että commit-historia on samassa linjassa.


---
---

## Vaiheittaiset ohjeet GitHUb sitella

### 1. Avaa oma forkkisi
* Mene GitHubissa omaan forkkirepoosi, esimerkiksi 
```
https://github.com/joku-tunnus/jokurepo
```

### 2. Tarkista, onko se jäljessä alkuperäisestä
Yläreunassa (repo-sivun ylälaidassa) näkyy usein ilmoitus tyyliin ```This branch is X commits behind luovi:main.```

Voi olla myös toisin päin: ```This branch is 35 commits ahead of site/tiedosto:main.```

Jos näitä ei näy, voit hypätä seuraavien yli kohtaan 3. 

#### olet edellä (ahead):
* Vaihtoehto 1: Pidät oma muutokset
Jos haluat vain säilyttää omat lisäyksesi eikä sinun tarvitse päivittää mitään: Ei tarvitse tehdä mitään. Forkkisi on edellä ja toimii täysin normaalisti. Voit jatkaa kehittämistä forkissa kuten ennenkin.

* Vaihtoehto 2:Lähetä muutokset alkuperäiseen (Pull Request)
  * Jos haluat, että alkuperäinen repo saa nämä commitit:
  * 1. Avaa forkkisi GitHubissa (esim. github.com/anpert/jokurepo)
  * 2. Yläreunassa näkyy nappi “Contribute” → klikkaa sitä
  * 3. Valitse “Open pull request”
  * 4. GitHub näyttää vertailun: 
    * Base repository: luovi/jokurepo
    * Head repository: anpert/jokurepo
  * 5. Tarkista, että vertaus on oikein (base = alkuperäinen, head = oma)
  * 6. Lisää otsikko ja kuvaus → klikkaa “Create pull request”
  * → Nyt alkuperäisen repon ylläpitäjät voivat tarkastaa muutoksesi ja yhdistää ne.

* Vaihtoehto 3: Peru omat muutokset ja palauta fork alkuperäisen tilaan
  * Jos haluat, että forkkisi on täsmälleen sama kuin alkuperäinen, ilman omia committeja:
  * GitHubin selaimessa ei ole suoraa nappia “Reset fork to upstream”, mutta voit tehdä sen näin:
    * Avaa forkkisi GitHubissa
    * Mene Pull requests-välilehdelle
    * Klikkaa New pull request
    * Vasemmalle valitse anpert/jokurepo:main
    * ja oikealle luovi/jokurepo:main
    * GitHub näyttää ilmoituksen:
    * ```“luovi:main is ahead of anpert:main by X commits”```
    * Klikkaa “Create pull request”, nimeä esim. “Sync to upstream”
    * Kun PR on tehty, GitHub antaa napin “Merge pull request” — klikkaa sitä → forkkisi päivitetään alkuperäisen mukaiseksi.

### 3. Käytä “Sync fork” -painiketta

klikkaa ensin ▼ main (branch-valikko) ja varmista, että olet päähaarassa (yleensä `main`).


GitHub tarjoaa nykyään nopean synkronoinnin:
* Klikkaa Sync fork -painiketta (näkyy yleensä commit-listan tai branch-näkymän yläpuolella).
* Valitse avautuvasta valikosta **Update branch**.

GitHub yhdistää (merge) muutokset automaattisesti alkuperäisestä repoista sinun forkkiisi.

### 🔍 Tarkista tulos

Kun päivitys on valmis:
* sivun ylälaidassa näkyy ilmoitus **“This branch is up to date with luovi:main”**
* commit-lista on sama kuin alkuperäisessä repossa.

### Vinkki
Jos “Sync fork” -painike ei näy:
* Mene kohtaan **Pull requests → New pull request**
* Valitse vasemmalle oma forkki (joku-tunnus/jokurepo:main)
ja oikealle alkuperäinen (luovi/jokurepo:main)
* GitHub ehdottaa “There isn’t anything to compare” (jos ajan tasalla)
tai vaihtoehtoisesti “Create pull request” (jos päivitettävää löytyy).
* Tee tällöin **'“pull request”** omalle haarallesi — GitHub tekee yhdistämisen puolestasi.

## Pari sanaa versioiden päivittymisestä
Molemmissa edellämainituissa on otettu huomioon se, että sekä forkki että upstream ovat voineet kehittyä. Tämän edellytyksenä on se, että ollaan huolellisia.

### Komentorivimenetelmä (git remote / fetch / merge / push)
* ```git fetch upstream``` hakee *alkuperäisen repon uusimmat commitit*, mutta ***ei koske vielä forkkiisi***.
* ```git merge upstream/main``` (tai ```rebase```) **yhdistää nämä muutokset** omaan ```main```-haaraasi paikallisesti.
* ```git push origin main``` **vie päivitykset GitHubin forkkirepoon** (eli remote päivittyy).

Tuloksena GitHubin forkki sisältää nyt kaikki alkuperäisen muutokset **sekä mahdolliset omat lisäyksesi**.<br>
Jos upstreamissä tulee myöhemmin uusia päivityksiä, voit toistaa vaiheet 3–6.

## GitHubin selainmenetelmä (Sync fork / Update branch)
* #**Sync fork → Update branch**” hakee alkuperäisen (```upstream```) repon päähaaran uudet commitit ja **mergaa ne automaattisesti forkkisi päähaaraan GitHubin palvelimella**.
* Se tekee siis käytännössä saman kuin ```git fetch + merge + push```, mutta ilman paikallista kloonia.

Forkkisi GitHubissa pysyy jatkuvasti ajan tasalla alkuperäiseen nähden, kun käytät Sync fork -toimintoa aina, kun upstream päivittyy.