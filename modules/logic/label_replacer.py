from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
def label_replacer(current_text):

    if current_text == "Binary":
        regex = QRegularExpressionValidator(QRegularExpression("[0-1]+"))
        return "Decimal","Hex","Octal",regex
    
    elif current_text == "Octal":
        regex = QRegularExpressionValidator(QRegularExpression("[0-7]+"))
        return "Binary","Decimal","Hex",regex
    
    elif current_text == "Decimal":
        regex = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        return "Binary","Hex","Octal",regex
    
    elif current_text == "Hex":
        regex = QRegularExpressionValidator(QRegularExpression("[0-9A-F]+"))
        return "Binary","Decimal","Octal",regex
    

