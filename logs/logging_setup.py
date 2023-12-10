import logging.config
import logging.handlers
import os
import yaml
def setup_logging(default_path='logs/logging.yaml', default_level=logging.DEBUG, env_key='LOG_CFG'):
    """Set up logging configuration.

    This function configures the logging system based on a YAML file containing
    logging settings. If the file is not found, it defaults to a basic configuration
    with the specified default logging level. The configuration path can be overridden
    by setting the 'LOG_CFG' environment variable.

    Args:
        default_path (str): The path to the YAML file containing the logging configuration.
            Defaults to 'logs/logging.yaml'.
        default_level (int): The default logging level to use if no configuration is found
            in the specified file. Defaults to logging.DEBUG.
        env_key (str): The environment variable key that, if set, will override the default_path.
            Defaults to 'LOG_CFG'.

    Returns:
        None
    Usage:
        Call this function at the beginning of your script or application to configure logging.
        You can set the 'LOG_CFG' environment variable to specify a custom configuration file.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        mail_handler = logging.handlers.SMTPHandler(
        mailhost=('smtp.gmail.com', 587),
        fromaddr='myapp321123@gmail.com',
        toaddrs=['sss111222333007@gmail.com'],
        subject='Error in your application',
        credentials=('myapp321123@gmail.com', 'evgq dnin chcy vehl'),
        secure=()
        )
        mail_handler.setLevel(logging.CRITICAL)
        logging.getLogger('').addHandler(mail_handler)
        logging.info('Logging loaded from yaml file is working')
    else:
        logging.basicConfig(level=default_level)
        
def test_logging_working():
    logging.debug('This is Debug Message From test_logging_working Function!')
    logging.info('This is Info Message From test_logging_working Function')
    logging.warning('This is Warning Message From test_logging_working Function')
    logging.error('This is Error Message From test_logging_working Function')
    logging.critical('This is Critical Message From test_logging_working Function')

if __name__=='__main__':
    setup_logging()
    test_logging_working()
    