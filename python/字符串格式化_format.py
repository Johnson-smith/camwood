print('i am {},my age is {}'.format('comyn', 18))
print('i am {1},my age is {0}'.format('comyn', 18))
print('i am {name},my age is {age}'.format(name='comyn', age=18))

print('i am %s' % ('hjw', ))
print('i am %(name)s' % {'name': 'hjw' })
print('i am %(name)s, my name is %(name)s' % {'name': 'hjw'})
print('i am %s, my name is %s' % ('hjw', 'hjw'))
print('i am %s' % 'hjw')
print('%d' % 18)
print('%i' % 18)
print('%u' % 18)
print('%a' % '马哥教育')
print('%c' %  'c')



print('i am {name},my age is {name}'.format(name='comyn', ))
print('i am {0}, my name is {0}'.format('comyn'))
print('{0} {name} {1}'.format('my', 'is hjw', name='abc'))
print('{1} {0} {name}'.format('phone_number', 'my', name='18651671668' ))
print('{} {} {name}'.format('phone', 'my', name='18651671668' ))
print('{}, {name}, {}'.format(1, 2, name='abc'))
#print('{}, {1}, {name}'.format(1, 2, name='abc'))
print("i'm {0}".format('hjw'))
print('i\'m {0}'.format('hjw'))
s='马哥教育'
print(type(s))
print(s)
b=s.encode()
print(type(b))
print(b.decode())

