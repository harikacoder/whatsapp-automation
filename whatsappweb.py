from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


directories = ["Text", "Images", "Videos"]
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")

print("Please scan the QR code to log in to WhatsApp Web.")
time.sleep(15)  

def copy_whatsapp_content():
    try:
        
        chat = driver.find_element(By.XPATH, "//span[@title='Chat Title']")  
        chat.click()
        time.sleep(2) 

       
        message = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text")[-1]
        message_text = message.text

        return message_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_text(content):
    with open("Text/message.txt", "a") as file:
        file.write(content + "\n")


def process_content(content):
    if content:
        save_text(content)

def main():
    try:
        while True:
            content = copy_whatsapp_content()
            if content:
                process_content(content)
            time.sleep(5)  
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        driver.quit()


        from selenium.webdriver.common.by import By
import requests

def copy_media_content():
    try:
       
        images = driver.find_elements(By.CSS_SELECTOR, "img")

        for img in images:
            src = img.get_attribute("src")
            if src.startswith("blob:"):
                continue  
            img_data = requests.get(src).content
            with open(f"Images/{os.path.basename(src)}", "wb") as handler:
                handler.write(img_data)

        videos = driver.find_elements(By.CSS_SELECTOR, "video")

        for vid in videos:
            src = vid.get_attribute("src")
            if src.startswith("blob:"):
                continue  
            vid_data = requests.get(src).content
            with open(f"Videos/{os.path.basename(src)}", "wb") as handler:
                handler.write(vid_data)
    except Exception as e:
        print(f"An error occurred while copying media: {e}")

def main():
    try:
        while True:
            copy_media_content()
            time.sleep(5)  
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()


