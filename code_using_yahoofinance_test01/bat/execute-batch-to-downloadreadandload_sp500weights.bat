:::::::
:: Pull

@echo off
C:\Anaconda\python.exe "C:\Batches\AutomationProjects\EfficientFrontier\code_using_yahoofinance_test01\py\good_downloadandread_sp500weightsassymbols.py" %*

:: Load
C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe "C:\Batches\AutomationProjects\EfficientFrontier\code_using_yahoofinance_test01\bat\run-sql-script.ps1"

