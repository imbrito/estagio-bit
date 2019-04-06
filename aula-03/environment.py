#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, yaml, json

def read_file(filepath):
    with open(filepath, 'r') as stream:
        if filepath.endswith(".yml"):
            data = yaml.load(stream, Loader=yaml.FullLoader)
        elif filepath.endswith(".json"):
            data = json.load(stream)
        stream.close()
    return data

def write_file(data, filepath):
    with open(filepath, 'w') as stream:
        if filepath.endswith(".yml"):
            yaml.dump(data, stream)
        elif filepath.endswith(".json"):
            json.dump(data, stream)
        stream.close()

def write_database_file(filepath):
    data = {}
    data["adapter"] = os.environ.get("TEST_ADAPTER")
    data["encoding"] = os.environ.get("TEST_ENCODING")
    data["database"] = os.environ.get("TEST_DATABASE")
    data["pool"] = int(os.environ.get("TEST_POOL"))
    data["username"] = os.environ.get("TEST_USERNAME")
    data["password"] = os.environ.get("TEST_PASSWORD")
    data["port"] = int(os.environ.get("TEST_PORT"))
    data["host"] = os.environ.get("TEST_HOST")
    write_file(data, filepath)