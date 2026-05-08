import streamlit as st

st.title("🎬 Movie Ticket Booking System")

try:
    # Input
    name = st.text_input("Enter Customer Name")

    movie = st.selectbox("Select Movie", [
        "Avangers",
        "Kung Fu Panda",
        "Frozen"
    ])

    time = st.selectbox("Select Show Time", [
        "10:00 AM",
        "2:00 PM",
        "8:00 PM"
    ])

    seat = st.radio("Select Seat Type", [
        "Standard",
        "Premium"
    ])

    # Button
    if st.button("Book Ticket"):
        if name == "":
            st.error("❌ Customer name cannot be empty!")
        else:
            st.success("✅ Booking Successful!")
            st.write("### 🎟 Booking Details")
            st.write("Customer Name:", name)
            st.write("Movie:", movie)
            st.write("Show Time:", time)
            st.write("Seat Type:", seat)

except Exception as e:
    st.error("⚠️ An error occurred: " + str(e))