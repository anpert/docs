# Entiteettien sidostyypit:

## 1. One-to-One, 1-1
* Molemmat osapuolet esiintyvät vain kerran suhteessa toisiinsa




```mermaid
erDiagram
        %% Entiteetit
    Asiakas {
        int asiakasnumero PK
        string sukunimi
        string etunimi
        date syntymapvm
    }
```

## 2. One-to-Many, 1-N
* Ensimmäinen entiteetti voi liittyä moneen toiseen, mutta toinen vain yhteen
* `Opettaja ||--o{ Kurssi : "opettaa"`
```mermaid
erDiagram
    henkilö ||--|| henkilötunnus : "omistaa"
```

# 3. Many-to-Many, N-M
* Molemmat voivat liittyä moneen toiseen. 
* Toteutetaan usein liitostaululla (junction entity) 
* **`Opiskelija }o--o{ Kurssi: "osallistuu"`**

```mermaid
erDiagram
    Opiskelija }o--|| Kurssi: "osallistuu"
```

# 4. valinnainen 0..1–N tai 0..n
* Käytetään, kun suhde ei ole pakollinen toiselle osapuolelle
* **`Asiakas o|--o{ Tilaus : "voi tehdä"`**
```mermaid
erDiagram
    Asiakas o|--o{ Tilaus : "voi tehdä"
```

# 4. valinnainen 0..1–N tai 0..n
* Käytetään, kun suhde ei ole pakollinen toiselle osapuolelle
```mermaid
erDiagram
    Asiakas |o--o| Tilaus : "tekee"
```





# ERD-esimerkki: sidostyypit Mermaidilla

```mermaid
erDiagram
    %% Entiteetit
    Opettaja {
        int opettaja_id PK
        string nimi
    }

    Kurssi {
        int kurssi_id PK
        string nimi
        int opintopisteet
    }

    Opiskelija {
        int opiskelija_id PK
        string nimi
        string sahkoposti
    }

    Luokka {
        int luokka_id PK
        string nimi
        int kapasiteetti
    }

    Asiakas {
        int asiakas_id PK
        string nimi
    }

    Tilaus {
        int tilaus_id PK
        date pvm
        string tila
    }

    Ilmoittautuminen {
        int ilmo_id PK
        date pvm
        string tila
    }

    %% 1–1 suhde
    Kurssi ||--|| Luokka : "pidetään"

    %% 1–N suhde
    Opettaja ||--o{ Kurssi : "opettaa"

    %% N–M suhde liitostaululla
    Opiskelija }o--o{ Kurssi : "osallistuu"
    Opiskelija ||--o{ Ilmoittautuminen : "tekee"
    Kurssi ||--o{ Ilmoittautuminen : "koskee"

    %% Valinnainen suhde
    Asiakas o|--o{ Tilaus : "voi tehdä"
```


```mermaid
erDiagram
ASIAKAS }o--o{ TILAUS : "TEKEE"
```
```mermaid
Diagram 
    Henkilo ||--|| Passi : "omistaa"
```

```mermaid
    KESAMOKKI {
        int id PK
        string osoite
    }
```



```mermaid
| vasen | oikea | suomeksi    | englanniksi | Crow’s Foot (vasen) | Crow’s Foot (oikea) |
|------:|:------|-------------|-------------|--------------------|---------------------|
|   1  |   1    | Yksi yhteen | One to one |Kurssi pidetään Luokassa || | || |
|   1  |   N    | Opettaja opettaa Kurssia | A Teacher teaches Courses | || | o{ |
|   N  |   M    | Opiskelija osallistuu Kurssille | A Student enrolls in Courses | o{ | o{ |
| 0..1 |   N  | Asiakas voi tehdä Tilauksen | A Customer may place Orders | o| | o{ |
```


https://mermaid.js.org/syntax/entityRelationshipDiagram.html


=======
| Viiva | Merkitys  | Esimerkki                         |
|-------|-----------|-----------------------------------|
| `||--||` | 1–1    | Kurssi pidetään Luokassa          |
| `||--o{` | 1–N    | Opettaja opettaa Kurssia          |
| `}o--o{` | N–M    | Opiskelija osallistuu Kurssille   |
| `o|--o{` | 0..1–N | Asiakas voi tehdä Tilauksen       |
```

```mermaid
erDiagram
ASIAKAS o{--|| TOIMITUSOSOITE : "tallentaa"
```

```mermaid
erDiagram
    ASIAKAS ||--o{ TILAUS : "tekee"
    TILAUS  }o--o{ TUOTE : "sisaltaa"

```
```
| Koodi   | Kardinaliteetti | Selitys                    |
|---------|-----------------|----------------------------|
| `\|\|`  | 1               | yksi ja vain yksi          |
| `o\|`   | 0..1            | nolla tai yksi             |
| `}`     | 1..M            | yksi tai monta, ei nollaa  |
| `}o`    | 0..M            | nolla tai monta            |
```

```
| Koodi            | Suhde    | Selitys                                  |
|------------------|----------|-------------------------------------------|
| `\|\|--\|\|`     | 1–1      | yksi suhde yhteen (molemmat päät 1)       |
| `\|\|--}o`       | 1–0..M   | yksi suhteessa nollaan tai moneen         |
| `\|\|--}`        | 1–1..M   | yksi suhteessa vähintään yhteen          |
| `o\|--\|\|`      | 0..1–1   | valinnainen yksi suhteessa yhteen        |
| `o\|--}o`        | 0..1–0..M| valinnainen yksi suhteessa nollaan/moneen|
| `}o--}o`         | 0..M–0..M| moni–moni, nolla tai monta molemmissa     |
| `}--}`           | 1..M–1..M| moni–moni, ei nollaa kummassakaan         |

```