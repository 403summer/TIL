with open("dream.txt","r") as my_file:
    content_list = my_file.readlines()      # 파일 전체를 리스트로 반환
    print(type(content_list))               # 자료형 확인
    print(content_list)                     # 리스트값 출력
