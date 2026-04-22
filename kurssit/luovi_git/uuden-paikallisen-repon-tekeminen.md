# Paikallisen repositoryn perustaminen

## Vaihtoehto 1: Perustetaan repositorio ilman valmista kansiota

1. Avaa komentorivi.
2. Luo ja alusta uusi repositorio yhdellä komennolla:
   ```bash
   git init projektinimi
   ```
3. Siirry kansioon:
   ```bash
   cd projektinimi
   ```

## Vaihtoehto 2: Perustetaan repositorio aiemmin luotuun kansioon

1. Avaa komentorivi.
2. Luo uusi kansio:
   ```bash
   mkdir projekti
   ```
3. Siirry kansioon:
   ```bash
   cd projekti
   ```
4. Alusta Git-repositorio:
   ```bash
   git init
   ```
5. Lisää kaikki tiedostot versiohallintaan:
   ```bash
   git add .
   ```

## Etärepositorion (remote) liittäminen ja sisällön tuonti

> Käytä tätä vain, jos GitHub-repositorio on jo olemassa ja se on tyhjä tai haluat yhdistää paikallisen kansion siihen.

1. Lisää etärepositorio (URL GitHubista):
   ```bash
   git remote add origin https://github.com/organisaatio/repo.git
   ```
2. Nouda sisältö:
   ```bash
   git pull origin main
   ```

> Jos GitHub-repositoriossa on jo README tms., tämä vaihe on pakollinen ennen pushia.

## Ensimmäinen commit ja julkaisu GitHubiin

1. Lisää tiedostot (jos ei vielä tehty):
   ```bash
   git add .
   ```
2. Tee ensimmäinen commit:
   ```bash
   git commit -m "Ensimmäinen commit"
   ```
3. Aseta päähaara ja lähetä GitHubiin:
   ```bash
   git branch -M main
   git push -u origin main
   ```

## Tarkistus

1. Tarkista repositorion tila:
   ```bash
   git status
   ```
2. Jos näet:
   ```text
   nothing to commit, working tree clean
   ```
   repositorio on kunnossa.