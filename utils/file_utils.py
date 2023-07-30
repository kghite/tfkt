import time


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


def challenge_directory_path(instance, filename):
    return "challenge/{1}/{0}/{2}".format(
        instance.user.id, time.strftime("%Y%m%d-%H%M%S"), filename
    )
