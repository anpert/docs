# 💡 Git-muistilista

## 📚 Sisällysluettelo

- [💡 Git-muistilista](#-git-muistilista)
  - [📚 Sisällysluettelo](#-sisällysluettelo)
  - [Perusasetukset](#perusasetukset)
  - [Repositorion luominen ja kloonaus](#repositorion-luominen-ja-kloonaus)
  - [Tilanne ja versiohistoria](#tilanne-ja-versiohistoria)
  - [Muokkaus ja versiointi](#muokkaus-ja-versiointi)
  - [Haarat (branchit)](#haarat-branchit)
  - [Etärepositorio (origin)](#etärepositorio-origin)
  - [Git-kansion siirtäminen ylemmälle tasolle (Windows)](#git-kansion-siirtäminen-ylemmälle-tasolle-windows)
    - [Tilanne](#tilanne)
  - [Vinkkejä ja lisäkomentoja](#vinkkejä-ja-lisäkomentoja)
  - [Windows- komentokehotteen työkaluja](#windows--komentokehotteen-työkaluja)
  - [tiedostojen siirtä githubissa reposta toiseen](#tiedostojen-siirtä-githubissa-reposta-toiseen)
    - [TAPA 1: Siirrä tiedostot ilman historiaa (helppo)](#tapa-1-siirrä-tiedostot-ilman-historiaa-helppo)
  - [TAPA 2: säilytä historia - kopioi osan toisesta reposta](#tapa-2-säilytä-historia---kopioi-osan-toisesta-reposta)
  - [TAPA 3: Forkkaa/klonaa ja valikoi](#tapa-3-forkkaaklonaa-ja-valikoi)
- [Tiedostojen ja kansioiden siirto Git hubissa](#tiedostojen-ja-kansioiden-siirto-git-hubissa)
- [!!!](#)

---

## Perusasetukset

```bash
git config --global user.name "Etunimi Sukunimi"
git config --global user.email "sahkoposti@example.com"
git config --global init.defaultBranch main
```

---

## Repositorion luominen ja kloonaus

```bash
git init                 # Luo uusi (paikallinen) Git-repositorio nykyiseen kansioon
git clone <repo-url>     # Kloonaa olemassa olevan (etä-)repositorion
```

---

## Tilanne ja versiohistoria

```bash
git status                  # Näytä nykyinen tila (muutetut/tallentamattomat)
git log                     # Näytä commit-historia
git log --oneline --graph   # Tiivis ja visuaalinen näkymä haaroista
```

---

## Muokkaus ja versiointi

```bash
git add tiedosto.txt       # Lisää yksittäinen tiedosto commitia varten
git add .                  # Lisää kaikki muutokset
git commit -m "Viesti"     # Tee commit annetulla viestillä
git commit -am "Viesti"    # Lisää ja commitoi kaikki muutetut tiedostot
```

---

## Haarat (branchit)

```bash
git branch                 # Näytä kaikki haarat
git branch uusi-haara      # Luo uusi haara
git checkout uusi-haara    # Vaihda uuteen haaraan
git checkout -b uusi-haara # Luo ja vaihda haaraan yhdellä komennolla
git merge toinen-haara     # Yhdistä toinen haara nykyiseen
```

---

## Etärepositorio (origin)

```bash
git remote -v                    # Näytä etäyhteydet
git remote add origin <url>      # Lisää etärepositorio
git push -u origin main          # Puske ja aseta oletushaaraksi main
git pull origin main             # Vedä uusimmat muutokset
git push                         # Puske muutokset etäpalvelimelle
```

---

## Git-kansion siirtäminen ylemmälle tasolle (Windows) ##
### Tilanne ###
Paikallinen Git-repositorio on väärässä kansiossa, esimerkiksi:
```
C:\Käyttäjät\Nimi\projekti\alikansio\  ← täällä on .git-kansio
```
Tarkoitus on siirtää kaikki tiedostot (myös piilotiedostot) kansiosta `alikansio` ylemmälle tasolle `projekti`. 

Voit tehdä nämä toimenpiteet Widowsin resurssimanagerilla. Kun siirrät piilotetun .git -tiedosto, onnistuu koko toimenpide tällä tiedostojen siirtämisellä.

## Vinkkejä ja lisäkomentoja

```bash
git diff                  # Näytä erot edelliseen commitin
git stash                 # Piilota keskeneräiset muutokset
git stash pop             # Palauta stashatut muutokset
git reset --hard HEAD     # Palauta kaikki edelliseen commitin tilaan
git clean -fd             # Poista kaikki versioimattomat tiedostot ja kansiot
```

---

## Windows- komentokehotteen työkaluja
```bash
move kansio\tiedostonimi kohde  # siirrä tiedostot:
move alikansio\* .
move alikansio\.git .
```

## tiedostojen siirtä githubissa reposta toiseen
* Tässä kolme tapaa ja niissäkin eri vaihtoehtoja.
* Jos siirrät paljon tai monimutkaisia kokonaisuuksia ja haluat säilyttää versionhallinnan historian, käytä Tapa 2 tai 3.
* Jos kyseessä on yksittäisiä tiedostoja tai kansion siirto, Tapa 1 riittää.

### TAPA 1: Siirrä tiedostot ilman historiaa (helppo) ###
Jos et tarvitse commit-historiaa mukaan:
* Vaihtoehto A: GitHub-verkkosivulla
  * Avaa lähderepo GitHubissa.
  * Mene tiedostoon tai kansioon, jonka haluat siirtää.
  * Kopioi tiedoston/kansion sisältö.
  * Avaa kohderepo.
  * Lisää uusi tiedosto tai muokkaa olemassa olevaa ja liitä sisältö.
  * Tee commit.
* Vaihtoehto B: Gitillä koneella
```bash
  # 1. Kloonaa kohderepo koneelle (tai käytä jo kloonattua)
  git clone https://github.com/oma-kayttaja/kohderepo.git
  cd kohderepo

  # 2. Kopioi tiedostot toiseen kansioon
  cp -r /polku/lähderepo/tiedosto .  # tai useita tiedostoja

  # 3. Lisää, commitoi ja puskuroi
  git add .
  git commit -m "Lisätty tiedosto toisesta reposta"
  git push
```

## TAPA 2: säilytä historia - kopioi osan toisesta reposta
Jos haluat säilyttää historiatiedot tietyistä tiedostoista (hieman edistyneempi)
```bash
  # 1. Kloonaa kohderepo
  git clone https://github.com/oma-kayttaja/kohderepo.git
  cd kohderepo

  # 2. Lisää lähderepo etärepona
  git remote add lähde https://github.com/oma-kayttaja/lähderepo.git
  git fetch lähde

  # 3. Tuo haluamasi hakemisto historia mukaan (esim. "src")
  git subtree add --prefix=src lähde/main --squash
  # tai jos haluat koko historialla:
  # git read-tree --prefix=src/ -u lähde/main

  # 4. Pushaa
  git push
```

## TAPA 3: Forkkaa/klonaa ja valikoi
Jos haluat isomman määrän tiedostoja valikoiden ja haluat säilyttää koko historian, kannattaa:

1. Kloonata lähderepo.
2. Käyttää git filter-repo (tai vanhaa git filter-branch) rajataksesi historia.
3. Pushata tulos kohderepoon.

# Tiedostojen ja kansioiden siirto Git hubissa
...ei onnistu. Github ei tue suoraan tätä toimintaa. Sen sijaan toimi näin:
huom. **Tämä on hidas jos tiedostoja on paljon — silloin Git on parempi**.

Vaihe 1: Mene lähderepoon
1. Avaa selain ja siirry GitHubissa siihen repositorioon, jossa kansio sijaitsee.
2. Avaa kansio, jonka haluat siirtää.
3. Avaa jokainen tiedosto yksi kerrallaan.
4. Kopioi sisällöt leikepöydälle (Ctrl + A → Ctrl + C).

Vaihe 2: Mene kohderepoon
1. Avaa toinen selainvälilehti ja mene kohderepoon.
2. Navigoi siihen kansioon, mihin haluat lisätä tiedoston (tai luo uusi).
3. Paina "Add file" > "Create new file".
4. Anna uusi polku muodossa:
```bash
  uusi-kansio/tiedoston_nimi.ext
```
Esim.:
```bash
  siirretty_kansio/myfile.py
```
Liitä kopioitu sisältö kenttään ja paina "Commit changes".
Toista tämä kaikille kansiossa oleville tiedostoille.



# !!!

📌 **Muista käyttää `git status` usein nähdäksesi tilanteen!**


