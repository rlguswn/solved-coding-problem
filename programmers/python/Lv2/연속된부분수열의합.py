def solution(sequence, k):
    i = j = len(sequence) - 1
    s = sequence[i]
    while(1):
        if s > k:
            s -= sequence[j]
            i -= 1
            j -= 1
            s += sequence[i]
        elif s < k:
            i -= 1
            s += sequence[i]
        else:
            if sequence.index(sequence[i]) != i and sequence[i-1] == sequence[j]:
                i, j = sequence.index(sequence[i]), j-i+sequence.index(sequence[i])
            break
    return [i, j]