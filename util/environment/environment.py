import datetime


def before_scenario(context, scenario):
    pass


def after_step(context, step):
    if step.status == 'passed':
        pass
    else:
        try:
            body = context.driver.find_element_by_tag_name('body')
            data = str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f"))
            body.screenshot(data + ".jpg")
        except:
            pass


def after_scenario(context, scenario):
    pass


def before_tag(context, tag):
    pass
