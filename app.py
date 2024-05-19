import streamlit as st
from streamlit_local_storage import LocalStorage

from features.loginPage import login_page
from components.sidemenu import SideMenuRouter


# 初始化主界面配置
st.set_page_config(page_title='智慧家庭', layout='wide')
localS = LocalStorage()


def main():
    # 檢查 local_storage 是否有 token
    if not localS.getItem('token'):
        # 如果沒有 token，則跳轉到登錄頁面
        login_page()
    else:
        # 如果有 token，則顯示首頁
        st.title("首頁內容")
        SideMenuRouter()


if __name__ == "__main__":
    main()
