#!/bin/bash
mv factorial_settings.json factorial_settings.example.json
cp factorial_settings.mine.json factorial_settings.json
python3.9 main_clock_in_till_yesterday.py
mv factorial_settings.example.json factorial_settings.json