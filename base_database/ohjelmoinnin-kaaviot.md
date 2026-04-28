# Ohjelmoinnin olennaiset kaaviot

Tässä Markdown-esimerkissä esitellään ohjelmoinnin kannalta tärkeimmät kaaviot yksinkertaisin esimerkein.

---

## 1. ERD (Entity-Relationship Diagram)
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    CUSTOMER }|..|{ DELIVERY_ADDRESS : uses
```
*Selitys:* `CUSTOMER` voi tehdä monta `ORDER`-tilausta, `ORDER` sisältää useita `LINE_ITEM`-rivikohtia, ja asiakas voi käyttää useita toimitusosoitteita.

---

## 2. UML Luokkakaavio
```mermaid
classDiagram
    class Vehicle {
        +String brand
        +int year
        +start()
    }
    class Car {
        +int doors
        +lockDoors()
    }
    Vehicle <|-- Car
```
*Selitys:* `Car` perii `Vehicle`-luokan ominaisuudet ja metodit.

---

## 3. Sekvenssikaavio
```mermaid
sequenceDiagram
    participant User
    participant ATM
    participant Bank

    User->>ATM: Insert card
    ATM->>Bank: Validate card
    Bank-->>ATM: Card valid
    ATM->>User: Enter PIN
```
*Selitys:* Näyttää käyttäjän ja pankkiautomaatin välisen viestinnän.

---

## 4. Aktiviteettikaavio
```mermaid
flowchart TD
    A[Start] --> B{Decision?}
    B -- Yes --> C[Do Action 1]
    B -- No --> D[Do Action 2]
    C --> E[End]
    D --> E[End]
```
*Selitys:* Kuvaa yksinkertaisen päätöksen ja toimintojen kulun.

---

## 5. Tilakaavio
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : start()
    Processing --> Idle : finish()
    Processing --> Error : errorOccurs()
    Error --> Idle : reset()
```
*Selitys:* Kuvaa olion mahdolliset tilat ja siirtymät.

---

## 6. Data Flow Diagram (DFD)
```mermaid
flowchart LR
    User -->|Input data| System
    System -->|Process data| Database
    Database -->|Return results| System
    System -->|Output data| User
```
*Selitys:* Näyttää datan virtauksen käyttäjän, järjestelmän ja tietokannan välillä.

---

### Yhteenveto
- ERD: tietokannat
- Luokkakaavio: olio-ohjelmointi
- Sekvenssikaavio: prosessien vuorovaikutus
- Aktiviteettikaavio: algoritmin logiikka
- Tilakaavio: olion tilat
- DFD: datan kulku
