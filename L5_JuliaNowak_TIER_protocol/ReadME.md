# TIER protocol i tidy data - dane pogodowe

Projekt miał na celu przeprowadzenia oczyszczania danych, a także ich posortowanie i przedstawienie w postaci wykresów oraz danych statystycznych. Dane do analizy są danymi opisującymi dzienne dane pogodowe z Global Historical Climatology Network dla jednej stacji pogodowej (MX17004) w Meksyku od 1955 do 2011 roku.

## Struktura projektu
Struktura została utworzona w taki sposób, aby w łatwy i przyjazny użytkownikowi sposób umożliwić odtworzenie projekty. Strukturę projektu tworzą następujące foldery:

- **Analysis Data** - zawieraja gotowe dane, które były wykorzstane do utworzenia końcowych wykresów, a także do przeprowadzenia standardowych obliczeń statystycznych. W folderze znajdują się 2 pliki. W pliku "Final_data.xlsx" znajdują się informacje o temperaturze maksymalnej i minimalnej, a w pliku "Final_opady.xlsx" znajdują się informacje o wielkości opadów w Meksyku w latach 1955-1980.

- **Command Files** - zawieraja pomocnicze arkusze kalkulacyjne formatu ".xlsx", programy napisane w języku Python, umożliwiające przeprowadzenie czyszczenia danych oraz notebook, w którym przeprowadzone zostały obliczenia dotyczące danych statystycznych, a także zostały utworzone wykresy.

- **Documents** - zawiera ostateczny, przykładowy plik ".pdf", w którym przedstawiono jedynie najważniejsze dane, przedstawiające ogólne przeznaczenie analizowanych danych, a także plik "DataAppendix.md" Zawieraący informacje o analizowanych danych i plik "ReadME.md".

- **Original Data** - zawiera oryginalny plik z danymi "weather.txt", a także podfolder "Metadata", w którym znajduje się plik tekstowy "Metadata_Guide.txt" z opisem danych zawartych w "weather.txt"


## Wymagane oprogramowanie
Do uruchomienia programów niezbędne będzie środowisko obsługujące język Python 3.10 z dodatkowo zainstalowanymi bibliotekami: matplotlib, numpy, openpyxl, pandas, notebook. Oprócz tego niezbędny będzie dostęp do darmowego programu Microsoft Excel. Pomocne może się okazać użycie aplikacji "Github Desktop" oraz środowiska "Pycharm Professional" lub "Visual Studio Code".
