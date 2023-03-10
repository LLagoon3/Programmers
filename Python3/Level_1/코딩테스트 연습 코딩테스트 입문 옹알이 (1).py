#https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    answer = 0
    for sentence in babbling:
        while 1:
            if len(sentence) >= 3 and (sentence[0:3] == 'aya' or sentence[0:3] == 'woo'):
                sentence = sentence[3:]
            elif len(sentence) >= 2 and (sentence[0:2] == 'ye' or sentence[0:2] == 'ma'):
                sentence = sentence[2:]
            else:
                break
        if len(sentence) == 0:
            answer += 1
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))