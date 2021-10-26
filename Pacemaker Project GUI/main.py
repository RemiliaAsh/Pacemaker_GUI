from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import  QtWidgets
import serial
import struct
from Ui_welcome import Ui_MainWindow
from Ui_sign_up import Ui_Dialog
from Ui_log_in import log
from Ui_mode_select import Ui_mode
from Ui_AOO import Ui_AOO_mode
from Ui_VOO import Ui_VOO_mode
from Ui_VVI import Ui_VVI_mode
from Ui_AAI import Ui_AAI_mode
from Ui_DOO import Ui_DOO_mode
from Ui_DDD import Ui_DDD_mode
from Ui_AOOR import Ui_AOOR_mode
from Ui_AAIR import Ui_AAIR_mode
from Ui_VOOR import Ui_VOOR_mode
from Ui_VVIR import Ui_VVIR_mode
from Ui_DOOR import Ui_DOOR_mode
from Ui_DDDR import Ui_DDDR_mode

#GLOBAL VARIABLES
mode_number = 0          #used when selecting pacing mode
account_number = str(0)  #used when locating corresponding parameter file for a logged account


#PUBLIC FUNCTIONS

#open a txt file and return contain in it as array
#parameter "name" is the name of target txt file, can be modified to open data file or one of the parameter files
def read(name):
     file = open(name)
     information = file.readlines()
     file.close
     return information
#write parameters into the correspoinding parameter file
#"mode" is used to locate the right place that the parameter should go in the file. "account_number" is to locate the correct file for a logged user. "parameter" is the contain that will be put into the file
def write_parameter(mode,account_number,parameter):
     information = read(account_number+'parameter.txt')
     file = open(account_number+'parameter.txt','w')   
     if mode == 0:
          file.writelines(information[0])
          file.writelines(parameter)
          file.writelines(information[5:])
     elif mode == 1:
          file.writelines(information[:6])
          file.writelines(parameter)
          file.writelines(information[10:])
     elif mode == 2:
          file.writelines(information[:11])
          file.writelines(parameter)
          file.writelines(information[16:])
     elif mode == 3:
          file.writelines(information[:17])
          file.writelines(parameter)
          file.writelines(information[22:])
     elif mode == 4:
          file.writelines(information[:23])
          file.writelines(parameter)
          file.writelines(information[30:])
     elif mode == 5:
          file.writelines(information[:31])
          file.writelines(parameter)
          file.writelines(information[51:])
     elif mode == 6:
          file.writelines(information[:52])
          file.writelines(parameter)
          file.writelines(information[61:])
     elif mode == 7:
          file.writelines(information[:62])
          file.writelines(parameter)
          file.writelines(information[76:])
     elif mode == 8:
          file.writelines(information[:77])
          file.writelines(parameter)
          file.writelines(information[86:])
     elif mode == 9:
          file.writelines(information[:87])
          file.writelines(parameter)
          file.writelines(information[100:])
     elif mode == 10:
          file.writelines(information[:101])
          file.writelines(parameter)
          file.writelines(information[113:])
     elif mode == 11:
          file.writelines(information[:114])
          file.writelines(parameter)
          file.writelines(information[139:])
     file.close

#New functions for new parameters and modes in assignment 2, work the same as "write_parameter"
def write_parameter_correct(mode,account_number,parameter):
     information = read(account_number+'parameter.txt')
     file = open(account_number+'parameter.txt','w')   
     if mode == 2:
          file.writelines(information[:140])
          file.writelines(parameter)
          file.writelines(information[144:])
     elif mode == 3:
          file.writelines(information[:144])
          file.writelines(parameter)
          file.writelines(information[147:])

#the function tells if there are already 10 accounts signed up
def maximum_reached():
     information = read('data.txt')
     users_line = -1
     for i in information:
          users_line+=1
     if users_line >= 19: return 1
     else: return 0

#creating a new account, write the account and password into data file
#two parameters are informations that will be saved into data file
def creating_account(account, password):
     information = read('data.txt')
     data = open('data.txt','w')                                                                    
     data.writelines(information[:-1])
     data.writelines(account)
     data.writelines("\n")  
     data.writelines(password)
     data.writelines("\n")  
     data.writelines(information[-1])
     data.close

#match account and password with data file, returns 1 when both matched, 2 when none matched, and 0 when only the account matched
#parameters are account and password that need to be compared
def matching(account, password):
     information = read('data.txt')
     global account_number
     matching_position = -1
     index = 0
     for i in information:
          if i == account and index % 2 ==0 :matching_position = index
          index += 1
     if not matching_position == -1:
          if (information[matching_position+1]) == password:
               account_number = str(matching_position)
               return 1
          else:
               return 0
     else: return 2


#CLASSES
#the window that prompt for account and password for signing up
class Dialog(QDialog, Ui_Dialog):
    #constructor
    def __init__(self, parent=None): 
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    #function for the confirm button
    def on_pushButton_clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.close()
        if matching(username+"\n", password+"\n") ==2: 
            creating_account(username, password)
            my_button = QMessageBox.information(self, "Congrats", "New Account has been created")
        else:my_button = QMessageBox.information(self, "Warning", "Account already existed")
    
    @pyqtSlot()
    #back button 
    def on_pushButton_2_clicked(self):
        self.close()


