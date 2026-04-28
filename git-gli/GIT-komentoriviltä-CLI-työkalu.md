# GITHUB - CLI

GitHub CLI (gh) on komentorivityökalu, jolla voi käyttää GitHubin ominaisuuksia suoraan terminaalista ilman, että tarvitsee avata selainta.

👉 Käyttö jakaantuu kolmeen pääalueeseen:
1. Repositorion hallinta
2. Issues ja Pull Requestit
3. Käyttäjä- ja organisaatiotoiminnot

🔹 Perusasiat (repo ja koodi)
* gh repo clone <owner>/<repo> → kloonaa repositorion (kuten git clone).
* gh repo create → luo uuden repositorion GitHubiin.
* gh repo fork → forkkkaa repositorion omalle tilille.
* gh repo view → näyttää tiedot repositoriosta (README, linkit, jne.).

🔹 Issues
* gh issue list → listaa kaikki avoimet issue-tiketit.
* gh issue view <numero> → näyttää tietyn issuen.
* gh issue create → luo uuden issuen.
* gh issue close <numero> → sulkee issuen.

🔹 Pull requestit
* gh pr create → avaa uuden PR:n (esim. branchistasi mainiin).
* gh pr list → listaa kaikki avoimet PR:t.
* gh pr checkout <numero> → vaihtaa suoraan PR:n haaraan.
* gh pr merge <numero> → hyväksyy ja mergaa PR:n (voi valita squash, rebase, merge).

🔹 Käyttäjä ja organisaatiot
* gh auth login → kirjautuminen GitHubiin.
* gh auth status → tarkista oletko kirjautuneena.
* gh gist create → luo Gistin (pieni koodinpätkä tms.).
* gh api → suorittaa suoraan GitHubin REST API -kutsuja.

🔹 Edistyneemmät
* Actions:
  * gh workflow list → listaa GitHub Actions -työnkulut.
  * gh run watch <run-id> → seuraa käynnissä olevaa CI/CD-ajoa.
* Release-hallinta:
  * gh release create <tag> → luo julkaisun.
  * gh release upload <tag> <tiedosto> → lisää tiedosto julkaisulle.
  * gh release list → listaa julkaisut.

* Muuta:
  * gh --version: näyttää versionumeron. Tällä voi esim. varmistaa, onko polussa

## Käytännön hyöty
* Ei tarvitse klikata GitHubissa — kaikki onnistuu terminaalista.
* Nopeuttaa työnkulkua (esim. git push → heti perään gh pr create).
* Auttaa automatisoinnissa (skripteissä voi käyttää gh-komentoja).


Tässä selkeä taulukko GitHub CLI:n tärkeimmistä komennoista:

| Osa-alue | Komento | Selitys |
|:---------| :------ | :------ |
|Repositoriot		| gh repo clone <owner>/<repo>	| Kloonaa repositorion
|	          		| gh repo create				| Luo uuden repositorion GitHubiin
|					| gh repo fork					| Forkkaa repositorion omalle tilille
|					| gh repo view					| Näyttää repositorion tiedot
|Issues				| gh issue list					| Listaa avoimet issuet
|					| gh issue view <numero>		| Näyttää yksittäisen issuen
|					| gh issue create 				| Luo uuden issuen
|					| gh issue close <numero> 		| Sulkee issuen
|Pull Requestit		| gh pr create 					| Luo uuden PR:n
|					| gh pr list 					| Listaa avoimet PR:t
|					| gh pr checkout <numero> 		| Vaihtaa PR:n haaraan
|					| gh pr merge <numero>			| Mergaa PR:n (merge/squash/rebase)
|Release & Actions	| gh release create <tag>		| Luo uuden julkaisun
|					| gh release upload <tag> <tiedosto> | Lisää tiedosto julkaisuun
|					| gh release lis 				| Listaa julkaisut
|					| gh workflow list	 			| Listaa Actions-työnkulut
|					| gh run watch <id>	 			| Seuraa CI/CD-ajon etenemistä
|Muut				| gh auth login	 				| Kirjaudu GitHubiin
|					| gh auth status	 			| Tarkista kirjautumistila
|					| gh gist create	 			| Luo Gist-koodinpätkän
|					| gh api	 					| Suorita suora GitHub API -kutsu

---




---
---
# GitHub CLI Cheat Sheet

GitHub CLI (`gh`) on komentorivityökalu, jolla voit hallita GitHubin toimintoja ilman selainta.

---

## 🔹 Repositoriot
- `gh repo clone <owner>/<repo>` → Kloonaa repositorion
- `gh repo create` → Luo uuden repositorion GitHubiin
- `gh repo fork` → Forkkaa repositorion omalle tilille
- `gh repo view` → Näyttää repositorion tiedot

---

## 🔹 Issues
- `gh issue list` → Listaa avoimet issuet
- `gh issue view <numero>` → Näyttää yksittäisen issuen
- `gh issue create` → Luo uuden issuen
- `gh issue close <numero>` → Sulkee issuen

---

## 🔹 Pull Requestit
- `gh pr create` → Luo uuden PR:n
- `gh pr list` → Listaa avoimet PR:t
- `gh pr checkout <numero>` → Vaihtaa PR:n haaraan
- `gh pr merge <numero>` → Mergaa PR:n (merge / squash / rebase)

---

## 🔹 Release & Actions
- `gh release create <tag>` → Luo uuden julkaisun
- `gh release upload <tag> <tiedosto>` → Lisää tiedosto julkaisuun
- `gh release list` → Listaa julkaisut
- `gh workflow list` → Listaa Actions-työnkulut
- `gh run watch <id>` → Seuraa CI/CD-ajon etenemistä

---

## 🔹 Käyttäjä & muut
- `gh auth login` → Kirjaudu GitHubiin
- `gh auth status` → Tarkista kirjautumistila
- `gh gist create` → Luo Gist-koodinpätkän
- `gh api` → Suorita suora GitHub API -kutsu

---

## 🔹 Vinkkejä
- Yhdistä Gitin kanssa:  
  ```bash
  git push
  gh pr create
