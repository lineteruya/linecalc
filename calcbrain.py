import re
import math
import tkinter
import tkinter.filedialog


def file_read():

    # ファイル選択ダイアログの表示
    file_path = tkinter.filedialog.askopenfilename()

    if len(file_path) != 0:
        # ファイルが選択された場合

        # ファイルを開いて読み込んでdataに格納
        f = open(file_path)
        data = f.read()
        f.close()
    else:
        # ファイル選択がキャンセルされた場合

        # dataは空にする
        data = ''

    return data


seconds = 0
minutes = 0
hours = 0
talks = data

#時間別分類
abovetenhour = re.findall('通話時間 ..:..:..',talks)#
abovehour = re.findall('通話時間 .:..:..',talks)#
aboveten = re.findall('通話時間 ..:..\n',talks) + re.findall('通話時間 ..:..$',talks)
underten = re.findall('通話時間 .:..\n',talks) + re.findall('通話時間 .:..$',talks)
aboveten = "".join(map(str, aboveten))
aboveten = aboveten.strip()
aboveten = aboveten.split('\n')
underten = "".join(map(str, underten))
underten = underten.strip()
underten = underten.split('\n')


abotenhour = ' '.join(map(str,abovetenhour)) # 通話時間 xx:xx:xx

abotenhoursec = re.findall(':..',abotenhour)
abotenhoursec = ' '.join(map(str,abotenhoursec))
abotenhoursec = re.sub('\:','',abotenhoursec)

abotenhourmin = re.findall(':..:',abotenhour)
abotenhourmin = ' '.join(map(str,abotenhourmin))
abotenhourmin = re.sub('\:','',abotenhourmin)

abotenhourhour = re.findall('..:',abotenhour)
abotenhourhour = ' '.join(map(str,abotenhourhour))
abotenhourhour = re.sub('\:','',abotenhourhour)

abotenhoursec_list = abotenhoursec.split()
abotenhoursec_list = [int(i) for i in abotenhoursec_list]
abotenhoursec_list = (abotenhoursec_list[1::2])

abotenhourmin_list = abotenhourmin.split()
abotenhourmin_list = [int(i) for i in abotenhourmin_list]

abotenhourhour_list = abotenhourhour.split()
abotenhourhour_list = [int(i) for i in abotenhourhour_list]
abotenhourhour_list = (abotenhourhour_list[0::2])


abohour = ' '.join(map(str,abovehour))

abohoursec = re.findall(':..',abohour)
abohoursec = ' '.join(map(str,abohoursec))
abohoursec = re.sub('\:','',abohoursec)

abohourmin = re.findall(':..:',abohour)
abohourmin = ' '.join(map(str,abohourmin))
abohourmin = re.sub('\:','',abohourmin)

abohourhour = re.findall('.:',abohour)
abohourhour = ' '.join(map(str,abohourhour))
abohourhour = re.sub('\:','',abohourhour)

abohoursec_list = abohoursec.split()
abohoursec_list = [int(i) for i in abohoursec_list]
abohoursec_list = (abohoursec_list[1::2])

abohourmin_list = abohourmin.split()
abohourmin_list = [int(i) for i in abohourmin_list]

abohourhour_list = abohourhour.split()
abohourhour_list = [int(i) for i in abohourhour_list]
abohourhour_list = (abohourhour_list[0::2])

aboten = ' '.join(map(str,aboveten))

abotensec = re.findall(':..',aboten)
abotensec = ' '.join(map(str,abotensec))
abotensec = re.sub('\:','',abotensec)

abotenmin = re.findall('..:',aboten)
abotenmin = ' '.join(map(str,abotenmin))
abotenmin = re.sub('\:','',abotenmin)

abotensec_list = abotensec.split()
abotensec_list = [int(i) for i in abotensec_list]

abotenmin_list = abotenmin.split()
abotenmin_list = [int(i) for i in abotenmin_list]

unten = ' '.join(map(str,underten))

untensec = re.findall(':..',unten)
untensec = ' '.join(map(str,untensec))
untensec = re.sub('\:','',untensec)

untenmin = re.findall('.:',unten)
untenmin = ' '.join(map(str,untenmin))
untenmin = re.sub('\:','',untenmin)

untensec_list = untensec.split()
untensec_list = [int(i) for i in untensec_list]

untenmin_list = untenmin.split()
untenmin_list = [int(i) for i in untenmin_list]

seconds_list = abotenhoursec_list + abohoursec_list + abotensec_list + untensec_list
minutes_list = abotenhourmin_list + abohourmin_list + abotenmin_list + untenmin_list
hours_list = abotenhourhour_list + abohourhour_list


seconds += sum(seconds_list)
second = seconds % 60
advsecond = seconds / 60
advsecond = math.floor(advsecond)
advsecond = [advsecond]
minutes = sum(minutes_list + advsecond)
minute = minutes % 60
advminute = minutes / 60
advminute = math.floor(advminute)
hours += sum(hours_list)
hour = hours + advminute
print('累計通話時間は、','',str(hour) + '時間' ,str(minute) + '分' ,str(second) + '秒','','です。',sep = '\n')