#the main window with options to sign up or log in, the first window that will be open when excuted
class MainWindow(QMainWindow, Ui_MainWindow):
    #constructor
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    #sign up button
    def on_pushButton_clicked(self):
        if (not maximum_reached()):
            sign_up_ui = Dialog()
            sign_up_ui.exec_()
        else: my_button = QMessageBox.information(self, "Warning", "Account number has reached a maximum")                                                              
    
    @pyqtSlot()
    #log in button
    def on_pushButton_2_clicked(self):
        log_in_ui = log_in()
        log_in_ui.exec_()
        

#log in window, with options to confirm or go back to main window
class log_in(QDialog, log):
    #constructor
    def __init__(self, parent=None):
        super(log_in, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    #confirm button
    def on_pushButton_clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == "": 
            my_button = QMessageBox.information(self, "Warning", "Please enter your username") 
        elif password == "":
            my_button = QMessageBox.information(self, "Warning", "Please enter your password") 
        else:
            
            if matching(username+"\n", password+"\n") == 0: 
                my_button = QMessageBox.information(self, "Warning", "Wrong Password")  
            elif matching(username+"\n", password+"\n") == 1: 
                ui.close()
                self.close()
                mode_selecter = mode()
                mode_selecter.exec_()
            else: my_button = QMessageBox.information(self, "Warning", "Account does not exist")  
    
    @pyqtSlot()
    #back button
    def on_pushButton_2_clicked(self):
        self.close()

#the window to select pacing mode, with 4 options for now, and a confirm button        
class mode(QDialog, Ui_mode):
    #constructor
    def __init__(self, parent=None):
        super(mode, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    #excute when AOO mode is selected, changing global variable "mode_number" to 1
    def on_radioButton_clicked(self):
        global mode_number
        mode_number = 1
    
    @pyqtSlot()
    #excute when VOO mode is selected, changing global "mode_number" variable to 2
    def on_radioButton_3_clicked(self):
        global mode_number
        mode_number = 2
    
    @pyqtSlot()
    #excute when AAI mode is selected, changing global "mode_number" variable to 3
    def on_radioButton_4_clicked(self):
        global mode_number
        mode_number = 3
    
    @pyqtSlot()
    #excute when VVI mode is selected, changing global "mode_number" variable to 4
    def on_radioButton_2_clicked(self):
        global mode_number
        mode_number = 4

    @pyqtSlot()
    def on_radioButton_5_clicked(self):
        """
       Slot function of the DOO radio button
        """
        global mode_number
        mode_number = 5
    
    @pyqtSlot()
    def on_radioButton_6_clicked(self):
        """
        Slot function of the DDD radio button
        """
        global mode_number
        mode_number = 6
        
    
    @pyqtSlot()
    def on_radioButton_7_clicked(self):
        """
        Slot function of the AOOR radio button
        """
        global mode_number
        mode_number = 7
    
    @pyqtSlot()
    def on_radioButton_8_clicked(self):
        """
        Slot function of the AAIR radio button
        """
        global mode_number
        mode_number = 8
    
    @pyqtSlot()
    def on_radioButton_9_clicked(self):
        """
        Slot funtion of the VOOR radio button
        """
        global mode_number
        mode_number = 9
    
    @pyqtSlot()
    def on_radioButton_10_clicked(self):
        """
        Slot function of the VVIR radio button
        """
        global mode_number
        mode_number = 10
    
    @pyqtSlot()
    def on_radioButton_11_clicked(self):
        """
        Slot function of the DOOR radio button
        """
        global mode_number
        mode_number = 11
    
    @pyqtSlot()
    def on_radioButton_12_clicked(self):
        """
        Slot function of the DDDR radio button
        """
        global mode_number
        mode_number = 12


        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        #reading parameters, opening windows and showing parameter on windows according to mode selected
        if (mode_number == 1) :
            LRL = read(account_number+'parameter.txt')[1]
            URL = read(account_number+'parameter.txt')[2]
            AA = read(account_number+'parameter.txt')[3]
            APW = read(account_number+'parameter.txt')[4]
            AOO = AOO_mode()
            AOO.comboBox_5.setItemText(0, LRL.strip())
            AOO.comboBox_4.setItemText(0, URL.strip())
            AOO.comboBox_3.setItemText(0, AA.strip())
            AOO.comboBox_2.setItemText(0,APW.strip())
            self.close()
            AOO.exec_()
        elif (mode_number == 2) :
            LRL = read(account_number+'parameter.txt')[6]
            URL = read(account_number+'parameter.txt')[7]
            VA = read(account_number+'parameter.txt')[8]
            VPW = read(account_number+'parameter.txt')[9]
            VOO = VOO_mode()
            VOO.comboBox_5.setItemText(0, LRL.strip())
            VOO.comboBox_4.setItemText(0, URL.strip())
            VOO.comboBox_3.setItemText(0, VA.strip())
            VOO.comboBox_2.setItemText(0,VPW.strip())
            self.close()
            VOO.exec_()
        elif (mode_number == 3) :
            LRL = read(account_number+'parameter.txt')[11]
            URL = read(account_number+'parameter.txt')[12]
            AA = read(account_number+'parameter.txt')[13]
            APW = read(account_number+'parameter.txt')[14]
            ARP = read(account_number+'parameter.txt')[15]
            AS = read(account_number+'parameter.txt')[140]
            PVARP = read(account_number+'parameter.txt')[141]
            HYS = read(account_number+'parameter.txt')[142]
            RS = read(account_number+'parameter.txt')[143]
            AAI = AAI_mode()
            AAI.comboBox_5.setItemText(0, LRL.strip())
            AAI.comboBox_4.setItemText(0, URL.strip())
            AAI.comboBox_3.setItemText(0, AA.strip())
            AAI.comboBox_2.setItemText(0,APW.strip())
            AAI.comboBox.setItemText(0,ARP.strip())
            AAI.comboBox_10.setItemText(0, AS.strip())
            AAI.comboBox_14.setItemText(0, PVARP.strip())
            AAI.comboBox_83.setItemText(0, HYS.strip())
            AAI.comboBox_84.setItemText(0, RS.strip())
            self.close()
            AAI.exec_()
        elif (mode_number == 4) :
            LRL = read(account_number+'parameter.txt')[17]
            URL = read(account_number+'parameter.txt')[18]
            VA = read(account_number+'parameter.txt')[19]
            VPW = read(account_number+'parameter.txt')[20]
            VRP = read(account_number+'parameter.txt')[21]
            VS = read(account_number+'parameter.txt')[144]
            HYS = read(account_number+'parameter.txt')[145]
            RS = read(account_number+'parameter.txt')[146]
            VVI = VVI_mode()
            VVI.comboBox_5.setItemText(0, LRL.strip())
            VVI.comboBox_4.setItemText(0, URL.strip())
            VVI.comboBox_3.setItemText(0, VA.strip())
            VVI.comboBox_2.setItemText(0,VPW.strip())
            VVI.comboBox.setItemText(0,VRP.strip())
            VVI.comboBox_11.setItemText(0, VS.strip())
            VVI.comboBox_17.setItemText(0,HYS.strip())
            VVI.comboBox_16.setItemText(0,RS.strip())
            self.close()
            VVI.exec_()
        elif (mode_number == 5) :
            LRL = read(account_number+'parameter.txt')[23]
            URL = read(account_number+'parameter.txt')[24]
            FAVDelay = read(account_number+'parameter.txt')[25]
            AA = read(account_number+'parameter.txt')[26]
            VA = read(account_number+'parameter.txt')[27]
            APW = read(account_number+'parameter.txt')[28]
            VPW = read(account_number+'parameter.txt')[29]
            DOO = DOO_mode()
            DOO.comboBox_5.setItemText(0, LRL.strip())
            DOO.comboBox_4.setItemText(0, URL.strip())
            DOO.comboBox_3.setItemText(0, FAVDelay.strip())
            DOO.comboBox_6.setItemText(0,AA.strip())
            DOO.comboBox_8.setItemText(0,VA.strip())
            DOO.comboBox_7.setItemText(0,APW.strip())
            DOO.comboBox_2.setItemText(0,VPW.strip())
            self.close()
            DOO.exec_()
        elif (mode_number == 6) :
            LRL = read(account_number+'parameter.txt')[31]
            URL = read(account_number+'parameter.txt')[32]
            FAVDelay = read(account_number+'parameter.txt')[33]
            DAD = read(account_number+'parameter.txt')[34]
            SAVOFF = read(account_number+'parameter.txt')[35]
            AA = read(account_number+'parameter.txt')[36]
            VA = read(account_number+'parameter.txt')[37]
            APW = read(account_number+'parameter.txt')[38]
            VPW = read(account_number+'parameter.txt')[39]
            AS = read(account_number+'parameter.txt')[40]
            VS = read(account_number+'parameter.txt')[41]
            VRP = read(account_number+'parameter.txt')[42]
            ARP = read(account_number+'parameter.txt')[43]
            PVARP = read(account_number+'parameter.txt')[44]
            PVARPEX = read(account_number+'parameter.txt')[45]
            HYS = read(account_number+'parameter.txt')[46]
            RS = read(account_number+'parameter.txt')[47]
            ATRD = read(account_number+'parameter.txt')[48]
            ATRM = read(account_number+'parameter.txt')[49]
            ATRT = read(account_number+'parameter.txt')[50]
            DDD = DDD_mode()
            DDD.comboBox_5.setItemText(0, LRL.strip())
            DDD.comboBox_4.setItemText(0, URL.strip())
            DDD.comboBox_3.setItemText(0, FAVDelay.strip())
            DDD.comboBox.setItemText(0,DAD.strip())
            DDD.comboBox_9.setItemText(0,SAVOFF.strip())
            DDD.comboBox_6.setItemText(0,AA.strip())
            DDD.comboBox_8.setItemText(0,VA.strip())
            DDD.comboBox_7.setItemText(0, APW.strip())
            DDD.comboBox_2.setItemText(0, VPW.strip())
            DDD.comboBox_10.setItemText(0, AS.strip())
            DDD.comboBox_11.setItemText(0,VS.strip())
            DDD.comboBox_12.setItemText(0,VRP.strip())
            DDD.comboBox_13.setItemText(0,ARP.strip())
            DDD.comboBox_14.setItemText(0,PVARP.strip())
            DDD.comboBox_15.setItemText(0, PVARPEX.strip())
            DDD.comboBox_17.setItemText(0, HYS.strip())
            DDD.comboBox_16.setItemText(0, RS.strip())
            DDD.comboBox_18.setItemText(0,ATRD.strip())
            DDD.comboBox_19.setItemText(0,ATRM.strip())
            DDD.comboBox_20.setItemText(0,ATRT.strip())
            self.close()
            DDD.exec_()
        elif (mode_number == 7) :
            LRL = read(account_number+'parameter.txt')[52]
            URL = read(account_number+'parameter.txt')[53]
            MSR = read(account_number+'parameter.txt')[54]
            AA = read(account_number+'parameter.txt')[55]
            APW = read(account_number+'parameter.txt')[56]
            AT = read(account_number+'parameter.txt')[57]
            RT = read(account_number+'parameter.txt')[58]
            RF = read(account_number+'parameter.txt')[59]
            RecTime = read(account_number+'parameter.txt')[60]
            AOOR = AOOR_mode()
            AOOR.comboBox_5.setItemText(0, LRL.strip())
            AOOR.comboBox_4.setItemText(0, URL.strip())
            AOOR.comboBox_23.setItemText(0, MSR.strip())
            AOOR.comboBox_25.setItemText(0,AA.strip())
            AOOR.comboBox_24.setItemText(0,APW.strip())
            AOOR.comboBox_26.setItemText(0,AT.strip())
            AOOR.comboBox_27.setItemText(0,RT.strip())
            AOOR.comboBox_28.setItemText(0, RF.strip())
            AOOR.comboBox_29.setItemText(0, RecTime.strip())
            self.close()
            AOOR.exec_()
        elif (mode_number == 8) :
            LRL = read(account_number+'parameter.txt')[62]
            URL = read(account_number+'parameter.txt')[63]
            MSR = read(account_number+'parameter.txt')[64]
            AA = read(account_number+'parameter.txt')[65]
            APW = read(account_number+'parameter.txt')[66]
            AS = read(account_number+'parameter.txt')[67]
            ARP = read(account_number+'parameter.txt')[68]
            PVARP = read(account_number+'parameter.txt')[69]
            HYS = read(account_number+'parameter.txt')[70]
            RS = read(account_number+'parameter.txt')[71]
            AT = read(account_number+'parameter.txt')[72]
            RT = read(account_number+'parameter.txt')[73]
            RF = read(account_number+'parameter.txt')[74]
            RecTime = read(account_number+'parameter.txt')[75]
            AAIR = AAIR_mode()
            AAIR.comboBox_5.setItemText(0, LRL.strip())
            AAIR.comboBox_4.setItemText(0, URL.strip())
            AAIR.comboBox_23.setItemText(0, MSR.strip())
            AAIR.comboBox_25.setItemText(0,AA.strip())
            AAIR.comboBox_24.setItemText(0,APW.strip())
            AAIR.comboBox_10.setItemText(0,AS.strip())
            AAIR.comboBox_13.setItemText(0,ARP.strip())
            AAIR.comboBox_14.setItemText(0, PVARP.strip())
            AAIR.comboBox_17.setItemText(0, HYS.strip())
            AAIR.comboBox_16.setItemText(0,RS.strip())
            AAIR.comboBox_26.setItemText(0,AT.strip())
            AAIR.comboBox_27.setItemText(0, RT.strip())
            AAIR.comboBox_28.setItemText(0, RF.strip())
            AAIR.comboBox_29.setItemText(0, RecTime.strip())
            self.close()
            AAIR.exec_()
        elif (mode_number == 9) :
            LRL = read(account_number+'parameter.txt')[77]
            URL = read(account_number+'parameter.txt')[78]
            MSR = read(account_number+'parameter.txt')[79]
            VA = read(account_number+'parameter.txt')[80]
            VPW = read(account_number+'parameter.txt')[81]
            AT = read(account_number+'parameter.txt')[82]
            RT = read(account_number+'parameter.txt')[83]
            RF = read(account_number+'parameter.txt')[84]
            RecTime = read(account_number+'parameter.txt')[85]
            VOOR = VOOR_mode()
            VOOR.comboBox_5.setItemText(0, LRL.strip())
            VOOR.comboBox_4.setItemText(0, URL.strip())
            VOOR.comboBox_23.setItemText(0, MSR.strip())
            VOOR.comboBox_8.setItemText(0,VA.strip())
            VOOR.comboBox_2.setItemText(0,VPW.strip())
            VOOR.comboBox_26.setItemText(0,AT.strip())
            VOOR.comboBox_27.setItemText(0,RT.strip())
            VOOR.comboBox_28.setItemText(0, RF.strip())
            VOOR.comboBox_29.setItemText(0, RecTime.strip())
            self.close()
            VOOR.exec_()
        elif (mode_number == 10) :
            LRL = read(account_number+'parameter.txt')[87]
            URL = read(account_number+'parameter.txt')[88]
            MSR = read(account_number+'parameter.txt')[89]
            VA = read(account_number+'parameter.txt')[90]
            VPW = read(account_number+'parameter.txt')[91]
            VS = read(account_number+'parameter.txt')[92]
            VRP = read(account_number+'parameter.txt')[93]
            HYS = read(account_number+'parameter.txt')[94]
            RS = read(account_number+'parameter.txt')[95]
            AT = read(account_number+'parameter.txt')[96]
            RT = read(account_number+'parameter.txt')[97]
            RF = read(account_number+'parameter.txt')[98]
            RecTime = read(account_number+'parameter.txt')[99]
            VVIR = VVIR_mode()
            VVIR.comboBox_5.setItemText(0, LRL.strip())
            VVIR.comboBox_4.setItemText(0, URL.strip())
            VVIR.comboBox_23.setItemText(0, MSR.strip())
            VVIR.comboBox_8.setItemText(0,VA.strip())
            VVIR.comboBox_2.setItemText(0,VPW.strip())
            VVIR.comboBox_11.setItemText(0,VS.strip())
            VVIR.comboBox_12.setItemText(0,VRP.strip())
            VVIR.comboBox_17.setItemText(0, HYS.strip())
            VVIR.comboBox_16.setItemText(0, RS.strip())
            VVIR.comboBox_26.setItemText(0, AT.strip())
            VVIR.comboBox_27.setItemText(0, RT.strip())
            VVIR.comboBox_28.setItemText(0, RF.strip())
            VVIR.comboBox_29.setItemText(0,RecTime.strip())
            self.close()
            VVIR.exec_()
        elif (mode_number == 11) :
            LRL = read(account_number+'parameter.txt')[101]
            URL = read(account_number+'parameter.txt')[102]
            MSR = read(account_number+'parameter.txt')[103]
            FAVDelay = read(account_number+'parameter.txt')[104]
            AA = read(account_number+'parameter.txt')[105]
            VA = read(account_number+'parameter.txt')[106]
            APW = read(account_number+'parameter.txt')[107]
            VPW = read(account_number+'parameter.txt')[108]
            AT = read(account_number+'parameter.txt')[109]
            RT = read(account_number+'parameter.txt')[110]
            RF = read(account_number+'parameter.txt')[111]
            RecTime = read(account_number+'parameter.txt')[112]
            DOOR = DOOR_mode()
            DOOR.comboBox_5.setItemText(0, LRL.strip())
            DOOR.comboBox_4.setItemText(0, URL.strip())
            DOOR.comboBox_23.setItemText(0, MSR.strip())
            DOOR.comboBox_3.setItemText(0,FAVDelay.strip())
            DOOR.comboBox_6.setItemText(0,AA.strip())
            DOOR.comboBox_8.setItemText(0,VA.strip())
            DOOR.comboBox_7.setItemText(0,APW.strip())
            DOOR.comboBox_2.setItemText(0, VPW.strip())
            DOOR.comboBox_26.setItemText(0, AT.strip())
            DOOR.comboBox_27.setItemText(0, RT.strip())
            DOOR.comboBox_28.setItemText(0, RF.strip())
            DOOR.comboBox_29.setItemText(0, RecTime.strip())
            self.close()
            DOOR.exec_()
        elif (mode_number == 12) :
            LRL = read(account_number+'parameter.txt')[114]
            URL = read(account_number+'parameter.txt')[115]
            MSR = read(account_number+'parameter.txt')[116]
            FAVDelay = read(account_number+'parameter.txt')[117]
            DAD = read(account_number+'parameter.txt')[118]
            SAVOFF = read(account_number+'parameter.txt')[119]
            AA = read(account_number+'parameter.txt')[120]
            VA = read(account_number+'parameter.txt')[121]
            APW = read(account_number+'parameter.txt')[122]
            VPW = read(account_number+'parameter.txt')[123]
            AS = read(account_number+'parameter.txt')[124]
            VS = read(account_number+'parameter.txt')[125]
            VRP = read(account_number+'parameter.txt')[126]
            ARP = read(account_number+'parameter.txt')[127]
            PVARP = read(account_number+'parameter.txt')[128]
            PVARPEX = read(account_number+'parameter.txt')[129]
            HYS = read(account_number+'parameter.txt')[130]
            RS = read(account_number+'parameter.txt')[131]
            ATRD = read(account_number+'parameter.txt')[132]
            ATRM = read(account_number+'parameter.txt')[133]
            ATRT = read(account_number+'parameter.txt')[134]
            AT = read(account_number+'parameter.txt')[135]
            RT = read(account_number+'parameter.txt')[136]
            RF = read(account_number+'parameter.txt')[137]
            RecTime = read(account_number+'parameter.txt')[138]
            DDDR = DDDR_mode()
            DDDR.comboBox_5.setItemText(0, LRL.strip())
            DDDR.comboBox_4.setItemText(0, URL.strip())
            DDDR.comboBox_23.setItemText(0, MSR.strip())
            DDDR.comboBox_3.setItemText(0,FAVDelay.strip())
            DDDR.comboBox.setItemText(0,DAD.strip())
            DDDR.comboBox_9.setItemText(0,SAVOFF.strip())
            DDDR.comboBox_6.setItemText(0,AA.strip())
            DDDR.comboBox_8.setItemText(0, VA.strip())
            DDDR.comboBox_7.setItemText(0, APW.strip())
            DDDR.comboBox_2.setItemText(0, VPW.strip())
            DDDR.comboBox_10.setItemText(0,AS.strip())
            DDDR.comboBox_11.setItemText(0,VS.strip())
            DDDR.comboBox_12.setItemText(0,VRP.strip())
            DDDR.comboBox_13.setItemText(0,ARP.strip())
            DDDR.comboBox_14.setItemText(0, PVARP.strip())
            DDDR.comboBox_15.setItemText(0, PVARPEX.strip())
            DDDR.comboBox_17.setItemText(0, HYS.strip())
            DDDR.comboBox_16.setItemText(0,RS.strip())
            DDDR.comboBox_18.setItemText(0,ATRD.strip())
            DDDR.comboBox_19.setItemText(0,ATRM.strip())
            DDDR.comboBox_20.setItemText(0, ATRT.strip())
            DDDR.comboBox_26.setItemText(0, AT.strip())
            DDDR.comboBox_27.setItemText(0,RT.strip())
            DDDR.comboBox_28.setItemText(0,RF.strip())
            DDDR.comboBox_29.setItemText(0,RecTime.strip())
            self.close()
            DDDR.exec_()


#the AOO window that can change parameters
class AOO_mode(QDialog, Ui_AOO_mode):
    #constructor
    def __init__(self, parent=None):
        super(AOO_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        #confirm button
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        AA = self.comboBox_3.currentText()
        APW = self.comboBox_2.currentText()
        try: #open a serial port
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:#saving and transmiting parameters
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+AA+"\n"+APW+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),0,0,0,0,float(AA),0,float(APW),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                  ser.write(code)
                  ser.close()
              
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        #back button
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()
        
#the VOO window that can change parameters
class VOO_mode(QDialog, Ui_VOO_mode):
    #Constructor
    def __init__(self, parent=None):
        super(VOO_mode, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    #confirm button
    def on_pushButton_clicked(self):
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        VA = self.comboBox_3.currentText()
        VPW = self.comboBox_2.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+VA+"\n"+VPW+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),0,0,0,0,0,float(VA),0,float(VPW),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                  ser.write(code)
                  ser.close()
        
    @pyqtSlot()
    #back button
    def on_pushButton_2_clicked(self):
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()

#the AAI window that can change parameters
class AAI_mode(QDialog, Ui_AAI_mode):
    #Constructor
    def __init__(self, parent=None):
        super(AAI_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    #confirm button
    def on_pushButton_clicked(self):
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        AA = self.comboBox_3.currentText()
        APW = self.comboBox_2.currentText()
        ARP = self.comboBox.currentText()
        AS = self.comboBox_10.currentText()
        PVARP = self.comboBox_14.currentText()
        HYS = self.comboBox_83.currentText()
        RS = self.comboBox_84.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+AA+"\n"+APW+"\n"+ARP+"\n"))
                  write_parameter_correct(2,account_number,(AS+"\n"+PVARP+"\n"+HYS+"\n"+RS+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if HYS == 'OFF': HYS = '0'
                  if RS == 'OFF':RS = '0'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),0,0,0,0,float(AA),0,float(APW),0,float(AS),0,0,int(ARP),int(PVARP),0,int(HYS),float(RS),0,0,0,0,0,0,0)
                  ser.write(code)
                  ser.close()
    
    @pyqtSlot()
    #back button
    def on_pushButton_2_clicked(self):
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()

#the VVI window that can change parameters
class VVI_mode(QDialog, Ui_VVI_mode):
    #Constructor
    def __init__(self, parent=None):
        super(VVI_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    #confirm button
    def on_pushButton_clicked(self):
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        VA = self.comboBox_3.currentText()
        VPW = self.comboBox_2.currentText()
        VRP = self.comboBox.currentText()
        VS = self.comboBox_11.currentText()
        HYS = self.comboBox_17.currentText()
        RS = self.comboBox_16.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+VA+"\n"+VPW+"\n"+VRP+"\n"))
                  write_parameter_correct(3,account_number,(VS+"\n"+HYS+"\n"+RS+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if HYS == 'OFF': HYS = '0'
                  if RS == 'OFF':RS = '0'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),0,0,0,0,0,float(VA),0,float(VPW),0,float(VS),int(VRP),0,0,0,int(HYS),float(RS),0,0,0,0,0,0,0)
                  ser.write(code)
                  ser.close()
    
    @pyqtSlot()
    #back button
    def on_pushButton_2_clicked(self):
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()

