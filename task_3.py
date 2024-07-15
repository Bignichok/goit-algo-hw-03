def hanoi_tower(n, source, target, auxiliary, steps):
    if n == 1:
        steps.append(f"Move disk 1 from {source} to {target}")
        return
    hanoi_tower(n - 1, source, auxiliary, target, steps)
    steps.append(f"Move disk {n} from {source} to {target}")
    hanoi_tower(n - 1, auxiliary, target, source, steps)

def solve_hanoi_tower(n):
    steps = []
    hanoi_tower(n, 'A', 'C', 'B', steps)
    return steps

def main():
    n = int(input("Enter the number of disks: "))
    steps = solve_hanoi_tower(n)
    print("\n".join(steps))

if __name__ == "__main__":
    main()
