from datetime import time
from time import strftime



#[('10:00 AM', '10:00 AM),('12:00 AM', '12:00 AM)....('11:30','11:30')]

# for h in range(0, 24):
#     for m in (0, 30):
#         print(time(h, m).strftime('%I:%M %p'))# I format code of hour and M for minut %p is am,pm
        
        
t = [(time(h, m).strftime('%I:%M %p'),time(h, m).strftime('%I:%M %p'))for h in range(0, 24)for m in (0, 30)] 
print(t)