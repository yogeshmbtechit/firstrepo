def toh(n, source, auxiliary, destination):
    if n == 1:
        print(source, "->", destination)
    else:
        toh(n - 1, auxiliary, source, destination)
        print(source, "->", destination)
        toh(n - 1, source, destination, auxiliary)

toh(3,'A', 'B', 'C')
