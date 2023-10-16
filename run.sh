#!/usr/bin/env sh
git pull
redis-cli FLUSHALL
sudo python3 -m uvicorn run:app --host 0.0.0.0 --proxy-headers &