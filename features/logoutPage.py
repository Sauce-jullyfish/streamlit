import streamlit as st
from streamlit_local_storage import LocalStorage
local_storage = LocalStorage()


def logout():
    if local_storage.getItem("token"):
        local_storage.deleteItem("token")
    st.rerun()
