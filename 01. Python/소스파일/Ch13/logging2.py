import logging

logger = logging.getLogger("main")          # Logger 선언
stream_hander = logging.StreamHandler()     # Logger의 출력 방법 선언
logger.addHandler(stream_hander)            # Logger의 출력 등록
