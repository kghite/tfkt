import time

from PIL import Image


def user_directory_path(instance, filename):
    return "media/user_{0}/{1}".format(instance.user.id, filename)


def challenge_directory_path(instance, filename):
    return "media/challenge/{1}/{0}/{2}".format(
        instance.user.id, time.strftime("%Y%m%d-%H%M%S"), filename
    )


def constrain_profile_images(image_object, max_size):
    img = Image.open(image_object.path)

    if img.height > max_size[1] or img.width > max_size[0]:
        output_size = max_size
        img.thumbnail(output_size)
        img.save(image_object.path)
