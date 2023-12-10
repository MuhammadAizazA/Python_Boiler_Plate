from logs import logging_setup
import logging

if __name__=="__main__":
    logging_setup.setup_logging()
    logging.debug('This is Debug Message From Testing Module!')
    logging.info('This is Info Message From Testing Module!')
    logging.warning('This is Warning Message From Testing Module!')
    logging.error('This is Error Message From Testing Module!')
    logging.critical('This is Error Message From Testing Module!')