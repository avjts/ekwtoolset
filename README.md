# eKW toolset

    narzędziownik poszukiwacza ksiąg

## Python

W zależności od systemu operacyjnego i sposobu zainstalowania Pythona
uruchomienie skryptu może wymagać różnych komend:

- `$ python3 script.py` na macOSie i Linuxie
- `$ python script.py` na Windowsie
- `$ py script.py` na Windowsie po zainstalowaniu Python launchera

## Generowanie numerów ksiąg `generate_kw.py`

```bat
$ py generate_kw.py -h        

usage: generate_kw.py [-h] [--last-digit [0-9]] [--hash [0-9]] court start [end]

positional arguments:
  court               Oznaczenie sądu, np. NS1Z
  start               od numeru
  end                 do numeru

options:
  --last-digit [0-9]  filtruj po ostatniej cyfrze numeru
  --hash [0-9]        filtruj po cyfrze kontrolnej
```

Gdy potrzebujesz wyliczyć cyfrę kontrolną jednego numeru księgi:

```bat
py generate_kw.py NS1Z <numer>
```

Gdy w wyszukiwarce poznałeś ostanią cyfrę numeru księgi i cyfrę kontrolną
i potrzebujesz listy ksiąg o takich identyfikatorach:

```bat
py generate_kw.py NS1Z 1 100000 --last-digit <np.5> --hash <np.6>
```