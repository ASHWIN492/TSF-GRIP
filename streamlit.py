import streamlit as st

def main():
    # Set page title and icon
    st.set_page_config(page_title="Student Score Predictor", page_icon="📚")

    st.title("Predict the Percentage of a Student")
    st.subheader("Based on the Number of Study Hours per Day")

    # Text input for hours studied
    hours = st.text_input('Enter the number of hours student studied')

    # Predict button
    if st.button('Predict'):
        if hours:
            st.success(f"Predicted Score = {hours}")  # Replace with actual prediction logic
        else:
            st.warning("Please enter the number of hours.")

if __name__ == "__main__":
    main()
