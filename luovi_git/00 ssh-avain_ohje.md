


# GitHub SSH-avain: Luonti ja käyttöönotto

Tämä ohje opastaa, kuinka luot SSH-avaimen työasemallasi ja liität sen GitHub-tiliisi, jotta voit käyttää GitHubia turvallisesti ilman salasanaa.

## Vaihe 1: Tarkista, onko sinulla jo SSH-avain

Avaa pääte (Terminal / Komentorivi) ja suorita:

```bash
ls -al ~/.ssh

# GitHub SSH-avain: Luonti ja käyttöönotto
## Vaihe 1: Tarkista, onko SSH-avain jo olemassa

```bash
ls -al ~/.ssh
```

Jos näet tiedostot `id_ed25519` ja `id_ed25519.pub`, siirry vaiheeseen 3.

## Vaihe 2: Luo uusi SSH-avain

```bash
ssh-keygen -t ed25519 -C "sinun.sahkoposti@example.com"
```

Hyväksy oletuspolku painamalla Enter.
Salasana (passphrase) on valinnainen.

## Vaihe 3: Käynnistä ssh-agent ja lisää avain

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

## Vaihe 4: Kopioi julkinen avain

macOS / Linux:
```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

Windows:
```bash
clip < ~/.ssh/id_ed25519.pub
```

## Vaihe 5: Lisää avain GitHubiin

GitHub → Settings → SSH and GPG keys → New SSH key  
Title: esim. Työkone  
Key: liitä kopioitu avain

## Vaihe 6: Testaa yhteys

```bash
ssh -T git@github.com
```

Onnistunut vastaus:
```text
Hi käyttäjänimi! You've successfully authenticated
```

## Käytä jatkossa repoissa SSH-osoitetta

```text
git@github.com:kayttaja/repo.git
```
