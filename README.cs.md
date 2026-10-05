# HC615

## Šifra z období studené války. 220 znaků. Jedno reprodukovatelné čtení.

![HC615: 220 znaků, 22 tříd grafémů, jedna pevná substituce a úplný český text](assets/hero.svg)

[English](README.md) · [简体中文](README.zh-CN.md) · **Čeština** · [日本語](README.ja.md)

**Autor:** Zijian Zeng, PhD · **Repozitář:** [hc615-cold-war-cipher-decoded](https://github.com/ArtificialZeng/hc615-cold-war-cipher-decoded) · **Verze:** v1.0.1

Archivní kryptogram, který veřejný katalog uvádí jako **„Not solved“**, nyní má úplnou, ověřitelnou českou rekonstrukci: **jedna pevná substituce vysvětluje všech 220 pozorovaných znaků bez oprav, nulových znaků a výjimek podle pozice.** Tento repozitář umožňuje výsledek samostatně zkontrolovat.

**220 znaků · 22 tříd grafémů · 32 původních úseků · 8 řádků · 0 neshod**

Předlohou je **cvičení z kurzu kryptoanalýzy**, podle katalogu HC Portal přibližně z roku **1952**, uložené v *Archivu bezpečnostních složek*. Text se týká vysílání pracovníků na Ostravsko: Transporta vyslala devět soudruhů na jednoroční brigádu. Každé písmeno získaného textu odpovídá témuž vratnému klíči.

**Stav dokumentace k 5. 10. 2026:** úplné čtení pozorované zprávy a místní ověření prošly kontrolami. Veřejný katalog při posledním přístupu stále uváděl „Not solved“. Potvrzení externím odborníkem a porovnání s původním řešením kurzu dosud chybí. Celosvětové prvenství se netvrdí. [Přesný rozsah závěrů](docs/CLAIMS.md).

## Ověření během několika sekund

V kořenovém adresáři repozitáře spusťte s Pythonem 3.9 nebo novějším:

```sh
python3 scripts/verify_solution.py
```

Tato kontrola používá pouze standardní knihovnu Pythonu a funguje bez sítě. Porovnává otevřený text, klíč s 22 položkami a uložený přepis grafémů, kontroluje uložené hashe a výstupy hledání a ověřuje **220/220 znaků, 32/32 úseků a 8/8 řádků**. Přiložená česká statistická data používá k přepočtu uložených skóre. Nevyžaduje externí službu AI, nové trénování modelu ani nové hledání klíče.

Původní sken stáhnete a jeho zaznamenaný SHA-256 vyžádáte takto:

```sh
python3 scripts/fetch_sources.py --archive-image
python3 scripts/verify_solution.py --require-source-image
```

Sken se uloží do cache ignorované Gitem. Shodný hash potvrzuje totožnost souboru; správnost rozlišení grafémů v přepisu je stále třeba ověřit pohledem na předlohu. Práva k dalšímu šíření archivního snímku nebyla potvrzena, proto se obrazová data stahují od původního poskytovatele a nejsou součástí balíčku.

## Úplné čtení

Následuje **nezměněný výstup řešiče**, rozdělený do osmi řádků podle předlohy. Diakritika, velká písmena a interpunkce nebyly získány jako původní typografie.

```text
vysilaji na ostravsko nejlepsi
pracovniky chrudimska transporta
vyslala devet soudruhu na jednorocni
brigadu jsou mezi nimi clenove
celozavodniho vyboru organisace
sami se prihlasili ostrava potrebuje
brigadniky kteri maji zkusenosti z
politicke prace
```

Jedna možná redakční úprava pro čtenáře:

> Vysílají na Ostravsko nejlepší pracovníky. Chrudimská Transporta vyslala devět soudruhů na jednoroční brigádu. Jsou mezi nimi členové celozávodního výboru organisace. Sami se přihlásili. Ostrava potřebuje brigádníky, kteří mají zkušenosti z politické práce.

ASCII tvar `chrudimska` připouští i druhé členění: **„Vysílají na Ostravsko nejlepší pracovníky Chrudimska. Transporta vyslala…“** Samotná šifrovaná písmena neurčují původní diakritiku ani hranici věty. Historický pravopis **`organisace`** zůstává zachován.

Viz [přesný otevřený text](data/solution/PLAINTEXT_ASCII.txt), [klíč pro pozorované grafémy](data/solution/OBSERVED_GLYPH_KEY.json) a [původ dat](docs/PROVENANCE.md).

## Jak vznikl výsledek

1. **Nejprve zajistit předlohu.** Přepis vznikl před jazykovým hledáním; podobné grafémy zůstaly samostatnými třídami a každý výskyt má souřadnice na snímku. Červené předěly byly výslovně použity jako hypotéza hranic slov.
2. **Kalibrovat řešič.** Šest srovnatelných syntetických českých substitučních úloh se skrytými odpověďmi dosáhlo průměrné úspěšnosti obnovy písmen **99,6708 %**. Jde o výkon programu na těchto kontrolách, nikoli o pravděpodobnost správnosti archivního řešení.
3. **Provést jeden předem zaregistrovaný útok.** Klasický řešič bijektivní substituce použil pevný český čtyřgramový model, seed **615499** a **16 × 32768** pokusů o změnu. Všech 16 uložených restartů dalo stejný celý text i stejné mapování 22 pozorovaných tříd.
4. **Pokusit se řešení vyvrátit.** Oddělené kontroly provedené AI agenty a programy prověřily předlohu, souvislost celého českého textu, vstupní data, všechna uložená skóre a zpětné zašifrování 220 znaků. Nejde o potvrzení externími akademickými odborníky.

Otevřený text je skutečný výstup řešiče, nikoli text vytvořený jazykovým modelem a vydávaný za dešifrování. Mechanismus je klasická monoalfabetická substituce; přínosem je transparentní úplná rekonstrukce a reprodukovatelný soubor důkazů. [Metody, konfigurace, kontroly a omezení](docs/METHODS.md).

Úplné hledání lze znovu spustit s překladačem C++17:

```sh
python3 scripts/reproduce.py --controls
python3 scripts/reproduce.py --target
python3 -m unittest discover -s tests -v
```

Seedy a rozsah hledání jsou zachovány. Rozdíly mezi překladači a standardními knihovnami C++ mohou změnit průběh náhodného hledání; bitově shodný výstup optimalizátoru na různých platformách se neslibuje. Ověření pevného klíče na tomto hledání nezávisí.

## Předloha a externí posouzení

- [Záznam HC Portal 615](https://api.hcportal.eu/api/cryptograms/615), nazvaný **„Unsolved cryptogram in 11 210“**.
- [Původní sken](https://api.hcportal.eu/media/1762/14161684790141.jpg).
- Archivní označení podle katalogu: **Archiv bezpečnostních složek · ZSGS · box BF388a · 27-19/6-099**.
- [Koordinátoři HC Portal a relevantní odborníci s veřejnými kontakty a zdroji](docs/EXPERT_CONTACTS.md).

Celá pozorovaná zpráva je vysvětlena. Historické šifrové znaky pro nepoužitá písmena **f, q, w, x** zůstávají **UNKNOWN**. Původní diakritika, interpunkce, zdroj novinového textu, odesílatel, adresát ani původní klíč kurzu nebyly nezávisle určeny. Shoda 16 restartů nedokazuje matematickou jednoznačnost ani světové prvenství.

Pro recenzenta jsou rozhodující dvě otázky: **vysvětluje tento jediný pevný klíč celou předlohu a dává výsledný český text jako celek smysl?** Repozitář zachovává podklady pro prověření i zpochybnění obou částí.

## Licence a citování

Kód, vlastní průvodní texty projektu a jazyková data třetích stran mají rozdílné licence; viz [původ dat a uvedení autorů](docs/PROVENANCE.md). Přiložený český model a volitelný původní korpus zachovávají podmínky **CC BY-NC-SA 4.0**. Archivní sken a stahované původní korpusy nejsou součástí verzovaných souborů.

Pro citaci použijte [CITATION.cff](CITATION.cff). Veřejné popisy by měly odpovídat ověřeným formulacím v [CLAIMS.md](docs/CLAIMS.md) a skutečnému stavu zveřejnění v [PUBLICATION_STATUS.md](docs/PUBLICATION_STATUS.md).

**Přečtěte text. Zašifrujte jej zpět. Ověřte každý znak.**

## Ilustrované tiskové materiály

[Čínský popularizační článek ve Wordu](press/HC615_冷战档案密码_科技报道图文稿.docx) obsahuje pět původních ilustrací a celý text. [Tiskové návrhy ve čtyřech jazycích](press/README.md) čekají na kontrolu; externí odborné potvrzení dosud chybí.
