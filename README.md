# Python-projekt-1---Textový analyzátor

Tento projekt byl vytvořen na základě zadaného úkolu a slouží k procvičení základních dovedností v jazyce Python. Zaměřuje se především na práci se vstupy od uživatele, podmínkami, seznamy, slovníky a základní textovou analýzu.

Program analyzuje předem připravené texty a poskytuje o nich různé informace. Po spuštění vyzve uživatele, aby zadal své uživatelské jméno a heslo. Zadané údaje porovná s předem registrovanými uživateli. Pokud se přihlášení podaří, program uživatele přivítá a nabídne mu možnost analyzovat texty. V opačném případě oznámí, že přístup není povolen, a ukončí se.

Po přihlášení si uživatel vybírá ze tří připravených textů, které byly v zadání. Pokud zadá neplatný vstup – například jiné číslo, než je povolené, nebo zadá místo čísla text – program jej upozorní a bez dalších kroků se ukončí.

Jakmile uživatel zvolí platný text, program ho zpracuje a sdělí mu několik základních údajů o jeho obsahu. Dozví se například:

• kolik slov text obsahuje,

• kolik z nich začíná velkým písmenem,

• kolik je napsaných jen velkými písmeny,

• kolik je naopak jen malými písmeny,

• kolik celých čísel se v textu nachází (nejde o jednotlivé cifry),

• a jaký je celkový součet těchto čísel.

Registrovaní uživatelé, kterým je přístup povolen, jsou:

• bob / 123

• ann / pass123

• mike / password123

• liz / pass123

Pokud se někdo pokusí přihlásit s neexistujícím jménem, jako je „marek“, a zadá heslo „123“, program oznámí, že uživatel není registrovaný, a ihned se ukončí.
