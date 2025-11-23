# datetime moduli
# Bugungi sana, vaqt, vaqt farqlari.
import datetime
now = datetime.datetime.now()
print(now)

# Faqat sana:
today = datetime.date.today()
print(today)

# Formatlash:
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Sana qo‘shish:
from datetime import timedelta
yarim_oy = today + timedelta(days=15)
print(yarim_oy)
