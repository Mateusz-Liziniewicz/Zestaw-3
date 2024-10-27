s1 = [1, 3, 4, 6, 7, 7, 8, 9]
s2 = [0, 1, 2, 4, 5, 6, 8, 8, 10]
wspolne = list(set(s1) & set(s2))
wszystkie = list(set(s1) | set(s2))
print(f"Wspólne elementy: {sorted(wspolne)}")
print (f"Wszystkie elementy: {wszystkie}")
