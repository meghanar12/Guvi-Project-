""" Selenium Automation to create a new query
     in ZenClass Portal
     Dev:Megha
     Version:1
     Date Create:03/07/2022"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ZenPortal:
    """Class Name : ZenPortal
    Functions :  login
                 access mainmenu items
                 newquery"""

    url = "https://www.zenclass.in/login"
    driver = webdriver.Firefox()

    def login_zen(self, username, password):
        """Login to zen portal"""

        try:

            self.driver.get(self.url)
            self.driver.maximize_window()
            # timer For 5 seconds  to load all elements
            time.sleep(5)
            # xpath of the username and password input & submit button
            username_xpath = (
                "/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input"
            )
            password_xpath = (
                "/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input"
            )
            submit_button_xpath = (
                "/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button"
            )
            username1 = self.driver.find_element(by=By.XPATH, value=username_xpath)
            password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
            submit_button = self.driver.find_element(by=By.XPATH, value=submit_button_xpath)

            username1.send_keys(username)
            password1.send_keys(password)

            submit_button.click()
            time.sleep(5)
            return "success"
        except:
            return "failed"

    def main_menu(self):
        """
        ************************************************************
        Accessing Zen portal items on the left-hand side of the page
        ************************************************************
        """
        time.sleep(5)
        l_menu = self.driver.execute_script(
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
        # convert list to dataframe
        df_fm = pd.DataFrame(l_menu, columns=["Main-menu"])

        writer = pd.ExcelWriter("ZenClass.xlsx", engine="xlsxwriter")

        # Convert the dataframe to an XlsxWriter Excel object.
        df_fm.to_excel(writer, sheet_name="Main-menu", index=False)

        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = workbook.add_worksheet("Class")
        # Take screenshot of the page
        self.driver.get_full_page_screenshot_as_file("Class.png")

        # Insert an image.
        worksheet.insert_image("A1", "Class.png")

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        return df_fm

    def new_query(self):
        """*******************
        create new query
        *********************"""
        try:
            # open create new query page
            self.driver.get("https://www.zenclass.in/queries/create")
            time.sleep(5)
            # *************************************
            # Enter new query details
            # *************************************
            query_text_head = "Guvi Python AT - 1 &2 Automation Project"
            query_text_body = """This is a Project Test Code Running for the Python Automation
            -1&2 Project Given by mentor Mr. Suman Gangopadhyay"""
            # Xpath of the elements  in the newquery page
            query_txt_head_path = (
            '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input'
            )
            query_txt_body_path = (
            '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
            )
            query_create_btn_path = (
            '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button'
            )
            query_cat_path = """//*[@id="root"]/div[2]/div/div[2]/div/div/form/
            div[2]/div[1]/select/option[2]"""
            query_sub_cat_path = """//*[@id="root"]/div[2]/div/div[2]/div/div/form/
            div[2]/div[2]/select/option[2]"""
            # query_language = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select'
            query_txt_head_path1 = self.driver.find_element(
            by=By.XPATH, value=query_txt_head_path
            )
            query_txt_body_path1 = self.driver.find_element(
            by=By.XPATH, value=query_txt_body_path
            )
            query_create_btn_path1 = self.driver.find_element(
            by=By.XPATH, value=query_create_btn_path
            )
            query_cat_path1 = self.driver.find_element(by=By.XPATH, value=query_cat_path)

            time.sleep(5)
            query_txt_head_path1.send_keys(query_text_head)
            query_txt_body_path1.send_keys(query_text_body)
            query_cat_path1.send_keys("Zen-Class Doubt")
            time.sleep(5)
            query_sub_cat_path1 = self.driver.find_element(
            by=By.XPATH, value=query_sub_cat_path
            )

            # select_sub_cat = Select(self.driver.find_element(by=By.NAME,value="subcategory"))
            # query_sub_cat_path1.select_by_index(2)

            query_sub_cat_path1.send_keys("Task")
            time.sleep(5)

            # query_language1=self.driver.find_elements(by=By.XPATH,value=query_language)
            # query_language1.send_keys("English")
            select_lang = Select(self.driver.find_element(by=By.NAME, value="language"))
            select_lang.select_by_index(1)
            time.sleep(5)
            # call Click function of  create Button to submit the newquery
            query_create_btn_path1.click()
            time.sleep(5)
            self.driver.get_full_page_screenshot_as_file("new_query.png")

            # return the query header

            self.driver.get("https://www.zenclass.in/queries")
            time.sleep(5)
            query_result = self.driver.execute_script(
              'return document.getElementsByClassName'\
              '("Queries_sq__tile__title__I0aWK")[0].innerText')
            time.sleep(5)
            self.driver.close()
            return query_result

        except:
            return "Failed"


# Create Zen object from Zenportal Class
zen = ZenPortal()