class DOO_mode(QDialog, Ui_DOO_mode):
    """
    DOO MODE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(DOO_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the DOO window
        """
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        FAVDelay = self.comboBox_3.currentText()
        AA = self.comboBox_6.currentText()
        VA = self.comboBox_8.currentText()
        APW = self.comboBox_7.currentText()
        VPW = self.comboBox_2.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+FAVDelay+"\n"+AA+"\n"+VA+"\n"+APW+"\n"+VPW+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),0,int(FAVDelay),0,0,float(AA),float(VA),float(APW),float(VPW),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                  ser.write(code)
                  ser.close()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the DOO window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()

class DDD_mode(QDialog, Ui_DDD_mode):
    """
    DDD MODE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(DDD_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the DDD window
        """
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        FAVDelay = self.comboBox_3.currentText()
        DAD = self.comboBox.currentText()
        SAVOFF = self.comboBox_9.currentText()
        AA = self.comboBox_6.currentText()
        VA = self.comboBox_8.currentText()
        APW = self.comboBox_7.currentText()
        VPW = self.comboBox_2.currentText()
        AS = self.comboBox_10.currentText()
        VS = self.comboBox_11.currentText()
        VRP = self.comboBox_12.currentText()
        ARP = self.comboBox_13.currentText()
        PVARP = self.comboBox_14.currentText()
        PVARPEX = self.comboBox_15.currentText()
        HYS = self.comboBox_17.currentText()
        RS = self.comboBox_16.currentText()
        ATRD = self.comboBox_18.currentText()
        ATRM = self.comboBox_19.currentText()
        ATRT = self.comboBox_20.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+FAVDelay+"\n"+DAD+"\n"+SAVOFF+"\n"+AA+"\n"+VA+"\n"+APW+"\n"+VPW+"\n"+AS+"\n"+VS+"\n"+VRP+"\n"+ARP+"\n"+PVARP+"\n"+PVARPEX+"\n"+HYS+"\n"+RS+"\n"+ATRD+"\n"+ATRM+"\n"+ATRT+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if DAD == 'OFF': DAD = ''
                  if ATRM == 'OFF': ATRM = ''
                  if PVARPEX == 'OFF':PVARPEX='0'
                  if HYS == 'OFF': HYS = '0'
                  if RS == 'OFF':RS = '0'
                  if SAVOFF == 'OFF': SAVOFF = '0'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),0,int(FAVDelay),DAD,int(SAVOFF),float(AA),float(VA),float(APW),float(VPW),float(AS),float(VS),int(VRP),int(ARP),int(PVARP),int(PVARPEX),int(HYS),float(RS),int(ATRD),ATRM,int(ATRT),0,0,0,0)
                  ser.write(code)
                  ser.close()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the DDD window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()
        
