# method 1

# n_files = 10000
# files = []
#
# for i in range(n_files):
#     files.append(open('output1/sample%i.txt' % i, 'w'))

# method 2

# n_files = 1000
# files = []
#
# for i in range(n_files):
#     f = open('output1/sample%i.txt' % i, 'w')
#     files.append(f)
#     f.close()

# method 3

n_files = 254
files = []

for i in range(n_files):
    with open('output1/sample%i.txt' % i, 'w') as f:
        files.append(f)

