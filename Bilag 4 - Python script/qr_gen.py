import qrcode
import os

dir_list = []
folder_list = []
project_web = "http://130.61.200.19/Byggeprojekt/"
directory = 'C:/Users/TurboNotik-PC/Aalborg Universitet/Gruppe - 1.317 - Documents/3. semester ' \
            '1.317/Semesterprojekt/Rapport/Scripts/Byggeprojekt/'

directory = os.path.normpath(directory)
for sub_dir in [x[0] for x in os.walk(directory)]:
    dir_name = sub_dir.split(os.sep)
    dir_list.append(dir_name)
    
removed = dir_list.pop(0)

for entry in dir_list:
    folder_list.append(entry[-1])

for i in folder_list:
    input_data = project_web + i + '/'
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(directory + '/' + i + '/' + 'qr_' + str(i) + '.png')
