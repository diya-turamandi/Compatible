
def calcStarSign(month, date):
    print(f"DOB = {month} {date}")
    dict = {
        "january": {range(1, 20): "capricorn", range(20, 32): "aquarius"},
        "february": {range(1, 19): "aquarius", range(19, 30): "pisces"},
        "march": {range(1, 20): "pisces", range(20, 32): "aries"},
        "april": {range(1, 21): "aries", range(21, 31): "taurus"},
        "may": {range(1, 20): "taurus", range(20, 32): "gemini"},
        "june": {range(1, 21): "gemini", range(21, 31): "cancer"},
        "july": {range(1, 23): "cancer", range(23, 32): "leo"},
        "august": {range(1, 23): "leo", range(23, 32): "virgo"},
        "september": {range(1, 23): "virgo", range(23, 31): "libra"},
        "october": {range(1, 23): "libra", range(23, 32): "scorpio"},
        "november": {range(1, 22): "scorpio", range(22, 31): "sagittarius"},
        "december": {range(1, 22): "sagittarius", range(22, 32): "capricorn"}
    }
    for r in dict[month]:
        if date in r:
            return dict[month][r]
    return "Invalid date"

if __name__ == "__main__":
    print(calcStarSign("january",20))