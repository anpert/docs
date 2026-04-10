# GIT JA GITHUB – PIKAOHJEET
## PAIKALLISEN REPOSITORYN LUOMINEN
1.	Mene haluamaasi kansioon.
2.	Avaa komentokehote tai PowerShell.
3.	Anna komento:
```
git init
```
4.	Lisää tiedostot versiohallintaan:
```
git add .
```
5.	Tee ensimmäinen commit:
```
git commit -m "Initial commit"
```
________________________________________
## ETÄREPOSITORYN HAKEMINEN PAIKALLISEKSI
1.	Kopioi GitHubista HTTPS- tai SSH-osoite.
2.	Avaa komentokehote aiottuun hakemistoon.
3.	Kloonaa:
```
git clone <url>
```
4.	Mene kloonattuun hakemistoon:
```
cd <hakemisto>
```
________________________________________
## REPOSITORYN LUOMINEN GITHUBIIN
1.	Kirjaudu GitHubiin.
2.	Valitse "New".
3.	Anna repolle nimi ja valitse public/private.
4.	Luo repository ilman README:ä (jos sinulla on jo paikallinen repo).
5.	Liitä paikallinen GitHubiin:
```
git remote add origin <repo-url>
git branch -M main
git push -u origin main
```
________________________________________
## FORKIN LUOMINEN ETÄREPOON
1.	Avaa GitHubissa jonkun muun repository.
2.	Klikkaa "Fork".
3.	Nyt sinulla on oma kopio (fork) omassa GitHubissasi.
4.	Kloonaa oma fork paikalliseksi:
```
git clone <oma-fork-url>
```
________________________________________
## FORKIN PÄIVITYS ALKUPERÄISEEN ETÄREPOON
(eli pidä oma fork ajan tasalla upstreamin kanssa)
1.	Mene paikalliseen hakemistoosi.
2.	Lisää upstream-osoite (vain kerran):
```
git remote add upstream <alkuperäisen-repon-url>
```
3.	Hae muutokset:
```
git fetch upstream
```
4.	Sulauta (yleisin tapa):
```
git merge upstream/main
```
5.	Lähetä päivitetty fork GitHubiin:
```
git push
```
________________________________________
## PAIKALLISEN REPOSITORYN PÄIVITYS (kun haluat uusimmat GitHubista)
1.	git pull
(Hakee ja sulauttaa origin/main-haaran muutokset.)
2.	Jos tulee konflikteja, korjaa tiedostot ja tee commit:
```
git add .
git commit
```
________________________________________
## KESKEISET MUUT PERUSTOIMINNOT
Muutosten lisääminen commitia varten:
```
git add <tiedosto>
tai kaikki:
git add .
```
Commitointi:
```
git commit -m "Kuvaava viesti"
```
Tilanteen tarkistus (mitä on muuttunut):
```
git status
```
Tiedostohistorian katselu:
```
git log
```
Uuden haaran luominen:
```
git checkout -b <haara-nimi>
```
Haaran vaihto:
```
git checkout <haara-nimi>
```
Haaran yhdistäminen toiseen:
```
git merge <haara-nimi>
```
Etärepo-osoitteiden tarkistus:
```
git remote -v
Muutosten lähetys GitHubiin:
```
git push
```
