# Paikallisen kansion tekeminen Github- repositoryksi

1. Luo uusi GitHub-repositorio
    1.	Mene GitHubiin ja kirjaudu sisään.
    2.	Klikkaa oikeasta yläkulmasta New repository (Uusi repositorio).
    3.	Anna repositoriolle nimi ja valitse, onko se Public (julkinen) vai Private (yksityinen).
    4.	ÄLÄ vielä lisää README-, .gitignore- tai lisenssitiedostoa (voit lisätä ne myöhemmin).
    5.	Klikkaa Create repository.
2. Linkitä paikallinen kansio GitHub-repositorioon
    1.	Avaa komentorivi (cmd) tai Git Bash ja siirry haluamaasi kansioon: 
        * cd "C:\polku\kansioon"
    2.	Alusta Git-repositorio: 
        * git init
    3.	Linkitä paikallinen kansio GitHub-repositorioon (korvaa <URL> GitHubista saamallasi linkillä) 
        * git remote add origin <URL>
3. Lisää ja lähetä tiedostot GitHubiin
    1.	Lisää kaikki tiedostot versiohallintaan: 
        * git add .
    2.	Tee ensimmäinen commit: 
        * git commit -m "Ensimmäinen commit"
    3.	Lähetä tiedostot GitHubiin:
        * git branch -M main
        * git push -u origin main

