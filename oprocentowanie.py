KWOTA_KREDYTU = float(input("Podaj kwotę kredytu w PLN:"))
RATA_MIESIECZNA = float(input("podaj stałą miesięczna ratę w PLN:"))
OPROCENTOWANIE_PONAD_INF = float (input("podaj oprocentowanie kredytu ponad inflacje w procentach:"))
INFL_STYCZEN_1 = 1.59282448436825
INFL_LUTY_1 = -0.453509101198007
INFL_MARZEC_1 = 2.32467171712441
INFL_KWIECIEN_1 = 1.26125440724877
INFL_MAJ_1 = 1.78252628571251
INFL_CZERWIEC_1 = 2.32938454145522
INFL_LIPIEC_1 = 1.50222984223283
INFL_SIERPNIEN_1 = 1.78252628571251
INFL_WRZESIEN_1 = 2.32884899407637
INFL_PAZDZIERNIK_1 = 0.616921348207244
INFL_LISTOPAD_1 = 2.35229588637833
INFL_GRUDZIEN_1 = 0.337779545187098
INFL_STYCZEN_2 = 1.57703524727525
INFL_LUTY_2 = -0.292781442607648
INFL_MARZEC_2 = 2.48619659017508
INFL_KWIECIEN_2 = 0.267110317834564
INFL_MAJ_2 = 1.41795267229799
INFL_CZERWIEC_2 = 1.05424326726375
INFL_LIPIEC_2 = 1.4805201044812
INFL_SIERPNIEN_2 = 1.57703524727525
INFL_WRZESIEN_2 = -0.0774206903147018
INFL_PAZDZIERNIK_2 = 1.16573339872354
INFL_LISTOPAD_2 = -0.404186717638335
INFL_GRUDZIEN_2 = 1.49970852083123

POZOSTALO = (1+(INFL_STYCZEN_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (KWOTA_KREDYTU - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na styczeń I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_LUTY_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na luty I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_MARZEC_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na marzec I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_KWIECIEN_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na kwiecien I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_MAJ_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na maj I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_CZERWIEC_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na czerwiec I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_LIPIEC_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na lipiec I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_SIERPNIEN_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na sierpien I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_WRZESIEN_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na wrzesien I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_PAZDZIERNIK_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na pazdziernik I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_LISTOPAD_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na listopad I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_GRUDZIEN_1 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na grudzien I roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_STYCZEN_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na styczen II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_LUTY_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na luty II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_MARZEC_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na marzec II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_KWIECIEN_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na kwiecien II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_MAJ_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na maj Ii roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_CZERWIEC_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na czerwiec II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_LIPIEC_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na lipiec II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_SIERPNIEN_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na sierpien II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_WRZESIEN_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na wrzesien II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_PAZDZIERNIK_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na pazdziernik II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_LISTOPAD_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na listopad II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))

POZOSTALO = (1+(INFL_GRUDZIEN_2 + OPROCENTOWANIE_PONAD_INF)/1200) * (POZOSTALO - RATA_MIESIECZNA)
ROZNICA = KWOTA_KREDYTU - POZOSTALO
print("Twoja pozostała kwota kredytu na grudzien II roku to: {}PLN, to {}PLN mniej niż w poprzednim miesiącu.".format(POZOSTALO, ROZNICA))
