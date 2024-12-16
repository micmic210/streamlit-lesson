import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.calculator import calculator_body

app = MultiPage(app_name = "Ca;ci;atpr App")

app.add_page("Calculator", calculator_body)

app.run()