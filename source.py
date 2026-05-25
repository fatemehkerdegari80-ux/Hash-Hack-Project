from hashlib import sha256
import csv
from collections import OrderedDict
def hash_password_hack(input_file_name , output_file_name):
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        hp = OrderedDict()
        new_hp = OrderedDict()
        for i in range(1000 , 10000):
            hash_jadid = sha256(str(i).encode())
            hash_jadid = hash_jadid.hexdigest()
            hp[hash_jadid] = i
        for radif in reader:
            name = radif[0]
            hash_in_reader = radif[1]
            for hach_in_hp in hp.keys():
               if hash_in_reader == hach_in_hp:
                    new_hp[name]=hp.get(hach_in_hp)
    with open(output_file_name , 'w') as out:
        count = 0
        for names in new_hp:
            count += 1
            if count == 1:
                out.write(names + ',' + str(new_hp.get(names)))
            else:
                out.write('\n' + names + ',' + str(new_hp.get(names)))
             
if __name__ == "__main__":
    hash_password_hack('input.csv', 'output.csv')
    print("عملیات با موفقیت انجام شد و نتایج در output.csv ذخیره شدند.")