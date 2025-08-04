import json
from datetime import datetime
user_emoji = input("What emoji represents your mood right now? \n To answer, open your emoji keyboard and select the emoji you want to use. \n Windows: press Windows + . (period) or Windows + ; (semicolon) to open the emoji keyboard. \n Mac: press Control + Command + Space to open the emoji keyboard. \n Linux: idk copy and paste it from Google. \n Your emoji/mood: ") 
date_today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
with open('history.json', 'r') as file:
    history = json.load(file)
history.append([user_emoji, date_today])
with open('history.json', 'w') as file:
    json.dump(history, file)


print(history)