# Net Worth Dashboard (Under development)
This is a Python Dashboard made with Plotly Dash to show you some statistics based on your daily incomings and expenses

# Installation
You just have to install all the modules in the 'requirements.txt' file by launching the following command:
```console
foo@bar:~$ pip install -r /networth_dashboard/requirements.txt
```
# Basic configuration
In order to use the dashboard you have to create a file named 'mynetworth.csv' under /networth_dashboard/csv/. The file must contain the following columns to be populated by your data: 
|Date      |Incomings|Expenses|Categories|Notes              |
|----------|---------|--------|----------|-------------------|
|2023-01-01|13546    |        |          |Salary of December |
|2023-01-02|         |45      |Food      |Restaurant with GF |
|2023-01-02|         |31      |Other     |Shopping with Elia |

The categories available are the following:
- Clothes
- Food 
- Other 
- Amazon 
- Bar 
- Gas
- Medicines
- Home
- Friends
- Presents
- Technology
- Phone
- Transport
- Vacation
