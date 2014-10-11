import os

from boto.s3.connection import Location, S3Connection
from boto.s3.key import Key

import settings

def get_bucket(bucket_name):
    s3 = S3Connection(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    try:
        return s3.get_bucket(bucket_name)
    except Exception as e:
        if e.error_code != 'NoSuchBucket':
            raise e
        bucket = s3.create_bucket(bucket_name, location=Location.USWest,
                                  policy='public-read')
        bucket.configure_website('index.html', 'error.html')
        return bucket

# Exclude ignored files, extensions
def exclude(file):
    # exclude hidden files
    if file.startswith('.'):
        return True
    # exclude ignored extensions
    if any(file.endswith(ext) for ext in settings.IGNORED_EXTS):
        return True
    # exclude ignored files
    if any(file == ignored for ignored in settings.IGNORED_FILES):
        return True
    # allowed file
    return False

def upload(bucket_name):
    src_dir = os.path.join(settings.REPOS_ROOT, bucket_name)
    bucket = get_bucket(bucket_name)

    # walk src dir and upload files
    for path, dir, files in os.walk(src_dir):
        print 'Uploading...'
        for file in files:
            # get relative path for s3
            rel_path = os.path.relpath(os.path.join(path, file), src_dir)

            # skip hidden folders, ignored extensions
            if exclude(rel_path):
                continue

            # upload file
            print rel_path

            # create key for uploaded file
            k = Key(bucket)
            k.key = rel_path

            # boto will guess content-type and try to set appropriate header for us
            if file.endswith('.json'):
                k.set_contents_from_filename(os.path.join(path, file), headers={'Cache-Control': 'no-cache'})
            else:
                k.set_contents_from_filename(os.path.join(path, file))

            # set public permisssions
            bucket.set_acl('public-read', k.key)
