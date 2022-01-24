import re
import glob

def get_filename(alpha = [0,0], phase=[90,-90]):
    return f'CsD1-43-det0-D2-44-det25-rabi0-eliptic-alpha_{alpha[0]}_{alpha[1]}-phase_{phase[0]}_{phase[1]}.out'

def extract_lines(filename):
    a_file = open(filename, "r")
    lines = a_file.readlines()
    a_file.close()

    # for idx_lines, line in enumerate(lines):
    #     print(idx_lines, line)
    new_file = open(f"{filename[:-4]}.txt", "w")

    idx_lines = 13
    while idx_lines <= len(lines):
        # print(lines[idx_lines])
        # print(re.split('B -> |; step: 10;\n', lines[idx_lines])[1])
        B = re.split('B -> |; step: 10;\n', lines[idx_lines])[1]

        idx_comp = idx_lines + 5
        comp_line = re.split('abs circ_1: |; abs circ_2: | ; abs intensity sum: |; abs starpiba: |\n', lines[idx_comp])

        # print(B, comp_line[3], comp_line[1], comp_line[2], comp_line[4])
        new_file.write(f'{B} {comp_line[3]} {comp_line[1]} {comp_line[2]} {comp_line[4]}\n')

        idx_lines += 9



if __name__ == '__main__':

    # alpha = [-45,-45]
    # phase = [90,-90]
    #
    # filename = get_filename(alpha=alpha, phase=phase)
    # print(filename)
    #
    # import_file(filename)

    filenames = sorted(glob.glob("*.out"))
    # filenames = filenames[::1]

    for filename in filenames:
        print(filename)
        extract_lines(filename)

