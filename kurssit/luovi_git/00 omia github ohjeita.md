
# Paikallisen kansion tekeminen GitHub-repositorioksi

## 1. Luo uusi GitHub-repositorio

1. Mene GitHubiin ja kirjaudu sisään.
2. Klikkaa oikeasta yläkulmasta **New repository**.
3. Anna repositoriolle nimi ja valitse **Public** tai **Private**.
4. **Älä** lisää README-, `.gitignore`- tai lisenssitiedostoja tässä vaiheessa.
5. Klikkaa **Create repository**.

## 2. Linkitä paikallinen kansio GitHub-repositorioon

1. Avaa Git Bash (suositeltu) tai komentorivi ja siirry haluamaasi kansioon:
   ```bash
   cd "C:\polku\kansioon"
   ```
2. Alusta Git-repositorio:
   ```bash
   git init
   ```
3. Linkitä paikallinen kansio GitHub-repositorioon  
   (korvaa `<URL>` GitHubista kopioidulla repo-osoitteella, mieluiten SSH-muotoinen):
   ```bash
   git remote add origin <URL>
   ```

## 3. Lisää ja lähetä tiedostot GitHubiin

1. Lisää kaikki tiedostot versiohallintaan:
   ```bash
   git add .
   ```
2. Tee ensimmäinen commit:
   ```bash
   git commit -m "Ensimmäinen commit"
   ```
3. Lähetä tiedostot GitHubiin:
   ```bash
   git branch
