import os
import sys
from PyQt6.QtCore import Qt, QTimer, QEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QGuiApplication, QIcon
from multiplication_input_view import MultiplicationInputView
from division_input_view import DivisionInputView

## PyInstaller file path handler
if getattr(sys, 'frozen', False):
    # Running as a PyInstaller executable
    base_path = sys._MEIPASS
else:
    # Running as a script
    base_path = os.path.abspath(".")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.multiplication_input_view = None
        self.division_input_view = None
        
        ## User screen's dimenions
        self.screen = QGuiApplication.primaryScreen()
        self.screen_size = self.screen.availableSize()

        self.setWindowTitle("Simulador de Multiplicacao e Divisao Sem Sinal em Binario")
        self.setWindowIcon(QIcon(os.path.join(base_path, 'resources', 'logo-unespar.jpg')))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        # Application Header
        title_label = QLabel("<h1>Simulador de Multiplicacao e Divisao Sem Sinal em Binario</h1>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Stacked layout
        self.stacked_layout = QStackedLayout()
        
        # First stacked view: Welcome screen
        self.welcome_layout = QVBoxLayout()
        self.welcome_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.choices_layout_label = QLabel("<h2>Bem vindo, escolha a operacao a ser realizada</h2>")
        self.choices_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_layout.addWidget(self.choices_layout_label)
        
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.button_multiplication_input = (QPushButton("Multiplicacao"))
        self.button_multiplication_input.clicked.connect(self.show_multiplication_input_view)
        self.button_division_input = (QPushButton("Divisao"))
        self.button_division_input.clicked.connect(self.show_division_input_view)
        
        self.buttons_layout.addWidget(self.button_multiplication_input)
        self.buttons_layout.addWidget(self.button_division_input)
        
        self.welcome_layout.addLayout(self.buttons_layout)
        
        ## Finalizing welcome screen layout into a widget
        self.welcome_container = QWidget()
        self.welcome_container.setLayout(self.welcome_layout)
        self.welcome_container.setFixedWidth(int(self.screen_size.width() * 0.80))
        
        ## Adding all views to stacked layout
        self.stacked_layout.addWidget(self.welcome_container)
        self.stacked_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        ## Finalizing stacked layout into a widget
        self.stacked_layout_widget = QWidget()
        self.stacked_layout_widget.setLayout(self.stacked_layout)

        ## Finalizing widgets into main application layout
        self.main_application_layout = QHBoxLayout()
        
        self.left_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_application_layout.addItem(self.left_spacer)
        
        self.main_application_layout.addWidget(self.stacked_layout_widget)
        
        self.right_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_application_layout.addItem(self.right_spacer)
        self.main_application_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(self.main_application_layout)
        
        self.showMaximized()
    
    ## Functions (related to what the user sees and stacked layout management)
    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.windowState() & Qt.WindowState.WindowMaximized:
                self.isMaximized = True
            else:
                if self.isMaximized:
                    self.center_on_screen()
                self.isMaximized = False
            
    def center_on_screen(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        
        center_x = int((screen_geometry.width() - self.width()) / 2)
        center_y = int((screen_geometry.height() - self.height()) / 2.5)
        
        self.move(center_x, center_y)
    
    def show_main_menu(self):
        self.stacked_layout.setCurrentWidget(self.welcome_container)
        
        self.destroy_multiplication_input_view()
        self.destroy_division_input_view()
        
    def show_multiplication_input_view(self):
        self.multiplication_input_view = MultiplicationInputView(self.show_main_menu)
        self.multiplication_input_view.setFixedWidth(int(self.screen_size.width() * 0.80))
        
        self.stacked_layout.addWidget(self.multiplication_input_view)
        self.stacked_layout.setCurrentWidget(self.multiplication_input_view)
        
        if not self.isMaximized:
            QTimer.singleShot(0, self.center_on_screen)
            
    def show_division_input_view(self):
        self.division_input_view = DivisionInputView(self.show_main_menu)
        self.division_input_view.setFixedWidth(int(self.screen_size.width() * 0.80))
        
        self.stacked_layout.addWidget(self.division_input_view)
        self.stacked_layout.setCurrentWidget(self.division_input_view)
        
        if not self.isMaximized:
            QTimer.singleShot(0, self.center_on_screen)
            
    ## Clean up functions
    def destroy_multiplication_input_view(self):
        if self.multiplication_input_view:
            self.multiplication_input_view.deleteLater()
            self.stacked_layout.removeWidget(self.multiplication_input_view)
            self.multiplication_input_view.deleteLater()
            self.multiplication_input_view = None
            
    def destroy_division_input_view(self):
        if self.division_input_view:
            self.division_input_view.deleteLater()
            self.stacked_layout.removeWidget(self.division_input_view)
            self.division_input_view.deleteLater()
            self.division_input_view = None        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())