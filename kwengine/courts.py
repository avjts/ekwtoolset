COURTS: set[str] = {
    'BB1B',  # BIELSKO-BIAŁA
    'BB1C',  # CIESZYN
    'BB1Z',  # ŻYWIEC
    'BI1B',  # BIAŁYSTOK
    'BI1P',  # BIELSK PODLASKI
    'BI1S',  # SOKÓŁKA
    'BI2P',  # HAJNÓWKA
    'BI3P',  # SIEMIATYCZE
    'BY1B',  # BYDGOSZCZ
    'BY1I',  # INOWROCŁAW
    'BY1M',  # MOGILNO
    'BY1N',  # NAKŁO NAD NOTECIĄ
    'BY1S',  # ŚWIECIE
    'BY1T',  # TUCHOLA
    'BY1U',  # SZUBIN
    'BY1Z',  # ŻNIN
    'BY2T',  # SĘPÓLNO KRAJEŃSKIE
    'CIKW',  # WARSZAWA
    'CZ1C',  # CZĘSTOCHOWA
    'CZ1L',  # LUBLINIEC
    'CZ1M',  # MYSZKÓW
    'CZ1Z',  # ZAWIERCIE
    'CZ2C',  # KŁOBUCK
    'EL1B',  # BRANIEWO
    'EL1D',  # DZIAŁDOWO
    'EL1E',  # ELBLĄG
    'EL1I',  # IŁAWA
    'EL1N',  # NOWE MIASTO LUBAWSKIE
    'EL1O',  # OSTRÓDA
    'EL2O',  # MORĄG
    'GD1A',  # STAROGARD GDAŃSKI
    'GD1E',  # KOŚCIERZYNA
    'GD1G',  # GDAŃSK
    'GD1I',  # KWIDZYN
    'GD1M',  # MALBORK
    'GD1R',  # KARTUZY
    'GD1S',  # SOPOT
    'GD1T',  # TCZEW
    'GD1W',  # WEJHEROWO
    'GD1Y',  # GDYNIA
    'GD2I',  # SZTUM
    'GD2M',  # NOWY DWÓR GDAŃSKI
    'GD2W',  # PUCK
    'GL1G',  # GLIWICE
    'GL1J',  # JASTRZĘBIE-ZDRÓJ
    'GL1R',  # RACIBÓRZ
    'GL1S',  # RUDA ŚLĄSKA
    'GL1T',  # TARNOWSKIE GÓRY
    'GL1W',  # WODZISŁAW ŚLĄSKI
    'GL1X',  # ŻORY
    'GL1Y',  # RYBNIK
    'GL1Z',  # ZABRZE
    'GW1G',  # GORZÓW WIELKOPOLSKI
    'GW1K',  # STRZELCE KRAJEŃSKIE
    'GW1M',  # MIĘDZYRZECZ
    'GW1S',  # SŁUBICE
    'GW1U',  # SULĘCIN
    'JG1B',  # BOLESŁAWIEC
    'JG1J',  # JELENIA GÓRA
    'JG1K',  # KAMIENNA GÓRA
    'JG1L',  # LUBAŃ
    'JG1S',  # LWÓWEK ŚLĄSKI
    'JG1Z',  # ZGORZELEC
    'KA1B',  # BĘDZIN
    'KA1C',  # CHORZÓW
    'KA1D',  # DĄBROWA GÓRNICZA
    'KA1I',  # SIEMIANOWICE ŚLĄSKIE
    'KA1J',  # JAWORZNO
    'KA1K',  # KATOWICE
    'KA1L',  # MYSŁOWICE
    'KA1M',  # MIKOŁÓW
    'KA1P',  # PSZCZYNA
    'KA1S',  # SOSNOWIEC
    'KA1T',  # TYCHY
    'KA1Y',  # BYTOM
    'KI1A',  # STASZÓW
    'KI1B',  # BUSKO ZDRÓJ
    'KI1H',  # STARACHOWICE
    'KI1I',  # KAZIMIERZA WIELKA
    'KI1J',  # JĘDRZEJÓW
    'KI1K',  # KOŃSKIE
    'KI1L',  # KIELCE
    'KI1O',  # OSTROWIEC ŚWIĘTOKRZYSKI
    'KI1P',  # PIŃCZÓW
    'KI1R',  # SKARŻYSKO-KAMIENNA
    'KI1S',  # SANDOMIERZ
    'KI1T',  # OPATÓW
    'KI1W',  # WŁOSZCZOWA
    'KN1K',  # KOŁO
    'KN1N',  # KONIN
    'KN1S',  # SŁUPCA
    'KN1T',  # TUREK
    'KO1B',  # BIAŁOGARD
    'KO1D',  # DRAWSKO POMORSKIE
    'KO1E',  # SŁAWNO
    'KO1I',  # SZCZECINEK
    'KO1K',  # KOSZALIN
    'KO1L',  # KOŁOBRZEG
    'KO1W',  # WAŁCZ
    'KO2B',  # ŚWIDWIN
    'KR1B',  # SUCHA BESKIDZKA
    'KR1C',  # CHRZANÓW
    'KR1E',  # OŚWIĘCIM
    'KR1H',  # PROSZOWICE
    'KR1I',  # WIELICZKA
    'KR1K',  # CZERNICHÓW
    'KR1M',  # MIECHÓW
    'KR1O',  # OLKUSZ
    'KR1P',  # KRAKÓW
    'KR1S',  # SŁOMNIKI
    'KR1W',  # WADOWICE
    'KR1Y',  # MYŚLENICE
    'KR2E',  # KĘTY
    'KR2I',  # NIEPOŁOMICE
    'KR2K',  # KRZESZOWICE
    'KR2P',  # SKAŁA
    'KR2Y',  # DOBCZYCE
    'KR3I',  # SKAWINA
    'KS1B',  # BRZOZÓW
    'KS1E',  # LESKO
    'KS1J',  # JASŁO
    'KS1K',  # KROSNO
    'KS1S',  # SANOK
    'KS2E',  # USTRZYKI DOLNE
    'KZ1A',  # KALISZ
    'KZ1E',  # KĘPNO
    'KZ1J',  # JAROCIN
    'KZ1O',  # OSTRZESZÓW
    'KZ1P',  # PLESZEW
    'KZ1R',  # KROTOSZYN
    'KZ1W',  # OSTRÓW WIELKOPOLSKI
    'LD1B',  # BRZEZINY
    'LD1G',  # ZGIERZ
    'LD1H',  # SKIERNIEWICE
    'LD1K',  # KUTNO
    'LD1M',  # ŁÓDŹ
    'LD1O',  # ŁOWICZ
    'LD1P',  # PABIANICE
    'LD1R',  # RAWA MAZOWIECKA
    'LD1Y',  # ŁĘCZYCA
    'LE1G',  # GŁOGÓW
    'LE1J',  # JAWOR
    'LE1L',  # LEGNICA
    'LE1U',  # LUBIN
    'LE1Z',  # ZŁOTORYJA
    'LM1G',  # GRAJEWO
    'LM1L',  # ŁOMŻA
    'LM1W',  # WYSOKIE MAZOWIECKIE
    'LM1Z',  # ZAMBRÓW
    'LU1A',  # LUBARTÓW
    'LU1B',  # BIAŁA PODLASKA
    'LU1C',  # CHEŁM
    'LU1I',  # LUBLIN
    'LU1K',  # KRAŚNIK
    'LU1O',  # OPOLE LUBELSKIE
    'LU1P',  # PUŁAWY
    'LU1R',  # RADZYŃ PODLASKI
    'LU1S',  # ŚWIDNIK
    'LU1U',  # ŁUKÓW
    'LU1W',  # WŁODAWA
    'LU1Y',  # RYKI
    'NS1G',  # GORLICE
    'NS1L',  # LIMANOWA
    'NS1M',  # MUSZYNA
    'NS1S',  # NOWY SĄCZ
    'NS1T',  # NOWY TARG
    'NS1Z',  # ZAKOPANE
    'NS2L',  # MSZANA DOLNA
    'OL1B',  # BISKUPIEC
    'OL1C',  # OLECKO
    'OL1E',  # EŁK
    'OL1G',  # GIŻYCKO
    'OL1K',  # KĘTRZYN
    'OL1L',  # LIDZBARK WARMIŃSKI
    'OL1M',  # MRĄGOWO
    'OL1N',  # NIDZICA
    'OL1O',  # OLSZTYN
    'OL1P',  # PISZ
    'OL1S',  # SZCZYTNO
    'OL1Y',  # BARTOSZYCE
    'OL2G',  # WĘGORZEWO
    'OP1B',  # BRZEG
    'OP1G',  # GŁUBCZYCE
    'OP1K',  # KĘDZIERZYN-KOŹLE
    'OP1L',  # OLESNO
    'OP1N',  # NYSA
    'OP1O',  # OPOLE
    'OP1P',  # PRUDNIK
    'OP1S',  # STRZELCE OPOLSKIE
    'OP1U',  # KLUCZBORK
    'OS1M',  # OSTRÓW MAZOWIECKA
    'OS1O',  # OSTROŁĘKA
    'OS1P',  # PRZASNYSZ
    'OS1U',  # PUŁTUSK
    'OS1W',  # WYSZKÓW
    'PL1C',  # CIECHANÓW
    'PL1E',  # SIERPC
    'PL1G',  # GOSTYNIN
    'PL1L',  # PŁOŃSK
    'PL1M',  # MŁAWA
    'PL1O',  # SOCHACZEW
    'PL1P',  # PŁOCK
    'PL1Z',  # ŻYRARDÓW
    'PL2M',  # ŻUROMIN
    'PO1A',  # SZAMOTUŁY
    'PO1B',  # WĄGROWIEC
    'PO1D',  # ŚRODA WLKP.
    'PO1E',  # WOLSZTYN
    'PO1F',  # WRZEŚNIA
    'PO1G',  # GNIEZNO
    'PO1H',  # CHODZIEŻ
    'PO1I',  # PIŁA
    'PO1K',  # KOŚCIAN
    'PO1L',  # LESZNO
    'PO1M',  # ŚREM
    'PO1N',  # NOWY TOMYŚL
    'PO1O',  # OBORNIKI
    'PO1P',  # POZNAŃ(V)
    'PO1R',  # RAWICZ
    'PO1S',  # GRODZISK WLKP.
    'PO1T',  # TRZCIANKA
    'PO1Y',  # GOSTYŃ
    'PO1Z',  # ZŁOTÓW
    'PO2A',  # MIĘDZYCHÓD
    'PO2H',  # WYRZYSK
    'PO2P',  # POZNAŃ(VI)
    'PO2T',  # CZARNKÓW
    'PR1J',  # JAROSŁAW
    'PR1L',  # LUBACZÓW
    'PR1P',  # PRZEMYŚL
    'PR1R',  # PRZEWORSK
    'PR2R',  # SIENIAWA
    'PT1B',  # BEŁCHATÓW
    'PT1O',  # OPOCZNO
    'PT1P',  # PIOTRKÓW TRYBUNALSKI
    'PT1R',  # RADOMSKO
    'PT1T',  # TOMASZÓW MAZOWIECKI
    'RA1G',  # GRÓJEC
    'RA1K',  # KOZIENICE
    'RA1L',  # LIPSKO
    'RA1P',  # PRZYSUCHA
    'RA1R',  # RADOM
    'RA1S',  # SZYDŁOWIEC
    'RA1Z',  # ZWOLEŃ
    'RA2G',  # BIAŁOBRZEGI
    'RA2Z',  # PIONKI
    'RZ1A',  # ŁAŃCUT
    'RZ1D',  # DĘBICA
    'RZ1E',  # LEŻAJSK
    'RZ1R',  # ROPCZYCE
    'RZ1S',  # STRZYŻÓW
    'RZ1Z',  # RZESZÓW
    'RZ2Z',  # TYCZYN
    'SI1G',  # GARWOLIN
    'SI1M',  # MIŃSK MAZOWIECKI
    'SI1P',  # SOKOŁÓW PODLASKI
    'SI1S',  # SIEDLCE
    'SI1W',  # WĘGRÓW
    'SI2S',  # ŁOSICE
    'SL1B',  # BYTÓW
    'SL1C',  # CHOJNICE
    'SL1L',  # LĘBORK
    'SL1M',  # MIASTKO
    'SL1S',  # SŁUPSK
    'SL1Z',  # CZŁUCHÓW
    'SO1C',  # CZELADŹ
    'SR1L',  # ŁASK
    'SR1S',  # SIERADZ
    'SR1W',  # WIELUŃ
    'SR1Z',  # ZDUŃSKA WOLA
    'SR2L',  # PODDĘBICE
    'SR2W',  # PAJĘCZNO
    'SU1A',  # AUGUSTÓW
    'SU1N',  # SEJNY
    'SU1S',  # SUWAŁKI
    'SW1D',  # DZIERŻONIÓW
    'SW1K',  # KŁODZKO
    'SW1S',  # ŚWIDNICA
    'SW1W',  # WAŁBRZYCH
    'SW1Z',  # ZĄBKOWICE ŚLĄSKIE
    'SW2K',  # NOWA RUDA
    'SZ1C',  # CHOSZCZNO
    'SZ1G',  # GRYFICE
    'SZ1K',  # KAMIEŃ POMORSKI
    'SZ1L',  # ŁOBEZ
    'SZ1M',  # MYŚLIBÓRZ
    'SZ1O',  # GOLENIÓW
    'SZ1S',  # SZCZECIN
    'SZ1T',  # STARGARD
    'SZ1W',  # ŚWINOUJŚCIE
    'SZ1Y',  # GRYFINO
    'SZ2S',  # POLICE
    'SZ2T',  # PYRZYCE
    'TB1K',  # KOLBUSZOWA
    'TB1M',  # MIELEC
    'TB1N',  # NISKO
    'TB1S',  # STALOWA WOLA
    'TB1T',  # TARNOBRZEG
    'TO1B',  # BRODNICA
    'TO1C',  # CHEŁMNO
    'TO1G',  # GOLUB-DOBRZYŃ
    'TO1T',  # TORUŃ
    'TO1U',  # GRUDZIĄDZ
    'TO1W',  # WĄBRZEŹNO
    'TR1B',  # BRZESKO
    'TR1D',  # DĄBROWA TARNOWSKA
    'TR1O',  # BOCHNIA
    'TR1T',  # TARNÓW
    'TR2T',  # TUCHÓW
    'WA1G',  # GRODZISK MAZOWIECKI
    'WA1I',  # PIASECZNO
    'WA1L',  # LEGIONOWO
    'WA1M',  # WARSZAWA(VI)
    'WA1N',  # NOWY DWÓR MAZOWIECKI
    'WA1O',  # OTWOCK
    'WA1P',  # PRUSZKÓW
    'WA1W',  # WOŁOMIN
    'WA2M',  # WARSZAWA(VII)
    'WA3M',  # WARSZAWA(IX)
    'WA4M',  # WARSZAWA(X)
    'WA5M',  # WARSZAWA(XIII)
    'WA6M',  # WARSZAWA(XV)
    'WL1A',  # ALEKSANDRÓW KUJAWSKI
    'WL1L',  # LIPNO
    'WL1R',  # RADZIEJÓW
    'WL1W',  # WŁOCŁAWEK
    'WL1Y',  # RYPIN
    'WR1E',  # OLEŚNICA
    'WR1K',  # WROCŁAW
    'WR1L',  # WOŁÓW
    'WR1M',  # MILICZ
    'WR1O',  # OŁAWA
    'WR1S',  # ŚRODA ŚLĄSKA
    'WR1T',  # STRZELIN
    'WR1W',  # TRZEBNICA
    'ZA1B',  # BIŁGORAJ
    'ZA1H',  # HRUBIESZÓW
    'ZA1J',  # JANÓW LUBELSKI
    'ZA1K',  # KRASNYSTAW
    'ZA1T',  # TOMASZÓW LUBELSKI
    'ZA1Z',  # ZAMOŚĆ
    'ZG1E',  # ZIELONA GÓRA
    'ZG1G',  # ŻAGAŃ
    'ZG1K',  # KROSNO ODRZAŃSKIE
    'ZG1N',  # NOWA SÓL
    'ZG1R',  # ŻARY
    'ZG1S',  # ŚWIEBODZIN
    'ZG1W',  # WSCHOWA
    'ZG2K',  # GUBIN
    'ZG2S',  # SULECHÓW
}
