import logging
import saveToFile as STF

#new logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(format)
logger.addHandler(file_handler)

#logging.basicConfig(filename='employee.log', level=logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')

logger.debug('Start of the employee program')

name = 'Arnob'
age = 27
email = 'sakifarnob98@gmail.com'

if STF.namecheck(name) is True:
    STF.saveData(name, age, email)
else:
    logger.critical('Employee info already exists in the database')

logger.info('End of the employee program')
logger.debug('############')