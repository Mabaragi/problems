def solution(record):
    # 마지막 아이디 저장
    datas = [i.split(' ') for i in record]
    last_id = {}
    for data in datas:
        if data[0][0] != 'L':
            last_id[data[1]] = data[2]
    answer = []
    
    dct = {'Enter':'들어왔습니다.', 'Leave':'나갔습니다.'}
    for data in datas:
        if data[0][0] != 'C':
            answer.append(last_id[data[1]] + '님이 ' + dct[data[0]])
    
    return answer