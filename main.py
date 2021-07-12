import sys
from PyQt5.QtWidgets import QApplication
from load import Ui_Form_load
from f_load import Ui_Form_f_load
from sudent import Ui_Form_student
from company import Ui_Form_company
from company_info import  Ui_Form_company_info
from company_update import Ui_Form_company_update
from interview import Ui_Form_interview
from job_fair import Ui_Form_job_fair
from school import Ui_Form_school
from statistic import Ui_Form_statistic
from student_base_info import Ui_Form_student_base_info
from student_base_update import Ui_Form_student_base_update
from student_study_info import Ui_Form_student_study_info
from student_study_update import Ui_Form_student_study_update
from success import Ui_Form_success
from no_need import Ui_Form_no_need
from false_ import Ui_Form_false_
from bottom import Ui_Form_bottom
from job_fair_s import  Ui_Form_job_fair_s
from attention import Ui_Form_attention
from fair_choose import Ui_Form_fair_choose
from api import IsCompany,IsSchool,IsStudent,Student_base_info_sql,Student_study_info_sql,Company_info_sql,Student_study_update_sql,Student_base_update_sql,Company_update_sql,Interview_sql,Job_fair_apply_sql,Statistic_sql,Fair_choose_sql,Job_fair_sql,Job_fair_s_sql

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter,QPen,QFont,QPixmap,QIcon
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QDialog,QFileDialog,QLabel,QInputDialog,QVBoxLayout,QPushButton,QAction,QColorDialog


