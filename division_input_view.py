from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QScrollArea
from logic import binaryDivide, convertDecimalToBinary, convertBinaryArrayToDecimal, generateArr

class DivisionInputView(QWidget):
    def __init__(self, show_main_menu_callback):
        super().__init__()
        
        self.show_main_menu_callback = show_main_menu_callback
        
        self.manual_input_layout = QVBoxLayout()
        self.manual_input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.manual_input_layout_label = QLabel("<h2>Divisao Sem Sinal</h2>")
        self.manual_input_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manual_input_layout.addWidget(self.manual_input_layout_label)
        
        
        ## Header buttons
        self.continue_button_layout = QHBoxLayout()
        self.continue_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_validate_input = (QPushButton("Dividir"))
        self.button_script_validate_input.clicked.connect(self.validate_and_divide)
        self.continue_button_layout.addWidget(self.button_script_validate_input)
        self.manual_input_layout.addLayout(self.continue_button_layout)
        
        self.choices_bottom = QHBoxLayout()
        self.choices_bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_script_show_options_menu = (QPushButton("Resetar"))
        self.button_script_show_options_menu.clicked.connect(self.reset)
        self.choices_bottom.addWidget(self.button_script_show_options_menu)
        self.manual_input_layout.addLayout(self.choices_bottom)
        
        self.back_button_layout = QHBoxLayout()
        self.back_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.manual_input_layout_back_button = (QPushButton("Voltar"))
        self.manual_input_layout_back_button.clicked.connect(self.show_main_menu_callback)
        self.back_button_layout.addWidget(self.manual_input_layout_back_button)
        self.manual_input_layout.addLayout(self.back_button_layout)
        
        
        ## Input fields
        self.variables_layout = QHBoxLayout()
        self.variables_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.variables_layout_dividend_label = QLabel("<h3>Dividendo</h3>")
        self.variables_layout_dividend_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.variables_layout.addWidget(self.variables_layout_dividend_label)
        
        self.variables_layout_dividend_input = QLineEdit()
        self.variables_layout_dividend_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.variables_layout_dividend_input.setPlaceholderText("Insira o dividendo")
        self.variables_layout.addWidget(self.variables_layout_dividend_input)
        
        self.variables_layout_divisor_label = QLabel("<h3>Divisor</h3>")
        self.variables_layout_divisor_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.variables_layout.addWidget(self.variables_layout_divisor_label)
        
        self.variables_layout_divisor_input = QLineEdit()
        self.variables_layout_divisor_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.variables_layout_divisor_input.setPlaceholderText("Insira o divisor")
        self.variables_layout.addWidget(self.variables_layout_divisor_input)
        
        self.manual_input_layout.addLayout(self.variables_layout)
                
                
        self.output_layout = QVBoxLayout()
        self.output_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.output_layout_label = QLabel("<h2>Passos realizados na divisao binaria sem sinal</h2>")
        self.output_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_layout.addWidget(self.output_layout_label)
        
        self.output_contents_layout = QHBoxLayout()
        self.output_contents_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.output_contents_layout_label = QLabel("")
        self.output_contents_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_contents_layout.addWidget(self.output_contents_layout_label)

        self.output_layout.addLayout(self.output_contents_layout)
        
        
        self.manual_input_layout.addLayout(self.output_layout)
        
        # output_layout items start invisible
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)
        
        
        self.scroll_container_layout = QVBoxLayout()
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        scroll_content = QWidget()
        scroll_content.setLayout(self.manual_input_layout)
        
        scroll_area.setWidget(scroll_content)
        
        self.scroll_container_layout.addWidget(scroll_area)
        
        
        self.setLayout(self.scroll_container_layout)
    
    def validate_and_divide(self):
        dividend = self.variables_layout_dividend_input.text()
        divisor = self.variables_layout_divisor_input.text()
        
        if not self.validate_value(dividend, "dividendo"):
            return
        else:
            dividend = int(self.variables_layout_dividend_input.text())
            
        if not self.validate_value(divisor, "divisor"):
            return
        elif (int(self.variables_layout_divisor_input.text()) == 0):
            QMessageBox.warning(self, "Valor invalido!", f"O valor inserido para o divisor e invalido. Nao e possivel dividir por 0!")
            return
        else:
            divisor = int(self.variables_layout_divisor_input.text())
            
        binary_dividend = convertDecimalToBinary(dividend)
        binary_divisor = convertDecimalToBinary(divisor)
        dividend_binary_array = generateArr(binary_dividend)
        divisor_binary_array = generateArr(binary_divisor)
        
        quotient, remainder, log = binaryDivide(divisor_binary_array, dividend_binary_array)
        decimalQuotient = convertBinaryArrayToDecimal(quotient)
        decimalRemainder = convertBinaryArrayToDecimal(remainder)
        
        log.insert(0, f"{dividend} / {divisor} = {decimalQuotient} com resto {decimalRemainder}")
        log.insert(0, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        
        self.output_contents_layout_label.setText('\n'.join(log))
        
    def validate_value(self, value, what_is_it):
        if not self.is_integer(value):
            QMessageBox.warning(self, "Valor invalido!", f"O valor inserido para o {what_is_it} e invalido. Por favor, insira um valor numerico.")
            return False 
        elif not self.is_integer_float(value):
            QMessageBox.warning(self, "Valor invalido!", f"O valor inserido para o {what_is_it} e invalido. Por favor, insira um valor inteiro.")
            return False 
        elif (int(value) > 32767):
            QMessageBox.warning(self, "Valor invalido!", f"O valor inserido para o {what_is_it} e invalido. Por favor, insira um valor que possa ser representado em 15 bits (menor ou igual que 32767).")
            return False 
        elif (int(value) < 0):
            QMessageBox.warning(self, "Valor invalido!", f"O valor inserido para o {what_is_it} e invalido. Por favor, insira um valor positivo.")
            return False 
        else:
            return True
        
    def is_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False 
        
    def is_integer_float(self, value):
        try:
            float_value = float(value)
            int_value = int(float_value)
            return float_value == int_value
        except (ValueError, TypeError):
            return False
                    
    def reset(self):
        self.variables_layout_dividend_input.setText("")
        self.variables_layout_divisor_input.setText("")
        self.output_contents_layout_label.setText("")
                
        for i in range(self.output_layout.count()):
            item = self.output_layout.itemAt(i)

            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(False)