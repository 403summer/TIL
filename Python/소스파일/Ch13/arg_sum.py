import argparse                 # argparse 모듈의 호출

parser = argparse.ArgumentParser(description='Sum two integers.')           # 기본 설정 도움말

parser.add_argument('-a',"--a_value", dest="a", help="A integers", type=int) # a 인자(argument) 추가
parser.add_argument('-b',"--b_value", dest="b", help="B integers", type=int) # b 인자(argument) 추가

args = parser.parse_args()      # 입력된 커맨드 라인 인자 파싱(command line argument parsing)

print(args)                     # 결과 출력
print(args.a)
print(args.b)
print(args.a + args.b)
