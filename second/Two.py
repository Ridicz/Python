L = L.sort()
# funkcja sort() nic nie zwraca, więc przypisanie jej do zmiennej pozbawione jest sensu

x, y = 1, 2, 3
# przypisanie krotki, liczba zmiennych po lewej stronie musi być równa wartościom po prawej

X = 1, 2, 3 ; X[1] = 4
# struktura tuple po przypisaniu jest niezmienialna, nie można jej modyfikować

X = [1, 2, 3]
X[3] = 4
# numeracja tablicy od zera, próba przypisania elementu poza zakresem

X = "abc"
X.append("d")
# X po przypisaniu "abc" jest typu str, który nie posiada funkcji append

map(pow, range(8))
# funkcja map nie przyjmuje jako argumentów funkcji wymagających więcej niż jednego argumentu
