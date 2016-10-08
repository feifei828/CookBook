import math
import random
from decimal import Decimal
from fractions import Fraction
from datetime import timedelta, datetime

round(1.234, 2)  # 1.23
round(1.27, 1)  # 1.3

# 当某个值等于两个整数间的一半时
# 取整操作会取到离该值最近的偶数上
round(1.5, 0)  # 2
round(2.5, 0)  # 2

round(2324, -1)  # 2320

# 格式化
format(1.2357, '0.3f')  # 1.235

'the value is {:0.3f}'.format(12.2352)

a = 2.1
b = 4.2
c = a + b  # 6.300000000000001

a = Decimal('2.1')
b = Decimal('4.2')
c = a + b  # 6.3

x = 1234.1245
format(x, '0.2f')  # 1234.12
format(x, '=>10.1f')  # ====1234.1
format(x, '=<10.1f')  # 1234.1====
format(x, '=^10.1f')  # ==1234.1==
format(x, ',')  # 1,234.1245
format(x, '0,.1f')  # 1,234.1

x = 1234
bin(x)  # 二进制
oct(x)  # 八进制
hex(x)  # 十进制

a = complex(2, 4)
b = 3 - 5j
a.real  # 2.0
a.imag  # 4.0
a.conjugate()  # 2-4j 共轭

a = float('inf')  # 无穷大
b = float('-inf')  # 负无穷大
c = float('nan')  # not a number
math.isinf(a)  # true
math.isnan(c)  # true

a = Fraction(5, 4)  # 5/4
a.numerator  # 5
a.denominator  # 4

b = 1.25
Fraction(*b.as_integer_ratio())  # 5/4

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
x + y  # [1, 2, 3, 4, 5, 6, 7, 8]
x * 2  # [1, 2, 3, 4, 1, 2, 3, 4]

random.choice(x)  # 在x中随机选择一个数
random.sample(x, 2)  # [1, 2]
random.shuffle(x)  # 打乱x

random.randint(0, 10)  # 产生随机整数
random.random()  # 0~1之间均匀分布的浮点数

a = timedelta(days=2, hours=6)
b = timedelta(days=4.5)
c = a + b
c.seconds  # 21600

a = datetime(2012, 9, 23)
b = timedelta(days=2)
a + b  # 2012-09-25 00:00:00

now = datetime.today()
use_now = datetime.now()

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')

