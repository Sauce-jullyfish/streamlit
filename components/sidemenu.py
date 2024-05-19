from streamlit_router import StreamlitRouter
import streamlit as st
from streamlit_option_menu import option_menu

from features.logoutPage import logout

# 假設有幾個分頁函數用於渲染不同的內容


def home_page():
    st.title("Home Page")


def projects_page():
    st.title("Projects")


def tasks_page():
    st.title("My Tasks")


def settings_page():
    st.title("Settings")

# 登出按鈕的處理邏輯


# def logout():
#     # 實現登出邏輯
#     pass

# Test Toast 的顯示邏輯


def test_toast():
    st.success("Test Toast Message")


class SideMenuRouter(StreamlitRouter):

    routes_set = {
        "Home": home_page,
        "Projects": projects_page,
        "My Tasks": tasks_page,
        "Settings": settings_page,
        "Logout": logout,
        "Test Toast": test_toast
    }

    def __init__(self):
        super().__init__()
        self.routes = self.routes_set

        # 獲取側邊欄選單選項
        selected_route = self.side_menu()

        # 基於選定選項調用相應的函數
        page_func = self.routes.get(selected_route)
        if page_func:
            page_func()
        else:
            st.error("Error: Page not found")

    def side_menu(self):
        with st.sidebar:
            st.image("images/icon-light.png", width=100)  # 根據實際路徑調整
            # 使用Streamlit Option Menu 插件創建選單項目
            selected = option_menu(
                menu_title="",
                options=["Home", "Projects", "My Tasks",
                         "Settings", "Logout", "Test Toast"],
                icons=['house', 'journal-code', 'check2-square',
                       'gear', 'box-arrow-left', 'bell'],
                menu_icon="cast", default_index=0)

            return selected
