import streamlit as st
import requests
from streamlit_local_storage import LocalStorage
import os
from dotenv import load_dotenv
local_storage = LocalStorage()
load_dotenv()
BASE_ENDPOINT = os.getenv('BASE_ENDPOINT')

# login_page


def login_page():
    st.title('登入')
    with st.form(key='user_login_form'):
        username = st.text_input('使用者名稱')
        password = st.text_input('密碼', type='password')
        login_button = st.form_submit_button('登入')
        if login_button:
            response = requests.post(f'{BASE_ENDPOINT}/users/signin', json={
                "username": username,
                "password": password
            })
            if response.status_code == 200:
                # 登入成功，取得 token
                data = response.json().get('data')
                token = data.get('token')
                local_storage.setItem('token', token)
                st.success('登入成功!')
            else:
                st.error('登入失敗: {}'.format(response.json().get('message')))
            # return username, password
