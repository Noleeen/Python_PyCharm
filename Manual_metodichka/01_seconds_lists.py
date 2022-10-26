# секунды в мин часы и дни

dur = 400153

if dur < 60:
    print(dur, 'second')
elif 60 <= dur < 3600:
    print(f'{dur // 60}minutes {dur % 60}second')
elif 3600 <= dur < 86400:
    print(f'{dur//3600} hours  {dur % 3600 // 60} minutes  {dur % 60} second')
elif 86400 <= dur:
    print(f'{dur//86400} days  {dur%86400//3600} hours  {dur % 3600 // 60} minutes  {dur % 60} second')

#-----------------------------------------------------------
