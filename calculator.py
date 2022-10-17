import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.operand_1 = ''
        self.operand_2 = ''
        self.my_input = ''

    def initUI(self):
        self.setGeometry(400, 400, 280, 360)
        self.setWindowTitle("Калькулятор")
        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(150, 100)
        self.label.move(130, 5)
        self.move(50, 50)

        self.num_1 = QPushButton('1',self)
        self.num_1.resize(50,50)
        self.num_1.move(5,100)
        self.num_1.clicked.connect(self.one)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 100)
        self.num_2.clicked.connect(self.two)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 100)
        self.num_3.clicked.connect(self.three)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 150)
        self.num_4.clicked.connect(self.four)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 150)
        self.num_5.clicked.connect(self.five)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 150)
        self.num_6.clicked.connect(self.six)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 200)
        self.num_7.clicked.connect(self.seven)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 200)
        self.num_8.clicked.connect(self.eight)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 200)
        self.num_9.clicked.connect(self.nine)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(150, 50)
        self.num_0.move(10, 250)
        self.num_0.clicked.connect(self.zero)

        self.tocka = QPushButton('.', self)
        self.tocka.resize(50, 50)
        self.tocka.move(225, 300)
        self.tocka.clicked.connect(self.Tochka)

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 100)
        self.plus.clicked.connect(self.Plus)

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(170, 150)
        self.minus.clicked.connect(self.Minus)

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 200)
        self.mul.clicked.connect(self.Mult)

        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(170, 250)
        self.div.clicked.connect(self.Diviz)

        self.procent = QPushButton('%', self)
        self.procent.resize(50, 50)
        self.procent.move(170, 300)
        self.procent.clicked.connect(self.Ost)

        self.ravno = QPushButton('=', self)
        self.ravno.resize(150, 50)
        self.ravno.move(10, 300)
        self.ravno.clicked.connect(self.Ravno)

        self.clear = QPushButton('C', self)
        self.clear.resize(50, 50)
        self.clear.move(225, 100)
        self.clear.clicked.connect(self.Clear)

        self.ost = QPushButton('/%', self)
        self.ost.resize(50, 50)
        self.ost.move(225, 150)
        self.ost.clicked.connect(self.Ostatok_1)


        self.vozv_2 = QPushButton('x^2', self)
        self.vozv_2.resize(50, 50)
        self.vozv_2.move(225, 200)
        self.vozv_2.clicked.connect(self.Vozved_v_2)

        self.vozved = QPushButton('x^y', self)
        self.vozved.resize(50, 50)
        self.vozved.move(225, 250)
        self.vozved.clicked.connect(self.Vozved_v_step)


    def enterValue(self):
        if self.label.text() == '0' or self.n:
            self.label.setText('')
            self.n = False
        self.label.setText(self.label.text() + self.my_input)

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def Plus(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def Minus(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def Mult(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def Diviz(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def Ost(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def Clear(self):
        self.label.setText('')

    def Tochka(self):
        if '.' not in self.label.text():
            self.my_input = '.'
            self.enterValue()

    def Ostatok_1(self):
        self.operation = '/%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def Vozved_v_2(self):
        self.operation = 'x^2'
        self.operand_1 = float(self.label.text())
        self.label.setText(str(self.operand_1 ** 2))

    def Vozved_v_step(self):
        self.operation = 'x^y'
        self.operand_1 = float(self.label.text())
        self.label.setText('')




    def Ravno(self):
        self.n = True
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'Ошибка! Деление на 0!'
            else:
                self.rezult = self.operand_1 / self.operand_2
        elif self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '//':
            if self.operand_2 == 0:
                self.rezult = 'Ошибка! Деление на 0!'
            else:
                self.rezult = int(self.operand_1 / self.operand_2)
        elif self.operation == '/%':
            if self.operand_2 == 0:
                self.rezult = 'Ошибка! Деление на 0!'
            else:
                self.rezult = int(self.operand_1 % self.operand_2)
        elif self.operation == 'x^y':
            self.rezult = int(self.operand_1 ** self.operand_2)

        self.label.setText(str(self.rezult))




app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec())