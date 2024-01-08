## Calendar advent
Aplicatia va contine o lista de 24 de zile pana la Craciun. 
Pentru fiecare zi avem posibilitatea sa adaugam o imagine 
si un mesaj. 

### Descriere a aplicatiei. 
Aplicatia va contine o pagina principala unde se 
vor afisa toate cele 24 de zile. Pentru fiecare zi 
se va afisa imaginea corespunzatoare, precum si mesajul configurat.

Daca se apasa pe una dintre zile, se va naviga catre
un formular in care se poate configura / edita imaginea si mesajul
corespunzator zilei.

In plus, ziele se pot afla in starea deschis sau inchis. 
O zi inchisa ascunde detaliile pe pagina principala
O zi deschisa afiseaza detaliile pe pagina principala. 
Tot pe pagina principala, vom avea si un buton (pentru fiecare zi)
pentru a marca o zi ca deschisa.

_Optional_ Nu se pot deschide zile in avans. (Spre exemplu, daca suntem pe 10 decembrie, nu putem deschide ziele 11-24)

## Taskuri 
1. Adaugarea rutelor - Ionela 
   1. Ca un utilzator al aplicatiei, vreau sa pot sa accesez urmatoarele rute
      * / - root - pagina principala
      * /editeaza/<x> - pagina ce editeaza ziua x 
2. Conexiunea la baza de date - Emanuela
   1. Ca un developer, vreau sa pot accesa o baza de date.
   2. Accesarea se va face folosind SQLAlchemy
   3. Baza de date este de tip MySQL, disponibila la adresa localhost:3306, user: root, si fara parola, baza de date: advent 
3. Definirea tabelelor in baza de date: - Dana
   1. Ca un developer, vreau ca in baza de date sa am definit urmatorul tabel
      * id: int - PK
      * numar_zi: integer
      * imagine: string - numele imaginii folosite 
      * mesaj: string
      * deschis: boolean
4. Definirea modelelor ce fac referire la baza de date. - Alex
   1. Ca un developer, vreau sa am definite modele corespunzatoare tabelelor din baza de date. 
5. Template homepage - Aura
   1. Ca un utilizator, atunci cand accesez pagina principala, vreau sa vad 24 de chenare impreuna cu 24 de mesaje standard 
6. Template editate - Dan
   1. Ca un utilzator, atunci cand accesez pagina de editate a unei zile. Vreau sa vad un formular
   cu un camp ce poate fi folosit pentru incarcarea unei imagini si un camp
   ce capteaza text 

