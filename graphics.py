# importations à faire pour la réalisation d'une interface graphique
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QColor
from PyQt5.QtCore import Qt

# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication


def appui_bouton1():
    print("TheForest")
    
def appui_bouton2():
    print("ThePrison")
    
def appui_bouton3():
    print("TheTunnel")
    
def appui_bouton4():
    print("PracticeFiel")

    
app = QApplication.instance() 
if not app: # sinon on crée une instance de QApplication
    app = QApplication(sys.argv)

class Button(QPushButton):
    def __init__(self, value):
        QPushButton.__init__(self)
        self.name = value
    def push_button():
        print()
    
class Fenetre(QWidget):
    def __init__(self, nom):
        QWidget.__init__(self)
        self.setWindowTitle(nom)

    def mousePressEvent(self, event):
        print("Chose a map")
    
    
fen = Fenetre("test")

# la fenêtre est rendue visible

gri = QGridLayout(fen)
pal = fen.palette()
pal.setColor(fen.backgroundRole(), Qt.white)
fen.setPalette(pal)

f = QFont("Helvetica", 100, QFont.Bold);
pal.setColor(QPalette.WindowText, QColor(20, 120, 120))
title = QLabel("Chose a Map")
title.setPalette(pal)
title.setFont(f)

button1 = Button( "TheForest")
button2 = Button( "PracticeFiels")
button3 = Button( "test")
button4 = Button( "test")

TheForest = QPixmap("/Users/sebastien/Documents/ENPC/2A/TDLog/Interface_graphique/images/TheForest.png");
ButtonIcon = QIcon(TheForest);
button1.setIcon(ButtonIcon);
button1.setIconSize(TheForest.rect().size());
button1.setFixedSize(TheForest.rect().size());
button1.clicked.connect(appui_bouton1)

ThePrison = QPixmap("/Users/sebastien/Documents/ENPC/2A/TDLog/Interface_graphique/images/ThePrison.png");
ButtonIcon = QIcon(ThePrison);
button2.setIcon(ButtonIcon);
button2.setIconSize(ThePrison.rect().size());
button2.setFixedSize(ThePrison.rect().size());
button2.clicked.connect(appui_bouton2)

TheTunnel = QPixmap("/Users/sebastien/Documents/ENPC/2A/TDLog/Interface_graphique/images/TheTunnel.png");
ButtonIcon = QIcon(TheTunnel);
button3.setIcon(ButtonIcon);
button3.setIconSize(TheTunnel.rect().size());
button3.setFixedSize(TheTunnel.rect().size());
button3.clicked.connect(appui_bouton3)

PracticeField = QPixmap("/Users/sebastien/Documents/ENPC/2A/TDLog/Interface_graphique/images/PracticeField.png");
ButtonIcon = QIcon(PracticeField);
button4.setIcon(ButtonIcon);
button4.setIconSize(PracticeField.rect().size());
button4.setFixedSize(PracticeField.rect().size());
button4.clicked.connect(appui_bouton4)

gri.addWidget(title, 1, 2)
gri.addWidget(button1, 3, 1)
gri.addWidget(button2, 3, 3)
gri.addWidget(button3, 4, 1)
gri.addWidget(button4, 4, 3)


fen.show()

app.exec_()

