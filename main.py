import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import urllib.parse
from bs4 import BeautifulSoup


#CHANGE CSV NAME
df = pd.read_csv("siha.csv")
data_dict = df.to_dict('records')
barcodes = [item['Barcode'] for item in data_dict]
# names = [item['Name'] for item in data_dict]
chrome_options = webdriver.ChromeOptions()



for barcode in barcodes:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/search?q=5285000201168&sca_esv=560946880&tbm=isch&sxsrf=AB5stBi24FB3-HvM3lZXc7ICrUqeHo3rAQ%3A1693299850492&source=hp&biw=1920&bih=995&ei=irTtZIeVG-PHkdUP96OoiAM&iflsig=AD69kcEAAAAAZO3CmjYgqhpcqRhnPykrz3kO7zPj6_kn&ved=0ahUKEwiHgtbAwYGBAxXjY6QEHfcRCjEQ4dUDCAc&uact=5&oq=5285000201168&gs_lp=EgNpbWciDTUyODUwMDAyMDExNjgyBBAjGCdIwQdQ3wRY3wRwAXgAkAEAmAHBAaABwQGqAQMwLjG4AQPIAQD4AQL4AQGKAgtnd3Mtd2l6LWltZ6gCCsICBxAjGOoCGCc&sclient=img")

    search_feild = driver.find_element(By.ID,'REsRA')
    search_feild.clear()
        # time.sleep(1)
    search_feild.send_keys(barcode)
    search_feild.send_keys(Keys.ENTER)

    # Locate the <a> tag element with the specified class attribute using XPath
    link_element = driver.find_element(By.XPATH,"//a[contains(@class, 'wXeWr') and contains(@class, 'islib') and contains(@class, 'nfEiy')]")

    # Perform click on the element
    link_element.click()

    # Retrieve the href attribute of the <a> tag
    href = link_element.get_attribute("href")
    print(href)

    parsed_url = urllib.parse.urlparse(href)
    query_parameters = urllib.parse.parse_qs(parsed_url.query)

    # Extract the imgurl parameter
    imgurl = query_parameters.get("imgurl")
    imgurl = imgurl[0]

    response = requests.get(imgurl)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Specify the file path where you want to save the image
        file_path =  f"/Users/venkatesh/Desktop/siha/{barcode}.jpg"   # You can change the file name and path as needed

        # Save the image content to a file
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"{barcode} downloaded succesfully")
    else:
        print(f"Failed to download {barcode}. Status code:", response.status_code)
    driver.quit()








# for barcode in barcodes:
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.com/search?q=5285000201168&sca_esv=560946880&tbm=isch&sxsrf=AB5stBi24FB3-HvM3lZXc7ICrUqeHo3rAQ%3A1693299850492&source=hp&biw=1920&bih=995&ei=irTtZIeVG-PHkdUP96OoiAM&iflsig=AD69kcEAAAAAZO3CmjYgqhpcqRhnPykrz3kO7zPj6_kn&ved=0ahUKEwiHgtbAwYGBAxXjY6QEHfcRCjEQ4dUDCAc&uact=5&oq=5285000201168&gs_lp=EgNpbWciDTUyODUwMDAyMDExNjgyBBAjGCdIwQdQ3wRY3wRwAXgAkAEAmAHBAaABwQGqAQMwLjG4AQPIAQD4AQL4AQGKAgtnd3Mtd2l6LWltZ6gCCsICBxAjGOoCGCc&sclient=img")
#
#     search_feild = driver.find_element(By.ID,'REsRA')
#     search_feild.clear()
#     # time.sleep(1)
#     search_feild.send_keys(barcode)
#     search_feild.send_keys(Keys.ENTER)
#
#     div_element = driver.find_element(By.CLASS_NAME,"bRMDJf.islir")
#
#
#     img_element = div_element.find_element(By.TAG_NAME,"img")
#
#
#     data_url = img_element.get_attribute("src")
#
#     data_parts = data_url.split(",")
#     image_data = data_parts[1]
#
#
#     decoded_image_data = base64.b64decode(image_data)
#
#     # CREATE A NEW FOLDER
#     save_path = f"/Users/venkatesh/Desktop/amul/{barcode}.jpg"  # Replace with your desired path and filename
#
#     # Save the image
#     with open(save_path, "wb") as image_file:
#         image_file.write(decoded_image_data)
#
#     print(f"{barcode} downloaded and saved successfully.")
#     driver.quit()mp3rc 2