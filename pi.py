from decimal import getcontext, Decimal

def pi(length, reps):

  """
  Calculates the value of pi using Nilakantha's series.
  """
  getcontext().prec = length
  pi = 3
  top_num = 4
  bot_num = 2
  positive = True

  for _ in range(1, reps):
    new_bot = bot_num*(bot_num+1)*(bot_num+2)
    num = Decimal(top_num)/Decimal(new_bot)
    if positive:
      pi += num
    else:
      pi -= num
    positive = not positive
    bot_num += 2

  return pi

length = 10**2
reps = 10**8

pi_calculated = pi(length, reps)
print(pi_calculated)

pi_hundred = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
print(pi_hundred)
