## 1️⃣ Paikallisen repon luominen, kun kansiota ei ole tehty
```
mkdir projekti
cd projekti
git init
```

Lisää tiedostoja ja tee ensimmäinen commit:
```
git add .
git commit -m "Initial commit"
```

## 2️⃣ Paikallisen repon luominen, kun kansio on jo tehty
```
cd olemassa_oleva_kansio
git init
```

## 3️⃣ Paikallisen repon ensimmäinen siirto GitHubiin

Luo tyhjä repo GitHubissa (älä lisää README:tä).
Yhdistä paikallinen repo GitHubiin:

```
git remote add origin https://github.com/kayttaja/repo.git
```

Lähetä sisältö GitHubiin:
```
git branch -M main
git push -u origin main
```

## 4️⃣ Repon haku paikalliseksi GitHubista (clone)
```
git clone https://github.com/kayttaja/repo.git
cd repo
```
Repo on nyt paikallinen ja origin on valmiiksi asetettu.


## 🧠 Muistisääntö
* git init → paikallisesta reposta liikkeelle
* git clone → GitHubista paikalliseksi
* origin → oma GitHub-repo
* upstream → alkuperäinen repo (forkeissa)