# -*- coding:utf-8 -*-

import os
import logging
import time

TIME=time.strftime('%Y-%m-%d-%H-%M-%S')

logFile = os.path.abspath(os.getcwd()+'/logs/')
log_path = logFile
file_extension = '.log'

logging.basicConfig(level=logging.WARNING,
                    format=' %(message)s',
                    datefmt='%S',
                    filename=os.path.join(log_path, TIME + file_extension),
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter('%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def C_CASE(msg=''):
    temp_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    logging.warning(temp_time+" CASE : " + msg)

def C_STEP(msg=''):
    temp_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    logging.warning(temp_time+" STEP : " + msg)

def C_INFO(msg=''):
    temp_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    logging.warning(temp_time+" INFO : " + msg)

def F_ERROR(msg=''):
    temp_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    logging.error(temp_time+" ERROR : " + msg)

def P_PASS(msg=''):
    temp_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    logging.error(temp_time+" PASS : " + msg)

def F_FAIL(msg=''):
    temp_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    logging.error(temp_time+" FAIL : " + msg)

