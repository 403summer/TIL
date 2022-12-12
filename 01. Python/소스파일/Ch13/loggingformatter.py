import logging

logger = logging.getLogger('myapp')                 # Logger 생성
hdlr = logging.FileHandler('myapp.log')             # FileHandler 생성

formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d%(message)s') # Logging Formatter 생성: 시간, 로깅 레벨, 프로세스I D, 메시지

hdlr.setFormatter(formatter)                        # FileHandler에 formatter 등록
logger.addHandler(hdlr)                             # Logger에 'FileHandler' 등록
logger.setLevel(logging.INFO)                       # 로깅 레벨 설정

logger.error('ERROR occurred')                      # 로깅 정보 출력
logger.info('HERE WE ARE')
logger.info('TEST finished')
