import streamlit as st
from PIL import Image

import sys
import os

# Get the absolute path of the Transactions2 directory
module_path = os.path.abspath("Transactions2")

# Add it to sys.path if not already included
project_root = os.path.abspath(os.path.dirname(__name__))
if project_root not in sys.path:
    sys.path.append(project_root)

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.sidebar.title("Hello")
choice = st.sidebar.radio(
    "Choose an option:",
    ["Home", "🛒 Transactions", "📊 Graphs"],
    index=0
)

# if choice == "🛒 Transactions":
#     # Import the Transactions page
#     import Transactions2.Pages.Transactions  # Update the file name if renamed
# elif choice == "📊 Graphs":
#     # Import the Graphs page
#     import Transactions2.Pages.Graphs  # Ensure the file exists
if choice == "🛒 Transactions":
    # Import and display the Transactions page
    from Transactions2.Pages import Transactions
    Transactions.main()  # Ensure `Transactions.py` has a `main()` function
elif choice == "📊 Graphs":
    # Import and display the Graphs page
    from Transactions2.Pages import Graphs
    Graphs.main()  # Ensure `Graphs.py` has a `main()` function
elif choice == "Home":
    st.write("# Welcome to Paypal Reviews")
    st.markdown(
        """
        These 2 Apps Help us review transactions from a customer

        *👈 Select an app from the sidebar* to get started

        If an app isn't working correctly, reach out to Lowwie

        ### Want to learn more?
        - Check out The [YouTube Video](#)
        """
    )
else:
    st.error("Invalid Page Selected")
