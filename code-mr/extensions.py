# -*- coding: utf-8 -*-

import sanic as sanic
import redis as redis
import uvloop as uvloop
import asyncio as asyncio
from sanic import Blueprint as Blueprint
from sanic.response import json as resjson
from sanic.config import LOGGING as LOGGING
from pymongo import MongoClient as MongoClient
import pyodbc as dbcn
import datetime as datetime,time as time
import json as jsonad
from rq import Queue