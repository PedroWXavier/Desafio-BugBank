
import util.environment.environment


def after_scenario(context, scenario):
    return util.environment.environment.after_scenario(context, scenario)


def before_scenario(context, scenario):
    return util.environment.environment.before_scenario(context, scenario)


def after_step(context, step):
    return util.environment.environment.after_step(context, step)


def before_tag(context, tag):
    return util.environment.environment.before_tag(context, tag)
