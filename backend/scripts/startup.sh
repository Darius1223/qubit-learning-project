#!/bin/bash

echo "Start web application"

uvicorn --reload  --host="0.0.0.0" src.main:app