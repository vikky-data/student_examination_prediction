import numpy as np
import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker 


engine = create_engine("sqlite.///./student.db")


stuff = "testing"