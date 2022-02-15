import re
import glob
import os

def get_filename(alpha = [0,0], phase=[90,-90]):
    return f'CsD1-43-det0-D2-44-det25-rabi0-eliptic-alpha_{alpha[0]}_{alpha[1]}-phase_{phase[0]}_{phase[1]}.out'
    # return f'/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Circular_polarization_angle_phase/CsD1-43_D2-44-det25-rabi20-alpha_0_0-phase_90_-0.out'

def get_filepath(alpha = [0,0], phase=[90,-90]):
    foldername = f'/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Circular_polarization_angle_phase/'
    filename = f'CsD1-43_D2-44-det25-rabi20-alpha_{alpha[0]}_{alpha[1]}-phase_{phase[0]}_{phase[1]}.out'

def extract_lines(filename, foldername='', startline = 13):
    a_file = open(filename, "r")
    lines = a_file.readlines()
    a_file.close()

    split_path = os.path.split(filename)


    # for idx_lines, line in enumerate(lines):
    #     print(idx_lines, line)
    # print(foldername)
    if len(foldername) > 0:
        new_foldername = f'{split_path[0]}/{foldername}'
        new_filename = split_path[1]
        if new_filename.startswith('0'):
            new_filename = new_filename[1:]
        if not os.path.exists(new_foldername):
            os.makedirs(new_foldername)
        new_file_path = f"{new_foldername}/{new_filename[:-4]}.txt"
    else:
        new_file_path = f"{filename[:-4]}.txt"
    # print(new_file_path)
    new_file = open(new_file_path, "w")

    idx_lines = startline
    while idx_lines <= len(lines):
        # print(lines[idx_lines])
        # print(re.split('B -> |; step: 10;\n|; step: 1;\n', lines[idx_lines])[1])
        B = re.split('B -> |; step: 10;\n|; step: 1;\n', lines[idx_lines])[1]

        idx_comp = idx_lines + 5
        if idx_comp > len(lines):
            break
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

    foldername = f'/home/laima/Documents/Pētījumi/AOC Rb (2018-)/Circular_polarization_angle_phase/'
    filenames = sorted(glob.glob(f"{foldername}/*CsD1-43_D2-44-det25-rabi*0-alpha*.out"))
    filenames = filenames[::1]

    save_folder = 'extracted_out_files'

    for filename in filenames:
        print(filename)
        for start in [13, 17, 14]:
            try:
                extract_lines(filename, foldername=save_folder, startline=start)
                break
            except Exception as e:
                print(start, e)
                continue
                # extract_lines(filename, foldername=save_folder, startline=17)

