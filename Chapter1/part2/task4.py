our = int(input("Какой час был:"))
minute = our * 60
sek = minute * 60
our2 = int(input('Какой сейчас час:'))
minute2 = our2 * 60
sek2 = minute2 * 60
rour = our2 - our
rmin = minute2 - minute
rsek = sek2 - sek
print(f'Разница во времени {rour} часов или {rmin} минут или {rsek} секунд')