class AOOR_mode(QDialog, Ui_AOOR_mode):
    """
    AOOR MDOE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(AOOR_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the AOOR window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the AOOR window
        """
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        MSR = self.comboBox_23.currentText()
        AA = self.comboBox_25.currentText()
        APW = self.comboBox_24.currentText()
        AT = self.comboBox_26.currentText()
        RT = self.comboBox_27.currentText()
        RF = self.comboBox_28.currentText()
        RecTime = self.comboBox_29.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+MSR+"\n"+AA+"\n"+APW+"\n"+AT+"\n"+RT+"\n"+RF+"\n"+RecTime+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if AT == 'V-LOW': AT = '0'
                  elif AT == 'LOW': AT = '1'
                  elif AT == 'MED-LOW': AT = '2'
                  elif AT == 'MED': AT = '3'
                  elif AT == 'MED-HIGH': AT = '4'
                  elif AT == 'HIGH': AT = '5'
                  else : AT = '6'
                  print(mode_number)
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),int(MSR),0,0,0,float(AA),0,float(APW),0,0,0,0,0,0,0,0,0,0,0,0,int(AT),int(RT),int(RF),int(RecTime))

                  ser.write(code)
                  ser.close()
        
class AAIR_mode(QDialog, Ui_AAIR_mode):
    """
    AAIR MODE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(AAIR_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the AAIR window
        """
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        MSR = self.comboBox_23.currentText()
        AA = self.comboBox_25.currentText()
        APW = self.comboBox_24.currentText()
        AS = self.comboBox_10.currentText()
        ARP = self.comboBox_13.currentText()
        PVARP = self.comboBox_14.currentText()
        HYS = self.comboBox_17.currentText()
        RS = self.comboBox_16.currentText()
        AT = self.comboBox_26.currentText()
        RT = self.comboBox_27.currentText()
        RF = self.comboBox_28.currentText()
        RecTime = self.comboBox_29.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+MSR+"\n"+AA+"\n"+APW+"\n"+AS+"\n"+ARP+"\n"+PVARP+"\n"+HYS+"\n"+RS+"\n"+AT+"\n"+RT+"\n"+RF+"\n"+RecTime+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if AT == 'V-LOW': AT = '0'
                  elif AT == 'LOW': AT = '1'
                  elif AT == 'MED-LOW': AT = '2'
                  elif AT == 'MED': AT = '3'
                  elif AT == 'MED-HIGH': AT = '4'
                  elif AT == 'HIGH': AT = '5'
                  else : AT = '6'
                  if HYS == 'OFF': HYS = '0'
                  if RS == 'OFF':RS = '0'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),int(MSR),0,0,0,float(AA),0,float(APW),0,float(AS),0,0,int(ARP),int(PVARP),0,int(HYS),float(RS),0,0,0,int(AT),int(RT),int(RF),int(RecTime))
                  ser.write(code)
                  ser.close()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the AAIR window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()


