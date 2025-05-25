#!/bin/bash
pip install -r requirements.txt
export $(cat .env | xargs)
python main.py
