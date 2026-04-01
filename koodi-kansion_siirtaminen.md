# Koodi- kansion siirtäminen Windowsissa pois OneDrive-kansiosta

* lähtötilanne: Koodi-kansio on OneDrive-kansion alla, ja se synkronoituu OneDriven kanssa. Tämä voi aiheuttaa ongelmia, esim. siksi, että Koodi- kansioon voi kertyä todella paljon tiedostoja. Samoin OneDrivessä on omat tapansa ylläpitää tiedostojen kirjanpitoa.
* Kun avaat koodi- kansion resurssienhallinnassa, katso, näetkö osoitepalkissa "OneDrive" tai vastaavaa. Jos näet sen, koodi- kansio on OneDrive-kansion alla.

```
C:\kayttajat\omatunnus\omakansio\
└─ tiedostot-kansiot (joka synkronoituu OneDriveen)\
   └─ koodit
   │  └─ projekti1\
   │  │  └─ .git\
   │  └─ projekti2\
   │     └─ .git\
   └─ tekstitiedostot-kansio\
   │
   └─ kuvat-kansio\
jne...
```
Ongelma on siis vain nuo koodi-kansion alla olevat Git-repositoryt, jotka synkronoituu OneDriveen. Muut voivat jäädä tuonne. 

OneDrive hoitaa näiden muiden varmuuskopioinnin ja synkronoinnin. Koodit synkronoidaan GitHubiin, joka on tarkoitettu koodin varmuuskopiointiin ja jakamiseen. Näin saadaan molempien maailmojen parhaat puolet: OneDrive dokumenteille ja GitHub koodille.


* eli: siirretään koodit pois OneDriveen menevistä

* tavoite: GitHub‑repositoryt ovat
  * paikallisesti koneella
  * ei OneDrivessa
  * Git toimii normaalisti (git status, push, pull)
  * koodi pidetään ajan tasalla GitHubin kautta

```
C:\kayttajat\omatunnus\omakansio\
└─ tiedostot-kansiot (joka synkronoituu OneDriveen)\
│  └─ tekstitiedostot-kansio\
│  │
│  └─ kuvat-kansio\
└─ koodit
      └─ projekti1\
      │  └─ .git\
      └─ projekti2\
         └─ .git\   
jne...
```
# Vaiheet:
1. sulje VSode tai muu koodin keihittelyssä olleet ohjelmat
2. varmista, että kaikki repositoryt ovat ajan tasalla:
   * siirry repon kansioon
   * kirjoita `git status` varmistaaksesi, että kaikki on commitattu
   * jos on jotain commitattavaa, tee se: `git add .`, `git commit -m "viestisi"`, `git push`
   * toista tämä kaikille repositoryille, jotka ovat koodi-kansion alla 
3. Voit vielä lopuksi tehdä OneDriveen kansion, jonka nimeksi kirjoitat vaikkapa "**EI_KOODIA_TÄNNE**"<br><br>
4. Sitten siirrytään pois OneDrivestä: Luo uusi kansio, johon haluat siirtää koodit. Esimerkiksi `C:\kayttajat\omatunnus\koodit` 
   * huom. älä tee sitä OneDrive-kansion alle. Esim. Documents, Desktop, Pictures... muuten ollaan takaisin lähtötilanteeseen.
5. Siirry tuohon uuteen kansioon resurssienhallinnassa.
6. siirry komentetilaan (kirjoita otsikkorivillä "cmd" ja paina Enter)
7. hae kaikki repositoryt git.hub:sta. Tässä vaiheessa voit käyttää muistilistana sitä ONeDrivessä olevaa koodi-kansiota.
8. anna koodi: ```git clone https://github.com/kayttaja/repo1.git```
9. toista tämä kaikille repositoryille, jotka olivat koodi-kansion alla
   * 



