import sys,os
# Get the absolute path of the current directory
current_dir = os.path.abspath(os.path.dirname(__file__))
# Get the absolute path of the Parent Directory (one level above)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
# Append the Parent Directory to sys.path if it's not already there
if parent_dir not in sys.path:
    sys.path.append(parent_dir)