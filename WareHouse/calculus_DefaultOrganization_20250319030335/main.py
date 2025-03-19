'''
This module contains the main GUI class for the calculator application. It uses PyQt5 to create a window with buttons and text fields for input and output.
'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget
import math
class CalculatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setup_ui()
    def setup_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        # Create input and output fields
        self.input_field = QLineEdit()
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)
        # Create buttons for numbers, operators, and trigonometric functions
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', '^',
        ]
        for button in buttons:
            if button.isdigit() or button == '.' or button == '=':
                btn = QPushButton(button)
                btn.clicked.connect(self.on_number_clicked if button.isdigit() else self.on_operator_clicked)
            elif button in ['+', '-', '*', '/']:
                btn = QPushButton(button)
                btn.clicked.connect(lambda _, op=button: self.on_operator_clicked(op))
            elif button == '^':
                btn = QPushButton('^')
                btn.clicked.connect(self.on_power_clicked)
            elif button in ['sin', 'cos', 'tan']:
                btn = QPushButton(button)
                btn.clicked.connect(lambda _, func=button: self.on_trigonometric_function_clicked(func))
        # Create clear and calculate buttons
        clear_btn = QPushButton('C')
        calculate_btn = QPushButton('=')
        clear_btn.clicked.connect(self.on_clear_clicked)
        calculate_btn.clicked.connect(self.on_calculate_clicked)
        # Add buttons to layout
        layout.addWidget(self.input_field)
        layout.addWidget(self.output_field)
        for row in range(4):
            row_layout = QHBoxLayout()
            for col in range(3):
                index = row * 3 + col
                if index < len(buttons):
                    btn = buttons[index]
                    row_layout.addWidget(QPushButton(btn))
            layout.addLayout(row_layout)
        layout.addWidget(clear_btn)
        layout.addWidget(calculate_btn)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def on_number_clicked(self, number):
        current_text = self.input_field.text()
        if current_text[-1] in ['+', '-', '*', '/']:
            current_text = current_text[:-1]
        self.input_field.setText(current_text + number)
    def On_operator_clicked(self, operator):
        current_text = self.input_field.text()
        if current_text[-1].isdigit():
            self.input_field.setText(current_text + operator)
    def On_power_clicked(self):
        current_text = self.input_field.text()
        if current_text[-1].isdigit():
            self.input_field.setText(current_text + '^')
    def On_trigonometric_function_clicked(self, func):
        current_text = self.input_field.text()
        if current_text[-1].isdigit():
            self.input_field.setText(current_text + f'{func}(')
    def On_clear_clicked(self):
        self.input_field.clear()
        self.output_field.clear()
    def On_calculate_clicked(self):
        try:
            result = eval(self.input_field.text())
            self.output_field.setText(str(result))
        except Exception as e:
            self.output_field.setText('Error')
if __name__ == '__main__':
    app = QApplication([])
    calculator = CalculatorGUI()
    calculator.show()
    app.exec_()