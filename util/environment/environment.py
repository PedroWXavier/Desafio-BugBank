from datetime import datetime

from selenium.webdriver.common.by import By

from util.driver.driver import driver_start, driver_quit


def before_scenario(context, scenario):
    context.driver = driver_start()


def after_step(context, step):
    print('\n')
    if step.status == 'passed':
        pass
    else:
        try:
            body = context.driver.find_element(By.TAG_NAME, 'body')
            data = str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f"))
            body.screenshot(data + ".jpg")
        except Exception as e:
            print(e)
            pass


def after_scenario(context, scenario):
    driver_quit()


def before_tag(context, tag):
    pass
