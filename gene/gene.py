readfile = open("./gene.inp", 'r')
sequence_a = readfile.readline().rstrip()
a_length = len(sequence_a)
sequence_b = readfile.readline().rstrip()
b_length = len(sequence_b)
value = map(int, readfile.readline().split())
keys = ['A', 'G', 'T', 'C']
weight = dict(zip(keys, value))
readfile.close()

sub_sequence = [''] * (a_length + 1)
weight_sum = [0] * (a_length + 1)

temp_sequence = [''] * (a_length + 1)
temp_weight_sum = [0] * (a_length + 1)

for i in range(1, b_length + 1):
    b = sequence_b[i-1]

    for j in range(1, a_length + 1):
        a = sequence_a[j-1]

        left = temp_weight_sum[j-1]
        left_s = temp_sequence[j-1]
        top = weight_sum[j]
        top_s = sub_sequence[j]

        if left < top or (left == top and left_s > top_s):
            temp_weight_sum[j] = top
            temp_sequence[j] = top_s
        else:
            temp_weight_sum[j] = left
            temp_sequence[j] = left_s

        if a == b:
            left_top = weight_sum[j-1]
            left_top_s = sub_sequence[j-1]

            left_top += weight[a]
            left_top_s += a

            if (left_top > temp_weight_sum[j]) or (left_top == temp_weight_sum[j] and temp_sequence[j] > left_top_s):
                temp_weight_sum[j] = left_top
                temp_sequence[j] = left_top_s

    weight_sum = temp_weight_sum[:]
    sub_sequence = temp_sequence[:]
    print(weight_sum)

writefile = open("./gene.out", 'w')
writefile.write(sub_sequence[a_length])
writefile.close()
