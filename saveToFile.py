import logging
import os

#new logger
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler('module_testing.log')
file_handler.setFormatter(format)
logger.addHandler(file_handler)

#logging.basicConfig(filename='module_testing.log', level=logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')

def namecheck(name):
    logger.debug(f"checking for '{name}'....")
    if os.path.exists('data.txt'):
        names = []
        with open('data.txt', 'r') as readfile:
            for line in readfile:
                line_name = line.split(":")[1].strip()
                names.append(line_name)
                if name.lower() == line_name.lower():
                    logger.error(f"Name: '{name}' already exists")
                    return False
        if name.lower() in [n.lower() for n in names]:
            logger.error(f"Name: '{name}' already exists")
            return False
        
        if len(name)==0:
            logger.critical("Name: can't be blank")   
            return False
        elif not name.isalpha():
            logger.critical('Name must consist alphabets only')  
            return False
        else:
            logger.error('Check successful')
            return
    else:
        logger.debug('No data found')
        return True

def saveData(name,age,mail):
    logger.debug(f"Saving the details of {name}....")
    with open('data.txt', 'a') as appendfile:
        appendfile.write(f"Name: {name} - Age: {age} - Email: {mail}\n")
        print('Details saved successfully')

logger.info('End of the savefile program')
logger.debug('############')