# Henkilön näkymminen GitHub.comissa (vain .MD- versio)

## 🌟 Miksi tuoda itsesi esille GitHubissa?

### 💼 Ammatillinen näkyvyys
- GitHub toimii digitaalisen CV:nä: projektit, koodi, taidot ja lahjat.
- Rekrytoijat ja yhteistyökumppanit voivat helposti nähdä osaamisesi ja tyylisi.
- Selkeä esittely antaa sinusta ammattimaisen kuvan.

### 🧭 Luotettavuus ja yhteistyökyky
- Näkyvä profiili lisää uskottavuutta ja luottamusta työskentelyssä ja yhteisöissä.
- Käyttäjät näkevät, mitä osaat ja mitä projekteja hallitset.

### 🌐 Verkostoituminen
- Mahdollisuus saada kontakteja GitHubin, tiimien, profiilisivun tai blogin kautta.
- Moderoitu kommentointi ja palautteen saaminen.

### 📘 Oppimisen ja kehityksen dokumentointi
- Tallenna projektisi, oppimistehtäväsi ja koodin eri vaiheet yhteen paikkaan.
- GitHub toimii samalla portfoliona ja oppimispäiväkirjana.

### 🧑‍💻 Henkilöbrändin rakentaminen
- Profiilisi on käyntikorttisi: selkeä kuvaus, tyylikäs esittely, linkit ja yhteystiedot.
- Lisää oma kuva, esittelyteksti ja linkki muihin some- tai ammatillisiin kanaviin.

---

## 🧱 GitHub-kotisivujen vaihtoehdot

GitHub tarjoaa kaksi tapaa luoda kotisivu Markdownilla:

| Tapa | Kuvaus | Soveltuu |
|------|---------|-----------|
| **README.md** | Näkyy automaattisesti GitHubin reposivulla. | Profiilissa tai yksittäisissä projekteissa |
| **index.md (GitHub Pages)** | Näkyy GitHub Pages-sivustona selaimessa. | Julkiseen kotisivuun |

GitHub Pages esitellään toisessa ohjeessa.

---

## 📄 README.md

### Mikä se on
- Tiedosto, joka näkyy automaattisesti GitHub-reposi etusivulla.
- Käytetään projektien ja profiilien esittelyyn.

### Sisältöehdotuksia
- Lyhyt esittely, projektit, yhteystiedot.
- Linkkejä ja kuvia.
- Markdownin käyttö tekee rakenteesta siistin ja selkeän.

### Hyödyt
- Helppo ylläpitää.
- Näkyy GitHubissa ilman GitHub Pages -sivua.
- Sopii erityisesti profiilin ja projektien kuvaamiseen.

---

## 🧭 Käyttötapa

1. Luo uusi **repository** nimellä `käyttäjätunnus/käyttäjätunnus.github.io`
2. Lisää juureen tiedosto `index.md`
3. Kirjoita siihen haluamasi sisältö Markdownilla.

Esimerkiksi:

```markdown
# Tervetuloa GitHub-profiiliini!
Tässä on kotisivuni.  
Tässä muutamia projektejani:

- [Projekti 1](https://github.com/kayttajatunnus/projekti1)
- [Projekti 2](https://github.com/kayttajatunnus/projekti2)
- [Projekti 3](https://github.com/kayttajatunnus/projekti3)

Yhteystiedot:  
📧 sähköposti@example.com  
🔗 [LinkedIn-profiilini](https://linkedin.com/in/kayttaja)
```

# ⚙️ GitHub Pages – käyttöönotto-opas
## 1. Luo ja valmistele repository

* Luo repo nimellä käyttäjätunnus.github.io
* Lisää tiedostot kuten index.md, README.md, kuvat jne.

Kansiorakenne voi olla esimerkiksi:
```
repo/
│
├─ index.md
├─ README.md
├─ kuvat/
│   ├─ profiili.png
│   └─ tausta.jpg
└─ projektit/
    ├─ projekti1.md
    └─ projekti2.md
```

### 2. Ota GitHub Pages käyttöön
1. Mene **Settings → Pages**
2. Etsi osa **Build and deployment**
3. Valitse:
   - **Source:** “Deploy from a branch”
   - **Branch:** `main`
   - **Folder:** `/ (root)`
4. Tallenna muutokset.

💡 Sivu julkaistaan automaattisesti osoitteeseen:  
`https://käyttäjätunnus.github.io`

---

### 3. Julkaise ja testaa
- Tee commit ja push `main`-haaraan:
  ```bash
  git add .
  git commit -m "Julkaistu kotisivu"
  git push origin main

* Odota muutama minuutti ja tarkista, että sivu latautuu osoitteessa:
https://käyttäjätunnus.github.io

## 💡 Vinkkejä ja huomioita

- **README.md** näkyy GitHubissa, mutta ei automaattisesti GitHub Pagesissa.  
  Käytä **index.md**-tiedostoa kotisivusi etusivuna.
- Markdowniin voi lisätä kuvia ja linkkejä suhteellisilla poluilla.
- Voit tehdä useita `.md`-tiedostoja ja linkittää ne toisiinsa.
- Jos haluat erillisen projektisivun, luo erillinen repo (esim. `projekti1`) ja ota siellä GitHub Pages käyttöön.
- Jos sivu ei päivity heti, odota hetki tai tyhjennä selaimen välimuisti.
- GitHub Pages tukee myös Jekyll-teemoja, mutta niitä ei tarvita, jos haluat vain Markdown-sivun.
- Kuvia varten on hyvä käyttää omaa `kuvat/`-kansiota ja viitata niihin suhteellisella polulla:  
  `![kuvaus](kuvat/profiilikuva.png)`

## 🔍 Yhteenveto

| Tarkoitus | Tiedoston nimi | Näkyy missä | Paras käyttö |
|------------|----------------|--------------|---------------|
| Profiilisivu GitHubissa | `README.md` | GitHub-profiilin alareunassa | Oma esittely, linkit, CV |
| Käyttäjän kotisivu verkossa | `index.md` | `https://käyttäjätunnus.github.io` | Julkinen verkkosivu |
| Projektin esittely | `README.md` | Projektin GitHub-sivulla | Projektikohtainen kuvaus |
