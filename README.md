# Payara
Use post-recieve hooks to upload the contents of git repositories to Amazon S3.

## Install
You can use `pip` to install payara easily:

    pip install payara

## Github Setup
To make a Github repo S3 push enabled:

1. Add service hook pointing to Payara server.
2. Make sure your Payara server has pull permissions.

## Running payara
Point payara to your settings module and off you go:

    payara ~/settings.py
