def cheese_and_crackers(cheese_count, boxes_crackers):
    print 'You have %d cheese!' % cheese_count
    print 'You have %d boxes of crackers!' % boxes_crackers
    print 'Man that\'s enough for a party!'
    print 'Get a blanket.\n'

print 'We can just give the function numers directly:'
cheese_and_crackers(20, 30)


print 'OR, we can use variables from our script:'
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_cheese)

print 'We can even do math inside too:'
cheese_and_crackers(10 + 20, 5 + 6)

print 'And we can combile the two, variables and math:'
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

def funbnanci(max):
   print 'Fabonnanci %r' % max
   print 'Len of %r is %d' % (max, len(max))

funbnanci('40')