class VOOR_mode(QDialog, Ui_VOOR_mode):
    """
    VOOR MODE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(VOOR_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the VOOR window
        """
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        MSR = self.comboBox_23.currentText()
        VA = self.comboBox_8.currentText()
        VPW = self.comboBox_2.currentText()
        AT = self.comboBox_26.currentText()
        RT = self.comboBox_27.currentText()
        RF = self.comboBox_28.currentText()
        RecTime = self.comboBox_29.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+MSR+"\n"+VA+"\n"+VPW+"\n"+AT+"\n"+RT+"\n"+RF+"\n"+RecTime+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if AT == 'V-LOW': AT = '0'
                  elif AT == 'LOW': AT = '1'
                  elif AT == 'MED-LOW': AT = '2'
                  elif AT == 'MED': AT = '3'
                  elif AT == 'MED-HIGH': AT = '4'
                  elif AT == 'HIGH': AT = '5'
                  else : AT = '6'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),int(MSR),0,0,0,0,float(VA),0,float(VPW),0,0,0,0,0,0,0,0,0,0,0,int(AT),int(RT),int(RF),int(RecTime))
                  ser.write(code)
                  ser.close()
        
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the VOOR window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()
        
class VVIR_mode(QDialog, Ui_VVIR_mode):
    """
    VVIR MODE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(VVIR_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the VVIR window
        """
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        MSR = self.comboBox_23.currentText()
        VA = self.comboBox_8.currentText()
        VPW = self.comboBox_2.currentText()
        VS = self.comboBox_11.currentText()
        VRP = self.comboBox_12.currentText()
        HYS = self.comboBox_17.currentText()
        RS = self.comboBox_16.currentText()
        AT = self.comboBox_26.currentText()
        RT = self.comboBox_27.currentText()
        RF = self.comboBox_28.currentText()
        RecTime = self.comboBox_29.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+MSR+"\n"+VA+"\n"+VPW+"\n"+VS+"\n"+VRP+"\n"+HYS+"\n"+RS+"\n"+AT+"\n"+RT+"\n"+RF+"\n"+RecTime+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if AT == 'V-LOW': AT = '0'
                  elif AT == 'LOW': AT = '1'
                  elif AT == 'MED-LOW': AT = '2'
                  elif AT == 'MED': AT = '3'
                  elif AT == 'MED-HIGH': AT = '4'
                  elif AT == 'HIGH': AT = '5'
                  else : AT = '6'
                  if HYS == 'OFF': HYS = '0'
                  if RS == 'OFF':RS = '0'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),int(MSR),0,0,0,0,float(VA),0,float(VPW),0,float(VS),int(VRP),0,0,0,int(HYS),float(RS),0,0,0,int(AT),int(RT),int(RF),int(RecTime))
                  ser.write(code)
                  ser.close()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the VVIR window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()

