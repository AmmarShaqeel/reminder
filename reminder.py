import subprocess
import time
from datetime import datetime

i = 0

while i < 1:
 current_hour = datetime.now().hour
 
 if current_hour > 6 and current_hour < 20:
     print('TK: I would stay on')
     time.sleep(10)

 elif current_hour == 20 or current_hour > 20:
    print('TK: I would turn off now')
    time.sleep(5)

 elif current_hour < 20:
    print('TK: I would turn off now')
    time.sleep(5)
            
