from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5 import QtCore
import math

app = QApplication([])
main_win = QWidget()
main_win.resize(260, 180)

# интерфейс
v_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
h4_line = QHBoxLayout()



lab = QLabel('расчет расстояния по гео-сетке')
lab.setAlignment(QtCore.Qt.AlignCenter)

lab2 = QLabel('⬇️ваш ответ⬇️')
lab2.setAlignment(QtCore.Qt.AlignCenter)

lab3 = QLabel('')
lab3.setAlignment(QtCore.Qt.AlignCenter)

btn = QPushButton('принять')
btn2 = QPushButton('принять')
btn_cas_ok = QPushButton('принять')
btn_cas_mash_ok = QPushButton('принять')



enter = QLineEdit()
enter.setPlaceholderText('сторона a × сторона b')

enter_a = QLineEdit()
enter_a.setPlaceholderText('сторона a')

enter_b = QLineEdit()
enter_b.setPlaceholderText('сторона b')
 
enter_new = QLineEdit()
enter_new.setPlaceholderText('сторона в пикселях')

enter_new_mash = QLineEdit()
enter_new_mash.setPlaceholderText('сторона в метрах')

cc = 100
dd = 100


def entering():
    if btn.text() == 'принять':
        text = enter.text()
        text_list = text.split(" × ")
        a = text_list[0]
        b = text_list[1]
        c = cc
        c = int(c)
        a2 = int(a)**2
        b2 = int(b)**2
        ab = a2+b2
        r_ab = round(math.sqrt(ab)*dd)
        answer = round(r_ab/c)
        lab3.setText(str(answer)+' м')
        enter.clear()

def entering2():
    text_a = enter_a.text()
    text_b = enter_b.text()
    a = text_a
    b = text_b
    c = cc
    c = int(c)
    a2 = int(a)**2
    b2 = int(b)**2
    ab = a2+b2
    r_ab = round(math.sqrt(ab)*dd)
    answer = round(r_ab/c)
    lab3.setText(str(answer)+' м')
    enter_a.clear()
    enter_b.clear()

def enter_castom():
    tex = enter_new.text()
    global cc
    cc = tex
    enter_new.clear()

def enter_castom_mash():
    tex2 = enter_new_mash.text()
    global dd
    cc = tex2
    enter_new_mash.clear()




# прикрепление
v_line.addWidget(lab)
v_line.addLayout(h4_line)
h4_line.addWidget(enter)
h4_line.addWidget(btn)
v_line.addLayout(h3_line)
h3_line.addWidget(enter_a)#######
h3_line.addWidget(enter_b)
h3_line.addWidget(btn2)

v_line.addWidget(lab2)
v_line.addWidget(lab3)



h1_line.addWidget(enter_new)
h1_line.addWidget(btn_cas_ok)

h2_line.addWidget(enter_new_mash)
h2_line.addWidget(btn_cas_mash_ok)




v_line.addLayout(h1_line)
v_line.addLayout(h2_line)





# конекты

btn.clicked.connect(entering)
btn2.clicked.connect(entering2)

btn_cas_ok.clicked.connect(enter_castom)
btn_cas_mash_ok.clicked.connect(enter_castom_mash)







main_win.setLayout(v_line)
main_win.show()
app.exec_()



# pip list
# pip install pyinstaller
# pyinstaller --onefile .\min.py
