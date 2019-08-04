import os
import datetime

# GitHub will have darker colors in the contribution area for more commits
# 1 - 4 commits - Lighest
# 5 - 6 commits - Light
# 7 - 9 commmits - Dark
# 10+ commits - Darkest

year = 2018
month = 9
day = 2

startDate = datetime.date(year, month, day)

letterH = [0, 1, 2, 3, 4, 5, 6, 10, 17, 21, 22, 23, 24, 25, 26, 27]
letterE = [0, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 17, 20, 21, 24, 27]
letterL = [0, 1, 2, 3, 4, 5, 6, 13, 20, 27]
letterO = [0, 1, 2, 3, 4, 5, 6, 7, 13, 14, 20, 21, 22, 23, 24, 25, 26, 27]
wordHello = [letterH, letterE, letterL, letterL, letterO]


def commitOnDate(date, numCommits):
    for i in range(numCommits):
        os.system('echo "." >> dots')
        os.system('git add dots')
        os.system('git commit --date {} -m "."'.format(date.isoformat()))


letterOffset = 0
for letter in wordHello:
    for offset in letter:
        commitOnDate(
            startDate + datetime.timedelta(days=(letterOffset + offset)), 1)
    letterOffset += 35
