# Paikallisen repositoryn perustaminen

## Perustetaan ilman valmista kansiota
1. Avaa komentorivi. Anna komento<br>
```git init projektinimi```

## Perustetaan aiemmin perustettuun kansioon
1. Avaa komentorivi. Luo uusi kansio
```mkdir projekti```.
2. Siirry kansioon: ```cd polku/kansioon```.
5. Alusta uusi Git-repo: ```git init```
6. Lisää kaikki tiedostot versiointiin: ```git add .```

## Tuodaan etärepon sisältö
1. siirry kansioon ```cd projektinimi```
2. anna komennot 
   ```
   git remote add origin
   https://github.com/organisaatio/repo.git

   git pull origin main
   ```
Tuon remote add origin- jälkwiawn polun saat suoraan GitHubin nettisivun URL:sta.

### Tarkistus
1. siirry kansioon ```cd projektinimi```
2. Tarkista että kaikki toimii: ```git status```.
3. Jos näet ```nothing to commit, working tree clean```, repo on kunnossa.
4. Voit tehdä myös ensimmäisen committisi (tässä vaiheessa ei oikeastaan tapahdu mitään näkyvää):<br>```git commit -m "Ensimmäinen commit"```