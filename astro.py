
def calcStarSign(month, date):
    print(f"DOB = {month} {date}")
    dict = {
        1: {range(1, 20): "capricorn", range(20, 32): "aquarius"},
        2: {range(1, 19): "aquarius", range(19, 30): "pisces"},
        3: {range(1, 20): "pisces", range(20, 32): "aries"},
        4: {range(1, 21): "aries", range(21, 31): "taurus"},
        5: {range(1, 20): "taurus", range(20, 32): "gemini"},
        6: {range(1, 21): "gemini", range(21, 31): "cancer"},
        7: {range(1, 23): "cancer", range(23, 32): "leo"},
        8: {range(1, 23): "leo", range(23, 32): "virgo"},
        9: {range(1, 23): "virgo", range(23, 31): "libra"},
        10: {range(1, 23): "libra", range(23, 32): "scorpio"},
        11: {range(1, 22): "scorpio", range(22, 31): "sagittarius"},
        12: {range(1, 22): "sagittarius", range(22, 32): "capricorn"}
    }
    for r in dict[month]:
        if date in r:
            print(dict[month][r])
            return dict[month][r]
    return "Invalid date"

if __name__ == "__main__":
    print(calcStarSign(1,20))