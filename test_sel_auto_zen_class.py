""" Selenium Automation to create a new query
     in ZenClass Portal
     Dev:Megha
     Version:1
     Date Create:03/07/2022"""
import time
import pandas as pd
import pytest
import sel_auto_zen_class



class TestZenPortal:
    """testing functions for sel_auto_zen_class"""

    def test_login_zen(self):
        """Login to zen portal"""

        sel_auto_zen_class.zen.login_zen("test@example.com", "123456")
        time.sleep(5)
        # if login is successful, class page will be the current url
        assert "/class" in sel_auto_zen_class.zen.driver.current_url

    def test_excel(self):
        """ access items from the menubar"""
        l_menu = sel_auto_zen_class.zen.driver.execute_script(
            " l_menu_items=document.getElementsByClassName"
            '("list-scroll py-3 color-area");'
            " l_menu_logo= document.getElementsByClassName"
            '("ml-3 d-inline-block mt-3 font-weight-bold")[0].innerText;'
            "l_menu_head=document.getElementsByClassName"
            '("list-scroll py-3 active-area active-left-bar")[0].innerText;'
            " l_menu=[];"
            """for (let index = 0; index < l_menu_items.length; index++)
                   {
                   l_menu[index]=l_menu_items.item(index).innerText;
                   }
                   l_menu.splice(0,0,l_menu_logo,l_menu_head);
                   return l_menu ;"""
        )
        time.sleep(5)
        df_fm = pd.DataFrame(l_menu, columns=["Main-menu"])
        # check dataframes
        pd.testing.assert_frame_equal(sel_auto_zen_class.zen.main_menu(), df_fm)
        time.sleep(5)

    def test_new_query(self):
        """ check the header of the newly created query in the query page"""
        query_text_head = "Guvi Python AT - 1 &2 Automation Project"

        assert query_text_head in sel_auto_zen_class.zen.new_query()
