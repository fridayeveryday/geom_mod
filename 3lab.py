# This is a sample Python script.
import os

path = "C://Temp/gm.txt"
out_path = "C://Temp/UUE.txt"

def to_UUE(bin_list):
    concated_str = [str(elem) for elem in bin_list]
    concated_str = "".join(concated_str)
    quad_symb_of_UUE = ""
    for i in range(4):
        first = int(concated_str[0:6], 2) + 32
        sec = int(concated_str[6:12], 2) + 32
        third = int(concated_str[12:18], 2) + 32
        fouth = int(concated_str[18:24], 2) + 32
        quad_symb_of_UUE += (chr(int(concated_str[i * 6:(i + 1) * 6], 2) + 32))
    return quad_symb_of_UUE


def to_normal_bin(num):
    res = ""
    while num > 0:
        res += str(num % 2)
        num //= 2
    res += str(0) * (8 - len(res))
    return res[::-1]


def main():
    file = open(path, "a")
    size = os.stat(path).st_size
    remains = size % 3
    if remains > 0:
        adding_str = ' ' * (3 - remains) #'`'
        file.write(adding_str)
    file.close()
    results = []
    byte_counter = 0
    with open(path, "rb") as file:
        one_UUE_line = ""
        while True:
            local_converted_bytes_2_bin = [] * 3
            triple_bytes = file.read(3)
            if triple_bytes == b"":
                break
            byte_counter += 3
            for i, elem in enumerate(triple_bytes):
                local_converted_bytes_2_bin.append(to_normal_bin(elem))
            one_UUE_line += to_UUE(local_converted_bytes_2_bin)
            if byte_counter == 45:
                byte_counter = 0
                results.append("M")
                results.append(one_UUE_line)
                one_UUE_line = ""
                results.append('\n')
        if byte_counter != 0:
            results.append(chr(32 + byte_counter))
            results.append(one_UUE_line)
    with open(out_path, "w") as out_file:
        for item in results:
            out_file.write(str(item))
        out_file.write('\n`')


if __name__ == '__main__':
    main()

