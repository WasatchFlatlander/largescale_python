# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import logging
#
##logging.basicConfig(level=logging.WARNING) - only can call this once per console
#logging.getLogger().setLevel(level=logging.INFO)
#logging.getLogger().setLevel(level=logging.WARNING)
#logging.info('InfoMessage')
#logging.error('ErrorMessage')

# log to file
logging.basicConfig(filename='log.txt')
logging.error('oops')
#logging.basicConfig(filename='log.txt', filemode='w')

# use f strings
item  = 'computer'
price = 499
log_msg = 'Your {} costs ${:0.2f}.'
print(log_msg.format(item, price))
#logging with data - GOOD WAY
logging.info('Your %s costs $0.1f.', item, price)
#logging bad way - DON'T DO THIS
logging.info('Your %s costs $%0.2f.' % (item, price))
#option 2 puts string together even if log level is below threshold

## what are the format of logging - Default
#Level:logger:Msg
logging.basicConfig(format='Log level: %(levelname)s, msg: %(message)s)')
# log format attributes:

#asctime
#funcName


                   
