import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')

def create_thumbnail(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((128, 128))
        image.save(resized_path)

def blog_friendly_resize(image_path, resized_path):
    with Image.open(image_path) as image:
        og_width, og_height = image.size
        new_width = 500
        new_height = (og_width / new_width) * og_height
        image.resize(new_width, new_height)
        image.save(resized_path)

def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        thumbnail_path = '/tmp/resized-{}'.format(key)
        blog_friendly_path = '/tmp/blog-{}'.format(key)

        s3_client.download_file(bucket, key, download_path)
        create_thumbnail(download_path, thumbnail_path)
        s3_client.upload_file(thumbnail_path, '{}-resized'.format(bucket), key)
        s3_client.upload_file(blog_friendly_path, '{}-blog-friendly'.format(bucket), key)
