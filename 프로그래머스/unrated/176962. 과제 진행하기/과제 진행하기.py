def solution(plans):
    plans = [[i[0], int(i[1][:2]) * 60 + int(i[1][3:5]), int(i[2])] for i in plans]
    plans.sort(key=lambda x: x[1])
    N = len(plans)

    task = plans[0]
    now = task[1]
    not_done = []
    done = []
    i = 1
    while i < N:
        next_task = plans[i]
        name, body, play_time = task
        if next_task[1] < now + play_time:
            not_done.append([name, 0, now + play_time - next_task[1]])
            task = plans[i]
            now = task[1]
            i += 1
        else:
            done.append(name)
            if not_done:
                task = not_done.pop()
                now += play_time
            else:
                task = plans[i]
                now = task[1]
                i += 1

    done.append(task[0])
    M = len(not_done)
    for _ in range(M):
        done.append(not_done.pop()[0])
    return done