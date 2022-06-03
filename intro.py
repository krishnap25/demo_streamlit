import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Demos instructions:
# 1. Uncomment/comment the call to the functions in the main step by step
# 2. Uncomment the pass lines inside the functions to move on the next illustration


def printing():
    # Let's just print something on the app
    msg = "Hello world"

    # To print something, you can simply use st.write
    st.write(msg)
    # pass

    # st.write can handle lots of objects (tables, arrays, etc...)
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    st.write(df)
    # pass

    # There exist some specific functions to render objects in different ways
    # st.write just uses the default way, uncomment the lines below to see
    st.table(df)
    # pass
    # Before st.write(df) was equivalent to st.dataframe(df)
    # Similarly you can change the way the text is displayed using, e.g.,
    st.code(msg)
    st.latex("\int e^{-x^2/2} = \sqrt{2\pi}")
    # pass

    # You can easily make plots too
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)
    # pass

    # For more writing options see https://docs.streamlit.io/library/api-reference


def interact():
    # To interact with the user, a variable is defined via some widget
    # For a simple sliding bar, use
    x = st.slider('x')
    # You can then access the variable input by the user and use it later on in your code such as
    st.write(x, 'squared is', x * x)
    # Streamlit works by simply rerunning your code each time one of these variables has changed
    # Hence depending on the number of operations made on the input variable the code may be slow/fast
    pass

    # You may also access the variable by defining a key registered in streamlit such as
    st.text_input("Your name", key="name")
    st.write("Hello", st.session_state.name, "!")
    pass

    # You can use checkboxes
    if st.checkbox('Show line chart'):
        chart_data = pd.DataFrame(
           np.random.randn(20, 3),
           columns=['a', 'b', 'c'])

        st.line_chart(chart_data)
    pass

    # Or selectboxes
    option = st.selectbox('Choose a number', [1, 2, 3, 4])
    st.write('The square of the number you selected is: ', option**2)
    pass

    # Again check https://docs.streamlit.io/library/api-reference for more options


def layout():
    # You can put text/sliders/slectboxes in a slidebar for a nicer presentation
    contact = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )
    values = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )
    pass

    # You can arrange the text into columns and add headers for example
    left_column, right_column = st.columns(2)
    left_column.header('Contact')
    left_column.write(f'Ok I will contact you by {contact}')

    # More simply you can call streamlit inside a with block
    with right_column:
        st.header('Range')
        st.write(f"You are between {values[0]} and {values[1]}!")


if __name__ == '__main__':
    printing()
    # interact()
    # layout()

    # Streamlit can handle multiple python files to navigate in a code easily
    # You simply need to create a folder called 'pages' and put the streamlit apps inside
    # In our case just rename the folder 'to_rename' to 'pages' to continue