class Fair_choose(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui=Ui_Form_fair_choose()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        num, L = Fair_choose_sql()
        for i in range(num):
            self.child_ui.comboBox.addItem('名字：%s  地点：%s'%(L[i][0], L[i][1]))

    def onclick1(self):
        fair_choose.hide()
        if student.now == 3:
            job_fair_s.fair_seq = self.child_ui.comboBox.currentIndex() + 1
            job_fair_s.show()
        else:
            job_fair_s.fair_seq = self.child_ui.comboBox.currentIndex() + 1
            job_fair.show()


class Bottom(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui=Ui_Form_bottom()
        self.child_ui.setupUi(self)

class Attention(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_attention()
        self.child_ui.setupUi(self)

class Success(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_success()
        self.child_ui.setupUi(self)

class False_(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui=Ui_Form_false_()
        self.child_ui.setupUi(self)

class No_need(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui=Ui_Form_no_need()
        self.child_ui.setupUi(self)

class Fail_Load(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui=Ui_Form_f_load()
        self.child_ui.setupUi(self)

class LoadWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui=Ui_Form_load()
        self.main_ui.setupUi(self)
        self.user = self.main_ui.lineEdit
        self.passward = self.main_ui.lineEdit_2
        self.main_ui.pushButton.clicked.connect(self.onclick)
        self.flag = 0
    def onclick(self):
        if self.login() == 1:
            self.flag = 1
            load.hide()
            student.show()
        elif self.login() == 2:
            self.flag = 1
            load.hide()
            company.show()
        elif self.login() == 3:
            self.flag = 1
            load.hide()
            school.show()
        else:
            f_load.show()
    def login(self):
        if IsStudent(self.user.text(), self.passward.text()):
            return 1
        elif IsCompany(self.user.text(), self.passward.text()):
            return 2
        elif IsSchool(self.user.text(), self.passward.text()):
            return 3
        else:
            return 4

class Student(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui=Ui_Form_student()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.child_ui.pushButton_3.clicked.connect(self.onclick3)
        self.now = 0

    def onclick1(self):
        if load.flag == 1:
            a, b, c, d, e, f, g, h, i, k, l = Student_study_info_sql(load.user.text())
            student_study_info.child_ui.textBrowser.setText(a)
            student_study_info.child_ui.textBrowser_2.setText(b)
            student_study_info.child_ui.textBrowser_3.setText(c)
            student_study_info.child_ui.textBrowser_4.setText(d)
            student_study_info.child_ui.textBrowser_5.setText(e)
            student_study_info.child_ui.textBrowser_6.setText(f)
            student_study_info.child_ui.textBrowser_7.setText(g)
            student_study_info.child_ui.textBrowser_8.setText(h)
            student_study_info.child_ui.textBrowser_9.setText(i)
            student_study_info.child_ui.textBrowser_10.setText(k)
            student_study_info.child_ui.textBrowser_11.setText(l)

            student_study_update.child_ui.textBrowser_2.setText(b)
            student_study_update.child_ui.textBrowser_3.setText(c)
            student_study_update.child_ui.textBrowser_5.setText(e)
        student.hide()
        student_study_info.show()

    def onclick2(self):
        if load.flag == 1:
            a, b, c, d, e, f, g, h, i, k, l, m = Student_base_info_sql(load.user.text())
            student_base_info.child_ui.textBrowser.setText(a)
            student_base_info.child_ui.textBrowser_2.setText(b)
            student_base_info.child_ui.textBrowser_3.setText(c)
            student_base_info.child_ui.textBrowser_4.setText(d)
            student_base_info.child_ui.textBrowser_5.setText(e)
            student_base_info.child_ui.textBrowser_6.setText(f)
            student_base_info.child_ui.textBrowser_7.setText(g)
            student_base_info.child_ui.textBrowser_8.setText(h)
            student_base_info.child_ui.textBrowser_9.setText(i)
            student_base_info.child_ui.textBrowser_10.setText(k)
            student_base_info.child_ui.textBrowser_11.setText(l)
            student_base_info.child_ui.textBrowser_12.setText(m)

            student_base_update.child_ui.textBrowser_2.setText(b)
            student_base_update.child_ui.textBrowser_4.setText(d)
            student_base_update.child_ui.textBrowser_5.setText(e)
            student_base_update.child_ui.textBrowser_6.setText(f)
            student_base_update.child_ui.textBrowser_10.setText(k)
            student_base_update.child_ui.textBrowser_11.setText(l)
            student_base_update.child_ui.textBrowser_12.setText(m)
        student.hide()
        student_base_info.show()

    def onclick3(self):
        self.now = 3
        student.hide()
        fair_choose.show()

class Student_base_info(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_student_base_info()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        a, b, c, d, e, f, g, h, i, k, l, m = Student_base_info_sql(load.user.text())
        self.child_ui.textBrowser.setText(a)
        self.child_ui.textBrowser_2.setText(b)
        self.child_ui.textBrowser_3.setText(c)
        self.child_ui.textBrowser_4.setText(d)
        self.child_ui.textBrowser_5.setText(e)
        self.child_ui.textBrowser_6.setText(f)
        self.child_ui.textBrowser_7.setText(g)
        self.child_ui.textBrowser_8.setText(h)
        self.child_ui.textBrowser_9.setText(i)
        self.child_ui.textBrowser_10.setText(k)
        self.child_ui.textBrowser_11.setText(l)
        self.child_ui.textBrowser_12.setText(m)
    def onclick1(self):
        #student_base_info.hide()
        student_base_update.show()
        attention.show()

    def onclick2(self):
        student_base_info.hide()
        student.show()

class Student_base_update(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_student_base_update()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.flag_ = False
        self.child_ui.textBrowser.setText('不可更改')

    def onclick1(self):

        #更新页面
        self.flag_, a, b, c, d, e, f, g, h, i, k, l, m = Student_base_update_sql(load.user.text(), self.child_ui.textBrowser.toPlainText(), self.child_ui.textBrowser_2.toPlainText(), self.child_ui.comboBox_7.currentText(), self.child_ui.textBrowser_4.toPlainText(), self.child_ui.textBrowser_5.toPlainText(),
                                                                            self.child_ui.textBrowser_6.toPlainText(),
                                                                            self.child_ui.comboBox_8.currentText(),
                                                                            self.child_ui.comboBox_9.currentText(),
                                                                            self.child_ui.comboBox_10.currentText(),
                                                                            self.child_ui.textBrowser_10.toPlainText(),
                                                                            self.child_ui.textBrowser_11.toPlainText(),
                                                                            self.child_ui.textBrowser_12.toPlainText())

        if self.flag_ == True:
            #student_base_info.child_ui.textBrowser.setText(a)
            student_base_info.child_ui.textBrowser_2.setText(b)
            student_base_info.child_ui.textBrowser_3.setText(c)
            student_base_info.child_ui.textBrowser_4.setText(d)
            student_base_info.child_ui.textBrowser_5.setText(e)
            student_base_info.child_ui.textBrowser_6.setText(f)
            student_base_info.child_ui.textBrowser_7.setText(g)
            student_base_info.child_ui.textBrowser_8.setText(h)
            student_base_info.child_ui.textBrowser_9.setText(i)
            student_base_info.child_ui.textBrowser_10.setText(k)
            student_base_info.child_ui.textBrowser_11.setText(l)
            student_base_info.child_ui.textBrowser_12.setText(m)
            success.show()

        elif self.flag_ == False:
            false_.show()
        else:
            no_need.show()


    def onclick2(self):
        student_base_update.hide()
        student_base_info.show()

class Student_study_info(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_student_study_info()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        a, b, c, d, e, f, g, h, i, k, l= Student_study_info_sql(load.user.text())
        self.child_ui.textBrowser.setText(a)
        self.child_ui.textBrowser_2.setText(b)
        self.child_ui.textBrowser_3.setText(c)
        self.child_ui.textBrowser_4.setText(d)
        self.child_ui.textBrowser_5.setText(e)
        self.child_ui.textBrowser_6.setText(f)
        self.child_ui.textBrowser_7.setText(g)
        self.child_ui.textBrowser_8.setText(h)
        self.child_ui.textBrowser_9.setText(i)
        self.child_ui.textBrowser_10.setText(k)
        self.child_ui.textBrowser_11.setText(l)

    def onclick1(self):
        #student_study_info.hide()
        student_study_update.show()
        attention.show()

    def onclick2(self):
        student_study_info.hide()
        student.show()

class Student_study_update(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_student_study_update()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.flag_ = False
        self.child_ui.textBrowser.setText('不可更改')

    def onclick1(self):

        self.flag_, a, b, c, d, e, f, g, h, i, k, l = Student_study_update_sql(load.user.text(),
                                                                                 self.child_ui.textBrowser.toPlainText(),
                                                                                 self.child_ui.textBrowser_2.toPlainText(),
                                                                                 self.child_ui.textBrowser_3.toPlainText(),
                                                                                 self.child_ui.comboBox.currentText(),
                                                                                 self.child_ui.textBrowser_5.toPlainText(),
                                                                                 self.child_ui.comboBox_2.currentText(),
                                                                                 self.child_ui.comboBox_3.currentText(),
                                                                                 self.child_ui.comboBox_4.currentText(),
                                                                                 self.child_ui.comboBox_5.currentText(),
                                                                                 self.child_ui.comboBox_6.currentText(),
                                                                                 self.child_ui.comboBox_7.currentText())
        if self.flag_ == True:
            #student_study_info.child_ui.textBrowser.setText(a)
            student_study_info.child_ui.textBrowser_2.setText(b)
            student_study_info.child_ui.textBrowser_3.setText(c)
            student_study_info.child_ui.textBrowser_4.setText(d)
            student_study_info.child_ui.textBrowser_5.setText(e)
            student_study_info.child_ui.textBrowser_6.setText(f)
            student_study_info.child_ui.textBrowser_7.setText(g)
            student_study_info.child_ui.textBrowser_8.setText(h)
            student_study_info.child_ui.textBrowser_9.setText(i)
            student_study_info.child_ui.textBrowser_10.setText(k)
            student_study_info.child_ui.textBrowser_11.setText(l)
            success.show()

        elif self.flag_ == False:
            false_.show()
        else:
            no_need.show()


    def onclick2(self):
        student_study_update.hide()
        student_study_info.show()

class Statistic(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_statistic()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_3.clicked.connect(self.onclick2)
        self.child_ui.pushButton_2.clicked.connect(self.onclick3)
        self.seq = 1
        self.num1 = 3
        a = Statistic_sql(self.seq)
        self.child_ui.textBrowser.setText(a)

    def onclick1(self):
        statistic.hide()
        school.show()

    def onclick2(self):
        if self.seq-1 > 0:
            a = Statistic_sql(self.seq - 1)
            self.child_ui.textBrowser.setText(a)
            self.seq -= 1
        else:
            bottom.show()

    def onclick3(self):
        if self.seq < self.num1:
            a = Statistic_sql(self.seq + 1)
            self.child_ui.textBrowser.setText(a)
            self.seq += 1
        else:
            bottom.show()


class School(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_school()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.now = 0

    def onclick1(self):
        school.hide()
        statistic.show()

    def onclick2(self):
        self.now = 1
        school.hide()
        fair_choose.show()

class Job_fair(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_job_fair()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.child_ui.pushButton_3.clicked.connect(self.onclick3)
        self.fair_seq = 1
        self.seq = 1
        self.num1 = 0
        self.num1, a, b, c = Job_fair_sql(str(self.fair_seq), self.seq)
        self.child_ui.textBrowser_12.setText(a)
        self.child_ui.textBrowser_13.setText(b)
        self.child_ui.textBrowser_14.setText(c)
        #发送信息
    def onclick1(self):
        if self.seq-1 > 0:
            self.flag1, a, b, c = Job_fair_sql(str(self.fair_seq), self.seq - 1)
            self.child_ui.textBrowser_12.setText(a)
            self.child_ui.textBrowser_13.setText(b)
            self.child_ui.textBrowser_14.setText(c)
            self.seq -= 1
        else:
            bottom.show()

    def onclick2(self):
        if self.seq < self.num1:
            self.flag1, a, b, c = Job_fair_sql(str(self.fair_seq), self.seq + 1)
            self.child_ui.textBrowser_12.setText(a)
            self.child_ui.textBrowser_13.setText(b)
            self.child_ui.textBrowser_14.setText(c)
            self.seq += 1
        else:
            bottom.show()

    def onclick3(self):
        job_fair.hide()
        if school.now != 0:
            school.now = 0
            school.show()
        else:
            company.now = 0
            company.show()

class Job_fair_s(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_job_fair_s()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton_4.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.child_ui.pushButton_3.clicked.connect(self.onclick3)
        self.child_ui.pushButton.clicked.connect(self.onclick4)
        self.fair_seq = 1
        self.seq = 1
        self.num1 = 0
        self.num1, a, b, c, d, e = Job_fair_s_sql(str(self.fair_seq), self.seq)
        self.child_ui.textBrowser_12.setText(a)
        self.child_ui.textBrowser_13.setText(b)
        self.child_ui.textBrowser_14.setText(c)
        self.child_ui.textBrowser_16.setText(d)
        self.child_ui.textBrowser_15.setText(e)

    def onclick1(self):
        if self.seq-1 > 0:
            self.num1, a, b, c, d, e = Job_fair_s_sql(str(self.fair_seq), self.seq - 1)
            self.child_ui.textBrowser_12.setText(a)
            self.child_ui.textBrowser_13.setText(b)
            self.child_ui.textBrowser_14.setText(c)
            self.child_ui.textBrowser_16.setText(d)
            self.child_ui.textBrowser_15.setText(e)
            self.seq -= 1
        else:
            bottom.show()

    def onclick2(self):
        if self.seq < self.num1:
            self.num1, a, b, c, d, e = Job_fair_s_sql(str(self.fair_seq), self.seq + 1)
            self.child_ui.textBrowser_12.setText(a)
            self.child_ui.textBrowser_13.setText(b)
            self.child_ui.textBrowser_14.setText(c)
            self.child_ui.textBrowser_16.setText(d)
            self.child_ui.textBrowser_15.setText(e)
            self.seq += 1
        else:
            bottom.show()

    def onclick3(self):
        job_fair_s.hide()
        student.show()

    def onclick4(self):
        if Job_fair_apply_sql(load.user.text(), self.child_ui.textBrowser_16):
            success.show()
        else:
            no_need.show()

class Interview(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_interview()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)

    def onclick1(self):

        if Interview_sql(load.user.text(),self.child_ui.textBrowser.toPlainText(), self.child_ui.textBrowser_3.currentText(), self.child_ui.textBrowser_4.toPlainText()) == True:
            success.show()

        elif Interview_sql(load.user.text(),self.child_ui.textBrowser.toPlainText(), self.child_ui.textBrowser_3.currentText(), self.child_ui.textBrowser_4.toPlainText()) == False:
            false_.show()

        else:
            no_need.show()
            no_need.hide()

    def onclick2(self):
        interview.hide()
        company.show()

class Company(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_company()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.child_ui.pushButton_3.clicked.connect(self.onclick3)
        self.now = 0

    def onclick1(self):
        if load.flag == 1:
            a, b, c, d, e, f, g = Company_info_sql(load.user.text())
            company_info.child_ui.textBrowser.setText(a)
            company_info.child_ui.textBrowser_2.setText(b)
            company_info.child_ui.textBrowser_3.setText(c)
            company_info.child_ui.textBrowser_4.setText(d)
            company_info.child_ui.textBrowser_5.setText(e)
            company_info.child_ui.textBrowser_6.setText(f)
            company_info.child_ui.textBrowser_7.setText(g)

            company_update.child_ui.textEdit.setText(a)
            company_update.child_ui.textEdit_2.setText(b)
            company_update.child_ui.textEdit_3.setText(d)
            company_update.child_ui.textEdit_4.setText(f)
            company_update.child_ui.textEdit_5.setText(g)
            company_update.child_ui.textEdit_6.setText(e)
        company.hide()
        company_info.show()

    def onclick2(self):
        self.now = 2
        company.hide()
        fair_choose.show()

    def onclick3(self):
        company.hide()
        interview.show()

class Company_info(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_company_info()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        a, b, c, d, e, f, g = Company_info_sql(load.user.text())
        self.child_ui.textBrowser.setText(a)
        self.child_ui.textBrowser_2.setText(b)
        self.child_ui.textBrowser_3.setText(c)
        self.child_ui.textBrowser_4.setText(d)
        self.child_ui.textBrowser_5.setText(e)
        self.child_ui.textBrowser_6.setText(f)
        self.child_ui.textBrowser_7.setText(g)

    def onclick1(self):
        #company_info.hide()
        company_update.child_ui.textEdit.setText('不可更改')
        company_update.child_ui.textEdit_3.setText('不可更改')
        company_update.show()
        attention.show()

    def onclick2(self):
        company_info.hide()
        company.show()

class Company_update(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child_ui = Ui_Form_company_update()
        self.child_ui.setupUi(self)
        self.child_ui.pushButton.clicked.connect(self.onclick1)
        self.child_ui.pushButton_2.clicked.connect(self.onclick2)
        self.flag_ = False

    def onclick1(self):

        self.flag_, a, b, c, d, e, f, g = Company_update_sql(load.user.text(),
                                                                                 self.child_ui.textEdit.toPlainText(),
                                                                                 self.child_ui.textEdit_2.toPlainText(),
                                                                                 self.child_ui.comboBox.currentText(),
                                                                                 self.child_ui.textEdit_3.toPlainText(),
                                                                                 self.child_ui.textEdit_4.toPlainText(),
                                                                                 self.child_ui.textEdit_5.toPlainText(),
                                                                                 self.child_ui.textEdit_6.toPlainText())

        if self.flag_ == True:
            #company_info.child_ui.textBrowser.setText(a)
            company_info.child_ui.textBrowser_2.setText(b)
            company_info.child_ui.textBrowser_3.setText(c)
            company_info.child_ui.textBrowser_4.setText(d)
            company_info.child_ui.textBrowser_5.setText(e)
            company_info.child_ui.textBrowser_6.setText(f)
            company_info.child_ui.textBrowser_7.setText(g)
            success.show()

        elif self.flag_ == False:
            false_.show()
        else:
            no_need.show()

    def onclick2(self):
        company_update.hide()
        company_info.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #各个页面
    MainWindow = QtWidgets.QMainWindow
    load = LoadWindow()  # 登录主界面
    f_load = Fail_Load()  # 登录失败
    student = Student()  # 学生页面
    company = Company()  # 公司页面
    company_info = Company_info()
    company_update = Company_update()
    interview = Interview()
    job_fair = Job_fair()
    school = School()
    statistic = Statistic()
    student_base_info = Student_base_info()
    student_base_update = Student_base_update()
    student_study_info = Student_study_info()
    student_study_update = Student_study_update()
    success = Success()
    no_need = No_need()
    false_ = False_()
    bottom = Bottom()
    job_fair_s = Job_fair_s()
    attention = Attention()
    fair_choose = Fair_choose()

    load.show()
    app.exec_()