class DOOR_mode(QDialog, Ui_DOOR_mode):
    """
    DOOR MODE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(DOOR_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the DOOR window
        """
        LRL = int(self.comboBox_5.currentText())
        URL = int(self.comboBox_4.currentText())
        MSR = self.comboBox_23.currentText()
        FAVDelay = self.comboBox_3.currentText()
        AA = self.comboBox_6.currentText()
        VA = self.comboBox_8.currentText()
        APW = self.comboBox_7.currentText()
        VPW = self.comboBox_2.currentText()
        AT = self.comboBox_26.currentText()
        RT = self.comboBox_27.currentText()
        RF = self.comboBox_28.currentText()
        RecTime = self.comboBox_29.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  LRL = str(LRL)
                  URL = str(URL)
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+MSR+"\n"+FAVDelay+"\n"+AA+"\n"+VA+"\n"+APW+"\n"+VPW+"\n"+AT+"\n"+RT+"\n"+RF+"\n"+RecTime+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if AT == 'V-LOW': AT = '0'
                  elif AT == 'LOW': AT = '1'
                  elif AT == 'MED-LOW': AT = '2'
                  elif AT == 'MED': AT = '3'
                  elif AT == 'MED-HIGH': AT = '4'
                  elif AT == 'HIGH': AT = '5'
                  else : AT = '6'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),int(MSR),int(FAVDelay),0,0,float(AA),float(VA),float(APW),float(VPW),0,0,0,0,0,0,0,0,0,0,0,int(AT),int(RT),int(RF),int(RecTime))
                  ser.write(code)
                  ser.close()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the DOOR window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()
        
