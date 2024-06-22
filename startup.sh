#!/bin/bash
echo "Starting Gunicorn..."
gunicorn --config gunicorn.py happy_stock_api:app