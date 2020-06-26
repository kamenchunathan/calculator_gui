import kivy
from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

kivy.require('1.11.0')


# set graphics to a resizable form
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 600)


class CalcGridLayout(GridLayout):
    """Controlling layout of the calculator"""

    def on_equals_pressed(self):
        self.calculate(self.display.text)


    def calculate(self, expression_to_evaluate):
        """
            called when the equals key is pressed
            takes in and expression and evaluates it using pythons built in eval() function and
        """

        if expression_to_evaluate is not None:
            try:
                # solve and display in entry
                self.display.text = str(eval(expression_to_evaluate))
            except Exception:
                self.display.text = 'Error: the expression you have entered cannot be evaluated'


class CalculatorApp(App):
    """Main class of the application"""
    def build(self):
        calc = CalcGridLayout()
        return calc


def main():
    simple_calc = CalculatorApp()
    simple_calc.run()

if __name__ == '__main__':
    main()