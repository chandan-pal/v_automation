FOR /f %%p in ('where python') do SET PYTHONPATH=%%~dpp
SET PATH=%PATH%;%PYTHONPATH%Scripts
pip install selenium

pause