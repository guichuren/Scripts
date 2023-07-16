import linecache

orig_file = "OUTCAR"
final_file = "POSCAR-"

atom_list = linecache.getline("SPOSCAR", 7).split()
num_atom = 0

for index in range(len(atom_list)):
    num_atom += int(atom_list[index])


line = 1
line_num = []

sign = True
while sign:
    if linecache.getline(orig_file, line) == '':
        break

    else:
        if len(linecache.getline(orig_file, line).split()) > 3:
            if linecache.getline(orig_file, line).split()[1] == "f/i=":
 #               fi_count += 1
                line_num.append(line)
            

    line += 1

fi_num = len(line_num)

for index in range(fi_num):
    writing_file = final_file + str(index + 1)
    with open(writing_file, "w") as tmp_write:
        for i in range(7):
            tmp_write.write(linecache.getline("SPOSCAR", i+1))

        tmp_write.write("Cartesian\n")
        for atom_index in range(num_atom):
            tmp_orig_line = linecache.getline(orig_file, line_num[index] + 2 + atom_index).split()
            tmp_x = str(round((float(tmp_orig_line[0]) + float(tmp_orig_line[3])), 6))
            tmp_y = str(round((float(tmp_orig_line[1]) + float(tmp_orig_line[4])), 6))
            tmp_z = str(round((float(tmp_orig_line[2]) + float(tmp_orig_line[5])), 6))
            tmp_writing_line = tmp_x + "\t" + tmp_y + "\t" + tmp_z + "\n"
            tmp_write.write(tmp_writing_line)
