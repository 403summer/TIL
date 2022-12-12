kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score                   # 학생마다 개별로 교과 점수를 저장
        i += 1                                      # 학생 인덱스 구분
    i = 0                                           # 과목이 바뀔 때 학생 인덱스 초기화
else:
    a, b, c, d, e = student_score                   # 학생별 점수를 언패킹
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)
