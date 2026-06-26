#!/bin/bash
echo "Setting up ERP-AI Platform..."
pip install -r requirements.txt
alembic upgrade head