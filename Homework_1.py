from datetime import datetime

def get_days_from_today():
    
    user_input = input("Введіть дату у форматі YYYY-mm-dd: ")
    date = datetime.strptime(user_input, "%Y-%m-%d")
    return date

datetime_object = get_days_from_today()
today = datetime.now()
delta = datetime_object - today
print(f"Кількість днів до введеної дати: {delta.days}")