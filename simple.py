__author__ = 'bernardo'

import gc

po = eval



str = """^for x in xrange(0, 10):^    print x"""

exec(str.replace("^", "\n"))