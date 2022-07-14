def pi(length, accuracy):

  """
  Calculates the value of pi using Nilakantha's series.
  """

  pi = 0
  top_num = 4 * length
  bot_num = 2
  positive = True

  for _ in range(1, accuracy):
    new_bot = bot_num*(bot_num+1)*(bot_num+2)
    num = top_num//new_bot
    if positive:
      pi += num
    else:
      pi -= num
    positive = not positive
    bot_num += 2

  print("3.", round(pi), sep="")

length = 10**100
accuracy = 10**7

pi(length, accuracy)
pi_hundred = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
print(pi_hundred)
print("21 digit accuracy with 10**100 length and 10**7 accuracy")