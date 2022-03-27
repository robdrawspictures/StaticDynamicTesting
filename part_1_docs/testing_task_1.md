### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # should be ==
      return True
    else # No colon
      return False
   

  dif highest_card(self, card1 card2): # def not dif; comma missing between card1 and card2
  if card1.value > card2.value: # not indented
    return card # card1
  else:
    return card2
  


def cards_total(self, cards): # Function not indented inside class
  total # undeclared variable; should be = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total # return should be outside the loop; total variable needs to be converted to a string to be concatanated.
  
```

<!-- Not sure if this is an intentional error or a weird bug,
but I couldn't get any tests to pass without removing self from every function; otherwise I got a 'missing 1 argument' error.

The only conclusion I could draw is it's something to do with
the class having no def __init__ so self isn't needed. -->