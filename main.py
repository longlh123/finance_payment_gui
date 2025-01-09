import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from view.gui.frmMain import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        #Load the Ui
        self.setupUi(self) 

        #show the main window
        self.show()

if __name__ == "__main__":
    # Create the QApplication instance
    app = QApplication(sys.argv)

     # Create and show the main window
    main_window = MainWindow()

    # Execute the application
    sys.exit(app.exec())