import hashlib
from comfy.cli_args import args
from PIL import ImageFile, UnidentifiedImageError


def conditioning_set_values(conditioning, values=None):
    if values is None:
        values = {}

    return [
        [t[0], {**t[1], **values}] for t in conditioning
    ]


def pillow(fn, arg):
    try:
        return fn(arg)
    except (OSError, UnidentifiedImageError, ValueError):  # PIL issues
        prev_value = ImageFile.LOAD_TRUNCATED_IMAGES
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        return fn(arg)
    finally:
        ImageFile.LOAD_TRUNCATED_IMAGES = prev_value


def hasher():
    hashfuncs = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }
    return hashfuncs.get(args.default_hashing_function)
