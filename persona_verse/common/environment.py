# -*- coding: utf-8 -*-
import os

from dotenv import dotenv_values

env = dotenv_values(dotenv_path=os.path.join(".env"), verbose=True)

__all__ = ["env"]
