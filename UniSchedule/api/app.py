from app import app
from flask import Flask

# Vercel requires this serverless function
def handler(request, response):
    return app(request, response)