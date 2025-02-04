## record
## Enter 유저아이디 닉네임
## Leave 유저아이디 닉네임
## Change 유저아이디 닉네임

def solution(record):
    answer = []
    user = dict()
    for i, v in enumerate(record):
        command = v.split()
        
        if command[0] == "Enter":
            user[command[1]] = command[2]
            answer.append(f"{command[1]} Enter")

        if command[0] == "Leave":
            answer.append(f"{command[1]} Leave")

        if command[0] == "Change":
            user[command[1]] = command[2]
            
    for i in range(len(answer)):
        uid, c = answer[i].split()
        if c == "Enter":
            answer[i] = f"{user[uid]}님이 들어왔습니다."
        elif c == "Leave":
            answer[i] = f"{user[uid]}님이 나갔습니다."
    
    return answer