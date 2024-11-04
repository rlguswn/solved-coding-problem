def sortSize(arr):
    if arr[0] >= arr[1]:
        return arr
    s = arr[0]
    arr[0] = arr[1]
    arr[1] = s
    return arr

def solution(wallet, bill):
    answer = 0
    
    while(1):
        wallet = sortSize(wallet)
        bill = sortSize(bill)
        
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            break
        
        bill[0] = bill[0]//2
        answer += 1
            
    return answer