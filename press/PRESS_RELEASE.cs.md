# 220 znaků. Žádné úpravy. Šifra z doby studené války, kterou si můžete ověřit sami.

**Výzkum podporovaný AI rekonstruoval celý text HC615, archivního cvičení z kryptoanalýzy datovaného v katalogu přibližně rokem 1952.**

*Návrh informačního textu připravený 5. října 2026. Potvrzení externími odborníky a změna stavu v oficiálním katalogu zatím neproběhly.*

Osm řádků číslic, teček, čárek a neobvyklých značek lze nyní přečíst jako souvislý český text. Projekt HC615 nalezl jednu pevnou substituční tabulku, která znovu zašifruje **všech 220 pozorovaných znaků, všech 32 úseků a všech osm řádků**. Výsledek nevyžaduje opravu či vypuštění znaků, nulové znaky ani výjimky závislé na pozici. Text, klíč, dokumentace zdroje a ověřovací program jsou připraveny v [balíčku pro GitHub](../README.md).

HC Portal eviduje předlohu pod názvem **„Unsolved cryptogram in 11 210“**. Záznam ji řadí k materiálům kurzu kryptoanalýzy přibližně z roku 1952 v Archivu bezpečnostních složek, `ZSGS / box BF388a, 27-19/6-099`. Při kontrole projektu dne 5. října 2026 zůstával v katalogu stav „Not solved“. Jde o stav katalogového záznamu, nikoli o důkaz, že cvičení dosud nikdo soukromě nevyřešil. [Původní záznam](https://api.hcportal.eu/api/cryptograms/615).

Rozluštěný text uvádí, že Transporta vyslala **devět soudruhů na jednoroční brigádu** a že Ostrava potřebuje brigádníky se zkušenostmi z politické práce. Celé sdělení je jazykově souvislé. Přesný výstup algoritmu je bez diakritiky; doplnění diakritiky, velkých písmen a interpunkce je oddělenou redakční vrstvou. U slova `chrudimska` zůstávají dvě možné interpretace členění a diakritiky, obě se stejnou posloupností písmen. [Úplný text a klíč](../docs/SOLUTION.md).

Mechanickou kontrolu lze shrnout jednoduše: **22 pozorovaných tříd znaků, jedna tabulka, 220 shod.** Krátký program v Pythonu z otevřeného textu a klíče rekonstruuje identifikátory šifrových znaků a z přiložených českých statistických dat přepočítává uložená skóre. Nevyžaduje externí službu AI, nové trénování modelu ani nové hledání klíče. Čtenář může zároveň porovnat přepis s [původním snímkem](https://api.hcportal.eu/media/1762/14161684790141.jpg). Certifikát dokládá shodu s uzamčeným přepisem evidujícím každý výskyt; shoda tohoto přepisu se snímkem je samostatnou kontrolou zdroje. [Postup reprodukce](../docs/METHODS.md).

Řešení využívá klasické simulované žíhání a české znakové statistiky v pracovním postupu podporovaném AI. Před pokusem o skutečný kryptogram byl řešič ověřen na šesti srovnatelných syntetických kontrolách z různých dokumentů. Všech 16 restartů při předem stanoveném rozpočtu vedlo ke stejnému textu a stejnému klíči pro pozorované znaky. To podporuje reprodukovatelnost, nikoli tvrzení o matematické jednoznačnosti ve všech modelech. [Metody a záznam experimentu](../docs/METHODS.md).

Výsledkem je **úplná rekonstrukce pozorované zprávy**. Katalog popisuje výukové cvičení; projekt nemá podklad pro tvrzení, že jde o nově odhalený tajný špionážní dopis. Historické šifrové znaky pro nepřítomná písmena `f/q/w/x` zůstávají neznámé. Nezávislé interní kontroly provedli oddělení AI agenti a programy, nikoli externí odborní recenzenti. Projekt netvrdí světové prvenství, nový algoritmus ani schválení institucí. [Rozsah tvrzení](../docs/CLAIMS.md), [stav zveřejnění a posouzení](../docs/PUBLICATION_STATUS.md).

K ověření zdroje, úplného čtení a případného staršího řešení či učebního klíče jsou zváni koordinátor HC Portal a odborníci na češtinu a historickou kryptologii. [Ověřené veřejné kontakty](../docs/EXPERT_CONTACTS.md).

**Každý pozorovaný znak má své vysvětlení. Kontrolu může spustit každý čtenář.**

**Autor:** Zijian Zeng, PhD · [GitHub](https://github.com/ArtificialZeng/hc615-cold-war-cipher-decoded)
