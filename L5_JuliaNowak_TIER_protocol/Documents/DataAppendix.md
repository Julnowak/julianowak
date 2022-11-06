# Informacje do plików w folderze "Analysis Data"

## Final_data

Końcowe dane, zawierające informacje o temperaturze maksymalnej i temperaturze minimalnej dla poszczególnych dni miesięcy od roku 1955 do roku 1980 w Meksyku. Plik można otworzyć w Microsoft Excel, a także odczytać w środowisku obsługującym język Python.

Pierwsza kolumna zawiera przypisaną numerację każdego rzędu (przy dalszej obróbce w Pythonie należałoby ją usunąć).

Druga kolumna "id" zawiera id pomiaru - z pliku od odczytane zostały wszystkie identyczne id.

Trzecia kolumna "date" zawiera informacje o dacie wykonnia pomiaru w formacie RRRR-MM-DD.

Czwarta kolumna "tmax" zawiera informację o maksymalnej wartości temperatury w danym dniu. Jednostką jest Kelwin.

Piąta kolumna "tmin" zawiera informację o minimalnej wartości temperatury w danym dniu. Jednostką jest Kelwin.

Z ponad 1700 wyników wzięto pod uwagę 561 wyników, które nie zawierały braków i niejasności. Usunięto także miesiące, któe miały tylko jedną wartość temperatury - albo maksymalną albo minimalną.

Informacje o danych:
- dane o temperaturze maksymalnej
    średnia wartość: 264.9229686950404
    Odchylenie standardowe: 28.225120190353934
    Wartość minimalna: 110.0
    Wartość maksymalna: 370.0
    Kwantyl 25%: 250.0
    Mediana: 260.0
    Kwantyl 75%: 280.0

- dane o temperaturze minimalnej
    średnia wartość: 148.0602649783093
    Odchylenie standardowe: 22.011832226110034
    Wartość minimalna: 30.0
    Wartość maksymalna: 290.0
    Kwantyl 25%: 135.0
    Mediana 150.0
    Kwantyl 75%: 160.0



## Final_opady

Końcowe dane, zawierające informacje o wielkości opadów dla poszczególnych dni miesięcy od roku 1955 do roku 1980 w Meksyku. Plik można otworzyć w Microsoft Excel, a także odczytać w środowisku obsługującym język Python.

Pierwsza kolumna zawiera przypisaną numerację każdego rzędu (przy dalszej obróbce w Pythonie należałoby ją usunąć).

Druga kolumna "id" zawiera id pomiaru - z pliku od odczytane zostały wszystkie identyczne id.

Trzecia kolumna "date" zawiera informacje o dacie wykonnia pomiaru w formacie RRRR-MM-DD.

Czwarta kolumna "prcp" zawiera informację o wielkości opadów w milimetrach, które wystąpiły w danym dniu danego miesiąca i roku.


Z ponad 1700 wyników wzięto pod uwagę 273 wyników, które nie zawierały braków i niejasności.

Wszystkie zmienne pochodzą z oryginalnego pliku "weather.txt".

Informacje o danych:
- dane o opadach
    średnia wartość: 32.37886884880873
    Odchylenie standardowe: 87.33190461873974
    Wartość minimalna: 0.0
    Wartość maksymalna: 1290.0
    Kwantyl 25%: 0.0
    Mediana 0.0
    Kwantyl 75%: 11.0


## Informacje dodatkowe

Histogramy do danych zostały zaprezentowane w pliku "Data_appendix.ipynb" znajdującym się w folderze "Documents". W pliku tym można znaleźć przydatne informacje, pomagające w analizie danych.