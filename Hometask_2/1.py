day = 20
month = 4
temperature = -3

print(f"Сегодня {day:>02}.{month:>02}. На уличе {temperature} градусов")
if temperature < 0:
    print("Холодно, лучше остаться дома")