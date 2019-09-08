'''
ac
'''

class Solution:

    @staticmethod
    def isR(year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
        return False

    def dayOfTheWeek(self, day, month, year):
        weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        standard = [1971,1,1,5]

        _sum = 0
        for yy in range(standard[0],year):
            if Solution.isR(yy):
                _sum += 366
            else:
                _sum += 365

        month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
        if Solution.isR(year):
            month_day[1] += 1
        for mm in range(standard[1],month):
            _sum += month_day[mm-1]

        _sum += day-standard[2]

        return weekday[(_sum+standard[3])%7]


