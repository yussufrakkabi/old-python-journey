def hanoi_solver(n):
    if n <= 0:
        return ""
    rods = [[i for i in range(n, 0, -1)], [], []]
    states = []
    
    def state_str():
        return ' '.join(str(rod) for rod in rods)
    
    def move(from_rod, to_rod):
        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        states.append(state_str())
    
    def solve(k, src, dest, aux):
        if k == 0:
            return
        solve(k-1, src, aux, dest)
        move(src, dest)
        solve(k-1, aux, dest, src)
    
    states.append(state_str())  # initial state
    solve(n, 0, 2, 1)
    return '\n'.join(states)


print(hanoi_solver(6))