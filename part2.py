import re

line = 'sdkf niod; sdf , sdfn,asdk,    foo'
f = re.split(r'(;|,|\s)\s*', line)

line.startswith('sdk')  # True
line.endswith('oo')
line.startswith(('sdk', 'abc'))  # True
line.split()
line.lstrip('s')
line.rsplit('o')
line.replace('s', '--')

#  大小写转换
line.upper()
line.lower()

# change map
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
line.translate(remap)

line.ljust(20, '=')
line.rjust(20)
line.center(20)

l = ['a', 'b', 'c']
','.join(l)
print(l[0], l[1], l[2], sep=':')

s = '{name}: {value}'
s.format(name=1, value=1)
name = 'a'
value = 2
s.format_map(vars())

s = '{:>10}, {:<10}, {:^10}'
s.format('a', 'b', 'c')


