# секунды в мин часы и дни

# dur = 400153
#
# if dur < 60:
#     print(dur, 'second')
# elif 60 <= dur < 3600:
#     print(f'{dur // 60}minutes {dur % 60}second')
# elif 3600 <= dur < 86400:
#     print(f'{dur//3600} hours  {dur % 3600 // 60} minutes  {dur % 60} second')
# elif 86400 <= dur:
#     print(f'{dur//86400} days  {dur%86400//3600} hours  {dur % 3600 // 60} minutes  {dur % 60} second')

#-----------------------------------------------------------
kub = []
new_l = []
for idx in range(1,1001,2):
    kub.append(idx ** 3)
print(kub)

for idx in range(len(kub)):
    sum_digits = 0
    temp = kub[idx]
    while temp // 10 != 0:
        sum_digits += temp % 10
        temp = temp // 10
    else:
        sum_digits += temp % 10
    if sum_digits % 7 == 0:
        new_l.append(kub[idx])
print(new_l)

sum = 0
for item in new_l:
    sum += item
print(sum)