class DDDR_mode(QDialog, Ui_DDDR_mode):
    """
    DDDR MODE WINDOW
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(DDDR_mode, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        slot function of the confirm button of the DDDR window
        """
        LRL = self.comboBox_5.currentText()
        URL = self.comboBox_4.currentText()
        MSR = self.comboBox_23.currentText()
        FAVDelay = self.comboBox_3.currentText()
        DAD = self.comboBox.currentText()
        SAVOFF = self.comboBox_9.currentText()
        AA = self.comboBox_6.currentText()
        VA = self.comboBox_8.currentText()
        APW = self.comboBox_7.currentText()
        VPW = self.comboBox_2.currentText()
        AS = self.comboBox_10.currentText()
        VS = self.comboBox_11.currentText()
        VRP = self.comboBox_12.currentText()
        ARP = self.comboBox_13.currentText()
        PVARP = self.comboBox_14.currentText()
        PVARPEX = self.comboBox_15.currentText()
        HYS = self.comboBox_17.currentText()
        RS = self.comboBox_16.currentText()
        ATRD = self.comboBox_18.currentText()
        ATRM = self.comboBox_19.currentText()
        ATRT = self.comboBox_20.currentText()
        AT = self.comboBox_26.currentText()
        RT = self.comboBox_27.currentText()
        RF = self.comboBox_28.currentText()
        RecTime = self.comboBox_29.currentText()
        try:
             ser = serial.Serial("/dev/tty.usbmodem0000001234561", 115200)
        except BaseException:
             my_button = QMessageBox.information(self, "Notification", "Device not connected")
        else:
             if LRL>URL:
                  my_button = QMessageBox.information(self, "Notification", "Invalid value")
             else:
                  write_parameter(mode_number-1,account_number,(LRL+"\n"+URL+"\n"+MSR+"\n"+FAVDelay+"\n"+DAD+"\n"+SAVOFF+"\n"+AA+"\n"+VA+"\n"+APW+"\n"+VPW+"\n"+AS+"\n"+VS+"\n"+VRP+"\n"+ARP+"\n"+PVARP+"\n"+PVARPEX+"\n"+HYS+"\n"+RS+"\n"+ATRD+"\n"+ATRM+"\n"+ATRT+"\n"+AT+"\n"+RT+"\n"+RF+"\n"+RecTime+"\n"))
                  my_button = QMessageBox.information(self, "Notification", "Your change has been saved")
                  if DAD == 'OFF': DAD = ''
                  if ATRM == 'OFF': ATRM = ''
                  if AT == 'V-LOW': AT = '0'
                  elif AT == 'LOW': AT = '1'
                  elif AT == 'MED-LOW': AT = '2'
                  elif AT == 'MED': AT = '3'
                  elif AT == 'MED-HIGH': AT = '4'
                  elif AT == 'HIGH': AT = '5'
                  else : AT = '6'
                  if PVARPEX == 'OFF':PVARPEX='0'
                  if HYS == 'OFF': HYS = '0'
                  if RS == 'OFF':RS = '0'
                  if SAVOFF == 'OFF': SAVOFF = '0'
                  code = struct.pack('?hhhhh?hffffffhhhhhfh?hhhhh',1,mode_number,int(LRL),int(URL),int(MSR),int(FAVDelay),DAD,int(SAVOFF),float(AA),float(VA),float(APW),float(VPW),float(AS),float(VS),int(VRP),int(ARP),int(PVARP),int(PVARPEX),int(HYS),float(RS),int(ATRD),ATRM,int(ATRT),int(AT),int(RT),int(RF),int(RecTime))
                  ser.write(code)
                  ser.close()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        slot function of the back button of the DDDR window
        """
        self.close()
        mode_selecter = mode()
        mode_selecter.exec_()


#main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()  #opening the main window, the first window
    sys.exit(app.exec_())

