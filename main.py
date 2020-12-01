
from graphics import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog as tk
plt.style.use('seaborn')


def import_data():
    csv_file = tk.askopenfilename()
    data = pd.read_csv(csv_file, sep=r'\s*,\s*', header=0, engine='python')
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

    adv_plot_title = Text(Point(72, 115), 'Advanced Plots')
    adv_plot_title.setStyle('bold')
    adv_plot_title.setSize(20)
    adv_plot_title.draw(win)

    boxplot_button = Rectangle(Point(20, 75), Point(205, 95))
    boxplot_button.setFill('gainsboro')
    boxplot_button.draw(win)
    box_text = Text(Point(112.5, 85), 'CREATE BOXPLOT')
    box_text.setSize(16)
    box_text.draw(win)

    return win, exit_button, selected_variable, submit_button, guide_button, selected_plot, selected_variable2, boxplot_button

def welcome_window():
    # Welcome Window Start

    welcome_win = GraphWin('Welcome!', 600, 400)
    welcome_win.setBackground('white')
    welcome_win.setCoords(0, 0, 60, 40)

    # Could get this from a text file
    welcome_heading = 'Welcome to the Personality Dataset Dashboard!'
    welcome_text = Text(Point(30, 35), welcome_heading)
    welcome_text.setSize(18)
    welcome_text.setStyle('bold')
    welcome_text.draw(welcome_win)

    welcome_message = 'In this dataset, participants completed the Big Five Personality\ntest, and were given a score on a seven-point scale.\
 They\nwere then assigned to watch several movies from different categories, \ne.g diversity, with conditions high, medium or low.\
 Finally,\nthey were asked to rate how much they enjoyed watching the movies\non a scale of 1 to 5.\n\
\nTo get started, please select the dataset.'

    welcome_text2 = Text(Point(30, 21), welcome_message)
    welcome_text2.setSize(12)
    welcome_text2.draw(welcome_win)

    back_button = Rectangle(Point(10, 3), Point(50, 7))
    back_button.setFill('gainsboro')
    back_button.setOutline('black')
    back_button.draw(welcome_win)
    back_text = Text(Point(30, 5), 'Select Dataset')
    back_text.setSize(14)
    back_text.setTextColor('black')
    back_text.draw(welcome_win)

    try:

        click = welcome_win.getMouse()

        while not button_clicked(click, back_button):
            click = welcome_win.getMouse()

        welcome_win.close()

    except GraphicsError:
        welcome_win.close()
    # Welcome Window End

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


