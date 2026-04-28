# Contributing Guidelines

Tämä projekti käyttää **sosiaalista kontrollia** versionhallinnassa.  
Kaikkien tiimin jäsenten on sitouduttava seuraaviin sääntöihin, jotta koodi pysyy laadukkaana ja historia selkeänä.

---

## 1. Haarat

- Kaikki kehitys tehdään omassa haarassa.
- Haaran nimeäminen:  
  - `feature/<aihe>` – uusi toiminnallisuus  
  - `bugfix/<aihe>` – virheenkorjaus  
  - `hotfix/<aihe>` – kiireellinen korjaus  

Esim: `feature/login-form`, `bugfix/null-pointer`

---

## 2. Commit-käytännöt

- Käytä selkeitä, kuvaavia commit-viestejä.
- Yksi commit = yksi looginen muutos.
- Aja lint/format ja testit ennen committia.

---

## 3. Pull Request (PR)

- Kaikki koodi tuodaan **Pull Requestin kautta mainiin**.
- Tekijä ei saa yhdistää omaa PR:ään.
- PR:ään täytetään kuvaus (mitä tehtiin, miksi, miten testattu).
- Pienet PR:t ovat suositeltavia (helpompi tarkistaa).

---

## 4. Katselmointi

- Vähintään yksi muu tiimin jäsen tarkistaa PR:n.  
- Integraattorit (valitut henkilöt) vastaavat hyväksynnästä ja yhdistämisestä.  
- Hyväksyntä annetaan selkeästi (`LGTM`, `Approved`, tms.).

---

## 5. Yhdistäminen (Merge)

- Käytetään aina **Squash & Merge** -tapaa.  
- Tämä pitää historian siistinä: yksi PR = yksi commit.  
- PR:n jälkeen kehityshaara poistetaan.

---

## 6. Julkaisut ja tagit

- Jokainen yhdistetty PR voi sisältää versionnoston.
- Integraattori lisää tarvittaessa tagin (`vX.Y.Z`) ja kirjaa lyhyen muutospäiväkirjan.

---

## 7. Poikkeustilanteet (Hotfix)

- Kiireelliset korjaukset tehdään `hotfix/*` -haarassa.
- Silti PR luodaan ja toinen tiimin jäsen hyväksyy, vaikka tarkastus olisi nopeutettu.
- Ei koskaan suoraa pushia mainiin.

---

## 8. Kiellettyä

- **Ei suoria committeja mainiin.**
- **Ei omien PR:ien yhdistämistä.**
- **Ei ohitetun tarkistuksen yhdistämistä.**

---

## 9. Miksi tämä on tärkeää

- Yhtenäinen historia ja selkeä audit trail.
- Koodi tarkistetaan aina vähintään kahden silmän toimesta.
- Virheet havaitaan aikaisemmin.
- Jokainen PR jää dokumentoiduksi.

---

Sitoutumalla tähän prosessiin varmistamme, että projektimme pysyy hallittavana ja laadukkaana.
