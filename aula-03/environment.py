#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, yaml, json

def read_file(filepath):
    with open(filepath, 'r') as stream:
        if filepath.endswith(".yml"):
            data = yaml.load(stream)
        elif filepath.endswith(".json"):
            data = json.load(stream)
        stream.close()
    return data

def write_file(data, filepath):
    with open(filepath, 'w') as stream:
        if filepath.endswith(".yml"):
            yaml.dump(data, stream, default_flow_style=False)
        elif filepath.endswith(".json"):
            json.dump(data, stream)
        stream.close()

def write_database_file(filepath_prefix, filepath_suffix, environments):
    var_envs = {
        "adapter" : os.environ.get("TEST_ADAPTER"),
        "encoding" : os.environ.get("TEST_ENCODING"),
        "database" : os.environ.get("TEST_DATABASE"),
        "pool" : int(os.environ.get("TEST_POOL")),
        "username" : os.environ.get("TEST_USERNAME"),
        "password" : os.environ.get("TEST_PASSWORD"),
        "port" : int(os.environ.get("TEST_PORT")),
        "host" : os.environ.get("TEST_HOST")
    }
    database = {}
    for env in environments:
        database[env] = var_envs.copy()
        database[env]["database"] = "{database}_{environment}".format(environment=env,**var_envs)
    for suffix in filepath_suffix: 
        write_file(database, filepath_prefix.format(suffix))