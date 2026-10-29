w = float(input("Wpisz kwotę roczną w złotych: "))

if w <= 30000:
    wyplata = w
    print("Twoja wypłata jest równa: ", wyplata)
if 120000 >= w > 30000:
    podatek = (0.12 * w)-3600
    print("Twoja wypłata jest równa: ", w - podatek)
if 1000000 >= w > 120000:
    podatek = 10800 + (w - 120000) * 0.32
    print("Twoja wypłata jest równa: ", w - podatek)
if w > 1000000:
    podatek = (10800 + (w - 120000) * 0.32) - 1000000 * 0.4
    print("Twoja wypłata jest równa: ", w - podatek)