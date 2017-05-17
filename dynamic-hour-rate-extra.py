hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate")
r = float(rate)

if hrs <= 40 :
    print hrs * rate

if hrs > 40 :
    hrsDiff = h - 40.00
    basicValue = 40.00 * r
    extraValue = hrsDiff * (1.5 * r)
    print basicValue + extraValue
