import base64
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions
import json
import os
import urllib

root_folder = 'ccnt/static/'

class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(20)
    
    def __enter__(self):
        return self.driver
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()
    
    def save(self, URL, filename):
        filename = f'ccnt/{filename}'
        if os.path.exists(root_folder + filename + '.png') and os.path.exists(root_folder + filename + '.pdf'):
            return filename

        print(URL, filename)
        
        try:
            if URL.endswith('.pdf'):
                # only save pdf
                self.driver.get(URL)
                response = urllib.request.urlopen(URL)    
                with open(root_folder + filename + '.pdf', 'wb') as f:
                    f.write(response.read())
            else:
                self.driver.get(URL)
                S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll'+X)
                self.driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                

                # # save as png
                # if not os.path.exists(root_folder + filename + '.png'):
                #     self.driver.get_screenshot_as_file(root_folder + filename + '.png')
                
                # save as pdf
                if not os.path.exists(root_folder + filename + '.pdf'):
                    print_options = PrintOptions()
                    print_options.shrink_to_fit = True
                    with open(root_folder + filename + '.pdf', 'wb') as f:
                        f.write(base64.b64decode(self.driver.print_page(print_options)))
        except Exception as e:
            print(e)
            filename = 'ccnt/default'
        
        return filename
        

def save_as_png(URL, filename):
    filename = f'ccnt/{filename}.png'
    if os.path.exists(root_folder + filename):
        return filename

    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(20)

    print(URL, filename)
    try:
        driver.get(URL)

        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
        driver.get_screenshot_as_file(root_folder + filename)
    except Exception as e:
        print(e)
        filename = 'ccnt/default.png'
        
    driver.quit()

    return filename

def save_as_pdf(URL, filename):
    filename = f'ccnt/{filename}.pdf'
    if os.path.exists(root_folder + filename):
        return filename

    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    print(URL, filename)
    try:
        driver.get(URL)

        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
        
        print_options = PrintOptions()
        print_options.shrink_to_fit = True
        with open(root_folder + filename, 'wb') as f:
            f.write(base64.b64decode(driver.print_page(print_options)))
        
    except Exception as e:
        print(e)
        filename = None
        
    driver.quit()

    return filename
     
# def save_as_pdf(URL, filename):
#     filename = f'ccnt/{filename}.pdf'
#     if os.path.exists(root_folder + filename):
#         return filename
    
#     appState = {
#         "recentDestinations": [
#             {
#                 "id": "Save as PDF",
#                 "origin": "local",
#                 "account": ""
#             }
#         ],
#         "selectedDestinationId": "Save as PDF",
#         "version": 2
#     }

#     print('/Users/ziqing.ye/ccnt_website/' + root_folder + filename)
#     profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
#             'savefile.default_directory': '/Users/ziqing.ye/ccnt_website/' + root_folder + filename}

#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.headless = True
#     chrome_options.add_experimental_option('prefs', profile)
#     chrome_options.add_argument('--kiosk-printing')

#     driver = webdriver.Chrome(options=chrome_options)
#     driver.set_page_load_timeout(20)

#     try:
#         driver.get(URL)
#         driver.execute_script('window.print();')
#     except Exception as e:
#         print(e)
#         filename = None

#     return filename