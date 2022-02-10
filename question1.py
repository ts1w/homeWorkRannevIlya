duration = int(input("Введите количество секунд, которое хотите преобразовать: "))
days = duration // 86400
hour = (duration - 86400) // 3600
minute = (duration - hour * 3600 - 86400) // 60
second = duration - (hour * 3600 + minute * 60) - 86400

if duration < 60:
    print(second, " сек")
elif 59 < duration < 3600:
    print(minute, " мин ", second, " сек")
elif 3600 < duration < 86400:
    print(hour, " час ", minute, " мин ", second, " сек")
elif duration > 86400:
    print(days, " дн ", hour, " час ", minute, " мин ", second, " сек")