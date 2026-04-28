# Ohjeet github classroomin tehtävien antamisesta

## Käsite‑analogiat: oma malli → GitHub Classroom

| Sinun käsitteesi         | GitHub Classroomissa |
|--------------------------|----------------------|
| Antamani tehtäväluettelo | Assignments (tehtävät Classroomissa) |
| Yksittäinen tehtävä      | Assignment (linkki, joka luo repositoriot) |
| Opiskelijan palauttama uusi tehtävä | Opiskelijan oma private repository (assignment‑repo) |
| Palautus                 | Commit / push opiskelijan repossa |
| Palautuksen määräaika    | Deadline (assignmentin asetuksissa) |
| Arvioidut tehtävät       | Reviewed repos (opettajan tekemät kommentit, PR:t, commit‑kommentit)|

## Koodaustehtävän jakaminen Github classroomin kautta
### Tehtävärepositoryn muodostaminen:
* tämän repositoryn pitää olla **template** muodossa
* repositoryn nimeä kuvaavasti, esim. *python-if-tehtava-template*.
* muodosta repo. Anna sille nimeksi vaikkapa *python-if-tehtava-tempplate*.
* ennen käyttöönottoa repossa pitää olla vähintään yksi **commit**.
* tee se commit vaikka nyt. Ainakin itse tehtävä on hyvä olla commitattuna, jotta opiskelijat näkevät, mitä heidän pitää tehdä. Voit committaa myös täydennettävän koosdin, joka on valmiiksi, jotta opiskelijat näkevät, mistä lähteä liikkeelle.
* klikkaa Settings, avaa General
* etsi kohta "Template Repository". Laita sen kohdalle ✅rasti.
* tallenna
* varmista viimeistään nyt, että repositoryn on  sinun tai organisaatiosi omistama  
* luo se organisaatiosi alle

### Tehtävän perustaminen
* siirry Github classroomiiin https://classroom.github.com/classrooms
  * valitse ryhmä, johon haluat antaa tehtävän. klik.
  * klikkaa <span style="background-color:green; color:white; padding:4px;">New assignment</span> (tehtävän luonti).
    * **assignment title**: kirjoita tehtävän nimi, esim. "**Tehtava-1-Hello-World**"
    * **deadline**: aseta tehtävälle määräaika, jonka jälkeen opiskelija ei enää voi palauttaa tehtävää.
    * **cutoff date**: aseta tehtävälle "kova määräaika", jonka jälkeen opiskelija ei enää voi palauttaa tehtävää.
    * **individual assignment**: valitse tämä, jos haluat, että jokaisella opiskelijalla on oma private repository, johon hän palauttaa tehtävänsä. Opiskelijat eivät näe toistensa tehtäviä, mutta opettaja näkee kaikki.
    * **group assignment**: valitse tämä, jos haluat, että kaikki opiskelijat tekevät tehtävän yhdessä (yhteinen repository). Tämä on hyvä vaihtoehto, jos haluat harjoitella projektityötä. Opiskelijat näkevät toistensa tehtävät kuten myös opettajakin.
    * klikkaa <span style="background-color:green; color:white; padding:4px;">Continue</span> (tehtävän luonti).
* seuraavalla sivulla määritellään tehtävään liittyvä repository. 
  * valitse alasvetovalikosta käytettävä template- muotoinen repository
  * määrittele, onko repository yksityinen (private) vai julkinen (public).
  * voit myös määritellä sen, annetaanko opiskelijoille admin-oikeudet heidän muodostamiinsa repositoryihin
  * sivun alareunassa voit määritellä koodiedirotin, jota käytetään tehtävässä. Tämän määrittely ei ole välttämätöntä.

### Tehtävän jakaminen opiskelijoille
* tehtävän luomisen jälkeen sinulle näytetään linkki, jonka kautta opiskelijat voivat hakea tehtävän. Kopioi tämä linkki ja jaa se opiskelijoille esim. Teamsilla.
* opiskelijat hakevat tehtävän klikkaamalla linkkiä, joka vie heidät Github Classroomiin. Heidän pitää kirjautua sisään Github-tilillään, jotta he voivat hakea tehtävän.
* opiskelijat hakevat tehtävän klikkaamalla <span style="background-color:green; color:white; padding:4px;">Accept this assignment</span> (hyväksy tämä tehtävä). Tämän jälkeen Github Classroom luo opiskelijoille repositoryt, joihin he voivat palauttaa tehtävänsä.
* opiskelijat tekevät opiskelijakohtaisessa repositoryssä tehtävän. 
* Valmis tehtävä talletetaan repositoryyn, jonka jälkeen he tekevät commitin ja pushin repositoryynsä. 
* Opiskelijat voivat tehdä useita committeja ja puskea useita kertoja, kunhan he tekevät sen ennen määräaikaa.
* opettaja näkee kaikki opiskelijoiden repositoryt Github Classroomissa. Opettaja voi tarkastella opiskelijoiden tehtäviä, antaa palautetta ja arvioida tehtävät.
* opettaja voi myös luoda pull requestin opiskelijoiden repositoryihin, jos hän haluaa antaa tarkempaa palautetta tai ehdottaa muutoksia. Opiskelijat voivat sitten hyväksyä tai hylätä pull requestin ja tehdä tarvittavat muutokset tehtäväänsä.
* tehtävän arviointi tapahtuu opettajan tekemien kommenttien ja pull requestien kautta. Opettaja voi antaa palautetta suoraan opiskelijoiden repositoryihin tai käyttää Github Classroomin arviointityökaluja, jos sellaisia on käytössä. 
* Opettaja voi myös määritellä arviointikriteerit, jotka auttavat opiskelijoita ymmärtämään, mitä heidän odotetaan saavuttavan tehtävässä.
