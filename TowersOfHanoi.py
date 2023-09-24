#Towers of Hanoi
def towers_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
if __name__ == "__main__":
    n = 3  # Number of disks
    towers_of_hanoi(n, 'A', 'B', 'C')