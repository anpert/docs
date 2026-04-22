# 🤝 Yhteistyö – TVTC:n ohje avoimeen repositoryjen käsittelyyn

Tämä repository noudattaa **Pull Request (PR) -virtausta**.  
👉 **Älä puske suoraan `main`-haaraan.** Tee työsi omassa haarassa ja avaa Pull Request.

---

## 0. Repositorion tuominen omalle koneelle (tehdään kerran / repo)

> Ohita tämä, jos repo on jo koneellasi (`git status` toimii).

1. Siirry omaan koodikansioosi.
2. Luo kansio repositorylle ja siirry siihen.
3. Alusta repo ja liitä etärepo:

```bash
git init -b main
git remote add origin https://github.com/kayttaja/projekti.git
git pull origin main
```

Voit käyttää myös SSH-osoitetta:
```
git@github.com:kayttaja/projekti.git
```

---

## 1. Päivitä main (aloita aina tästä)

```bash
git checkout main
git pull origin main
```

---

## 2. Luo oma haara (branch)

Nimeä muotoon: `tyyppi/githubtunnus_kuvaus`

Esimerkki:
```bash
git checkout -b feat/heebo_tietokanta
```

### Käytettävät etuliitteet
- **feat** – uusi ominaisuus käyttäjälle
- **fix** – bugikorjaus
- **docs** – dokumentaatio
- **style** – muotoilu, ei toiminnallista muutosta
- **refactor** – koodin rakenteellinen muutos
- **test** – testit
- **chore** – ylläpito, automaatio

---

## 3. Tee muutokset, add ja commit

```bash
git add .
git commit -m "Korjaa tietokantahaun virhe"
```

### Commit-viestit
- Käskymuoto: **Lisää**, **Korjaa**, **Päivitä**
- Lyhyt ja kuvaava

---

## 4. Push omaan branchiin (EI mainiin)

```bash
git push origin feat/heebo_tietokanta
```

---

## 5. Pull Request GitHubissa

1. Avaa repository GitHubissa.
2. Valitse **Pull Requests → New pull request**.
3. Valitse oma branch → `main`.
4. Täydennä otsikko ja kuvaus.

### PR-kuvauspohja (Markdown)

```markdown
### Mitä tehtiin?
- 

### Miksi?
- 

### Miten testata?
1) 
2) 

### Muuta huomioitavaa
```

- Pyydä katselmointi (`@kayttajatunnus`)
- Klikkaa **Create pull request**
- Älä mergeä itse, ellei niin ole sovittu

---

## 6. PR:n hyväksynnän jälkeen

1. Poista oma haara GitHubissa.
2. Päivitä paikallinen repo:

```bash
git checkout main
git pull origin main
```

---

## PR:n käsittely (reviewerille)

- Tarkista koodi
- Testaa paikallisesti
- Kommentoi tarvittaessa
- Hyväksy **Squash and merge**
- Poista branch mergauksen jälkeen

---

## Konfliktit (rebase-tyyli)

```bash
git checkout feat/oma-haara
git fetch origin
git rebase origin/main
# Ratkaise konfliktit
git add .
git rebase --continue
git push -f origin feat/oma-haara
```

Vaihtoehto:
```bash
git merge origin/main
```

---

## Usein kysyttyä

**Q: Pushasin vahingossa mainiin**  
A: Ilmoita heti. Korjataan PR:llä tai palaamalla edelliseen commit-tasoon.

**Q: PR:ssä on konflikteja**  
A: Päivitä haara rebasella tai mergellä (ohje yllä).

**Q: Kuka hyväksyy PR:n?**  
A: Opettaja tai nimetty tiimiläinen.

---

## Koodin laatu

- Pidä tiedostot ja funktiot pieniä ja selkeitä
- Lisää testejä bugikorjauksissa ja uusissa ominaisuuksissa