def create_boxplot(df, column_names):

    categories = ['serendipity', 'popularity', 'diversity']
    conditions = ['low', 'medium', 'high']

    boxplot_win = GraphWin('Create Boxplot', 960, 650)
    boxplot_win.setBackground('white')
    boxplot_win.setCoords(0, 0, 96, 65)

    variables = Text(Point(76, 58), 'Personality Traits:')
    variables.setStyle('bold')
    variables.setTextColor('gray')
    variables.draw(boxplot_win)
    for i in range(len(column_names)):
        col = Text(Point(76, 55 - (2 * i)), column_names[i])
        col.setTextColor('gray')
        col.draw(boxplot_win)

    movie_category = Text(Point(76, 41), 'Movie Categories:')
    movie_category.setStyle('bold')
    movie_category.setTextColor('gray')
    movie_category.draw(boxplot_win)
    for i in range(len(categories)):
        cat = Text(Point(76, 38 - (2 * i)), categories[i])
        cat.setTextColor('gray')
        cat.draw(boxplot_win)

    available_conditions = Text(Point(76, 28), 'Possible Conditions:')
    available_conditions.setStyle('bold')
    available_conditions.setTextColor('gray')
    available_conditions.draw(boxplot_win)
    for i in range(len(conditions)):
        cond = Text(Point(76, 25 - (2*i)), conditions[i])
        cond.setTextColor('gray')
        cond.draw(boxplot_win)

    submit_button = Rectangle(Point(5, 5), Point(60, 10))
    submit_button.setFill('steelblue')
    submit_button.setOutline('steelblue')
    submit_button.draw(boxplot_win)
    submit_text = Text(Point(32.5, 7.5), 'Submit')
    submit_text.setSize(20)
    submit_text.setTextColor('white')
    submit_text.draw(boxplot_win)

    back_button = Rectangle(Point(67, 5), Point(87, 10))
    back_button.setFill('gainsboro')
    back_button.setOutline('black')
    back_button.draw(boxplot_win)
    back_text = Text(Point(77, 7.5), 'Back')
    back_text.setSize(20)
    back_text.setTextColor('black')
    back_text.draw(boxplot_win)

    # Input Variable
    variable_text = Text(Point(32.5, 55), 'Personality Trait:')
    variable_text.setSize(20)
    variable_text.draw(boxplot_win)
    selected_variable = Entry(Point(32.5, 50), 20)
    selected_variable.setFill('white')
    selected_variable.setSize(20)
    selected_variable.draw(boxplot_win)

    # Input Category
    category_text = Text(Point(32.5, 41), 'Movie Category:')
    category_text.setSize(20)
    category_text.draw(boxplot_win)
    selected_cat = Entry(Point(32.5, 36), 20)
    selected_cat.setFill('white')
    selected_cat.setSize(20)
    selected_cat.draw(boxplot_win)

    # Input Condition
    condition_text = Text(Point(32.5, 27), 'Condition:')
    condition_text.setSize(20)
    condition_text.draw(boxplot_win)
    selected_cond = Entry(Point(32.5, 22), 20)
    selected_cond.setFill('white')
    selected_cond.setSize(20)
    selected_cond.draw(boxplot_win)

    try:
        click = boxplot_win.getMouse()

        while not button_clicked(click, back_button):

            if button_clicked(click, submit_button):

                selected_trait = selected_variable.getText()
                selected_category = selected_cat.getText()
                selected_condition = selected_cond.getText()

                if selected_trait in column_names and selected_category in categories and selected_condition in conditions:

                    df1 = df.copy()
                    df1['trait'] = ['High' if x > sum(df1[selected_trait]) / len(df1[selected_trait]) else 'Low' for x in df1[selected_trait]]

                    df_filtered = df1[df1['assigned metric'] == selected_category]
                    df_filtered2 = df_filtered[df_filtered['assigned condition'] == selected_condition]

                    fig, ax = plt.subplots()
                    df_filtered2.boxplot(column='enjoy_watching', by='trait', ax=ax)
                    fig.suptitle('')
                    plt.title('Boxplot for Movies Rated ' + selected_condition.capitalize() + ' in ' + selected_category.capitalize())
                    plt.xlabel(selected_trait.capitalize())
                    plt.ylabel('Amount Enjoyed by Participant')
                    plt.savefig('boxplot.png')
                    plt.clf()

                    boxplot_win.close()
                    return Image(Point(454, 220), 'boxplot.png')

                else: error_message()

            click = boxplot_win.getMouse()

        boxplot_win.close()
        return None

    except GraphicsError:
        boxplot_win.close()
        return None


def error_message():
    error_win = GraphWin('Invalid Submission', 400, 100)
    error_win.setBackground('orangered')
    error_win.setCoords(0, 0, 40, 10)
    message = Text(Point(20, 5), 'Sorry your input was invalid :(\nPlease refer to the guide for which variables\nand plots can be used and ensure no spelling\nmistakes were made.')
    message.setTextColor('white')
    message.draw(error_win)


def main():

    welcome_window()

    try:
        df = import_data()
        column_names = list(df.columns)[:5]
        available_plots = ['histogram', 'scatter']

        win, exit_button, selected_variable, submit_button, guide_button, selected_plot, selected_variable2, boxplot_button = create_gui()

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

            if button_clicked(click, boxplot_button):
                box_plot = create_boxplot(df, column_names)
                if box_plot:
                    box_plot.draw(win)

            click = win.getMouse()

        win.close()

    except:
        print('Sorry the data set you selected was invalid :(')

if __name__ == '__main__':
    main()
