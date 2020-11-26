
from graphics import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog as tk
plt.style.use('seaborn')


def import_data():
    csv_file = tk.askopenfilename()
    data = pd.read_csv(csv_file, sep=r'\s*,\s*', header=0)
    df = data[['openness', 'agreeableness', 'emotional_stability', 'conscientiousness',
           'extraversion', 'assigned metric', 'assigned condition', 'enjoy_watching']]
    return df


def button_clicked(click, button):
    bottom_left = button.getP1()
    top_right = button.getP2()
    return bottom_left.getX() < click.getX() < top_right.getX() and bottom_left.getY() < click.getY() < top_right.getY()


def create_gui():
    win = GraphWin('Data Visualization App', 1366, 768)
    win.setBackground('white')
    win.setCoords(0.0, 0.0, 683, 384)

    gray_sidebar = Rectangle(Point(0, 0), Point(225, 384))
    gray_sidebar.setOutline('whitesmoke')
    gray_sidebar.setFill('whitesmoke')
    gray_sidebar.draw(win)

    exit_button = Rectangle(Point(603, 20), Point(663, 45))
    exit_button.setFill('steelblue')
    exit_button.setOutline('steelblue')
    exit_button.draw(win)
    exit_text = Text(Point(633, 32.5), 'Exit')
    exit_text.setSize(20)
    exit_text.setTextColor('white')
    exit_text.draw(win)

    simple_plot_title = Text(Point(60, 360), 'Simple Plots')
    simple_plot_title.setStyle('bold')
    simple_plot_title.setSize(20)
    simple_plot_title.draw(win)

    submit_button = Rectangle(Point(145, 150), Point(205, 175))
    submit_button.setFill('steelblue')
    submit_button.setOutline('steelblue')
    submit_button.draw(win)
    submit_text = Text(Point(175, 162.5), 'Submit')
    submit_text.setSize(20)
    submit_text.setTextColor('white')
    submit_text.draw(win)

    guide_button = Rectangle(Point(20, 320), Point(140, 340))
    guide_button.setFill('gainsboro')
    guide_button.draw(win)
    guide_text = Text(Point(80, 330), 'GUIDE')
    guide_text.setSize(16)
    guide_text.draw(win)

    plot_choice_text = Text(Point(50, 300), 'Type of Plot:')
    plot_choice_text.setSize(16)
    plot_choice_text.draw(win)
    selected_plot = Entry(Point(80, 280), 20)
    selected_plot.setFill('white')
    selected_plot.setSize(16)
    selected_plot.draw(win)

    variable1_text = Text(Point(65, 260), 'Name of X variable:')
    variable1_text.setSize(16)
    variable1_text.draw(win)
    selected_variable = Entry(Point(80, 240), 20)
    selected_variable.setFill('white')
    selected_variable.setSize(16)
    selected_variable.draw(win)

    variable2_text = Text(Point(65, 220), 'Name of Y variable:')
    variable2_text.setSize(16)
    variable2_text.draw(win)
    selected_variable2 = Entry(Point(80, 200), 20)
    selected_variable2.setFill('white')
    selected_variable2.setSize(16)
    selected_variable2.draw(win)

    line = Line(Point(0, 135), Point(225, 135))
    line.setFill('gainsboro')
    line.draw(win)

    adv_plot_title = Text(Point(70, 115), 'Advanced Plots')
    adv_plot_title.setStyle('bold')
    adv_plot_title.setSize(20)
    adv_plot_title.draw(win)

    return win, exit_button, selected_variable, submit_button, guide_button, selected_plot, selected_variable2


def show_guide(column_names, available_plots):
    guide_win = GraphWin('Guide', 600, 400)
    guide_win.setBackground('white')
    guide_win.setCoords(0, 0, 30, 20)

    plots = Text(Point(5, 18), 'Available plots:')
    plots.setStyle('bold')
    plots.draw(guide_win)
    for i in range(len(available_plots)):
        Text(Point(5, 16 - (2 * i)), available_plots[i]).draw(guide_win)

    variables = Text(Point(15, 18), 'Available variables:')
    variables.setStyle('bold')
    variables.draw(guide_win)
    for i in range(len(column_names)):
        Text(Point(15, 16 - (2 * i)), column_names[i]).draw(guide_win)


def create_histogram(df, variable):
    plt.hist(df[variable])
    plt.title('Histogram of ' + variable.capitalize())
    plt.savefig('histogram.png')
    plt.clf()


def create_scatter(df, variable1, variable2):
    plt.scatter(df[variable1], df[variable2])
    plt.title('Scatter Plot of ' + variable2.capitalize() + ' vs. ' + variable1.capitalize())
    plt.xlabel(variable1.capitalize())
    plt.ylabel(variable2.capitalize())
    plt.savefig('scatter.png')
    plt.clf()


def error_message():
    error_win = GraphWin('Invalid Submission', 400, 100)
    error_win.setBackground('orangered')
    error_win.setCoords(0, 0, 40, 10)
    message = Text(Point(20, 5), 'Sorry your input was invalid :(\nPlease refer to the guide for which variables\nand plots can be used and ensure no spelling\nmistakes were made.')
    message.setTextColor('white')
    message.draw(error_win)


def main():

    df = import_data()
    column_names = list(df.columns)[:5]
    available_plots = ['histogram', 'scatter']

    win, exit_button, selected_variable, submit_button, guide_button, selected_plot, selected_variable2 = create_gui()

    click = win.getMouse()

    while not button_clicked(click, exit_button):

        if button_clicked(click, submit_button):

            if selected_plot.getText() in available_plots:

                if selected_variable.getText() in column_names:

                    if selected_plot.getText() == 'histogram':
                        create_histogram(df, selected_variable.getText())
                        histogram = Image(Point(454, 220), 'histogram.png')
                        histogram.draw(win)

                    elif selected_variable2.getText() in column_names:

                        if selected_plot.getText() == 'scatter':
                            create_scatter(df, selected_variable.getText(), selected_variable2.getText())
                            scatter = Image(Point(454, 220), 'scatter.png')
                            scatter.draw(win)

                        else: error_message()

                    else: error_message()

                else: error_message()

            else: error_message()

        if button_clicked(click, guide_button):
            show_guide(column_names, available_plots)

        click = win.getMouse()

    win.close()


if __name__ == '__main__':
    main()
