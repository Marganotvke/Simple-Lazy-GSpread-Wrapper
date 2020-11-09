# Simple-Lazy-GSpread-Wrapper
A simple wrapper for gspread for people who have limited programming experience, or just simply too lazy to read the gspread docs.
<br>Provides some simple functions for ordinary daily use cases. 
<br>
### Installation
First, install the dependencies of the module (which are gspread and oauth2client):

    pip install gspread oauth2client

Then, you can install this module by typing:
    
    pip install git+https://github.com/Marganotvke/Simple-Lazy-GSpread-Wrapper#egg=slgsw
If you have trouble installing this module, or just simply do not want to install it, you can also just clone the module in the 'slgsw' directory and put the module into your project's directory.

#### Importing
Importing the module is easy, all you need to do is just type in the first line:
    
    from slgsw import slgsw

or:

    import slgsw.slgsw

Alternatively, you can do:

    import slgsw

If you know what you are doing. 

### Functions
Here is a list of functions that this module provide, in the format of function(argument(s)):
* slgsw(scope,cred)
    <br> This is the initialization function of this module for Authentication.
    <br> Scope: you will need to fill in the list of 'powers' the service accounts have access to, in the form of a list. eg:
        
        scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

    A full list of scopes is available in the gspread api docs, however in most cases, https://www.googleapis.com/auth/spreadsheets (allows for read/write of spreadsheets) and https://www.googleapis.com/auth/drive (allow for access of google drive) is enough.
    <br><br>credentials: you will need to fill the the name (or the path) of the credentials file you downloaded from google's api control panel. Full instructions can be found here:https://gspread.readthedocs.io/en/latest/oauth2.html#enable-api-access-for-a-project
    <br>The format is in a string (double or single quotes, "" | ''), and the file's format MUST be in json, eg:
        
        'credentials.json'
    
    Absolute path referencing or relative path referencing is also fine for this argument.

    Do keep in mind that you will need to set a variable to save what this function returns, to later for the other functions to reference to. eg:
        
        sheet = slgsw(scope,creds)

* sheet.open_sheet(sp,ws)
    <br>To open and start working on a single worksheet or a spreadsheet. The starting 'sheet' is the variable we mentioned in the initial function 'slgsw()' that saves all authenticating results.
    <br><br>sp: The name of the spreadsheet you want to work with. eg:
    
       "Example Spreadsheet"
    Space is allowed, as there are spreadsheets with space in between characters.
    <br><br>ws: The name of the worksheet you want to work on, in another words, the name of the sheet within the big sheet you want to work on .
    <br><br>Currently it needs both the sheet and worksheet name to work, even if there's only one worksheet.
    
*   sheet.update_cell(cell,item)
    <br>To update a cell's value or formula.
    <br><br>cell: The cell's locaiton you are referencing to. Take cell referencing (A1 notation). eg:
        
        "A1"
        
    <br>item: The stuff you want to put in the cell. Can be words (string) or numbers (numeric). eg:
        
        13
        "Hello!"
    This function will return the value you just updated to the sheet, so you can also save the value by assigning a variable to it, eg:
    
        x = sheet.update_cell("A1","Hello!")
        print(x)
        # will print Hello!
    Do keep in mind that this function only supports one cell at a time. If you want to update multiuple cells at once, you can use:

*   sheet.update_range(rng,item)
    <br> Will update a range of cell at once.
    <br><br>rng: The range of cells, eg:
        
        "A1:B2"
        
    <br>item: The stuff you want to put in this range of cells.
    <br> Please do keep in mind that this only takes in a 'lists within a list'. eg:
    
        data = [[1],[2]]
    The way the function will write in is:
    1. The first list within the list into the first referenced row. eg:
        
            data = [[1,2],[3,4]]
            #for "A1:B2",
            #it will write [1,2] into A1:B1
    2. The second list within the list into the second referenced row. eg:
            
            data = [[1,2],[3,4]]
            #for "A1:B2",
            #it will write [3,4] into A2:B2
            
    So on and so forth.
   
*   sheet.update_format(cell,txt,size)
    <br> To change the format of a (range of) cell. This currently only supports text formatting and font size, if you want some other advance formatting, please refer to the gspread api docs instead. (https://gspread.readthedocs.io/en/latest/user-guide.html#formatting , https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#cellformat)
    <br><br>rng: The range of cells you want to change the format of. Can be a single cell ("A1") or a range ("A1:B2").
    <br><br>txt: The format of the texts. Currently supports:
        
        bold,italic,strikethrough,underline
    <br>size: The size of texts. Takes a number only, eg: 12
    <br><br>If you want to just use one of the parameters, you can just use either 'txt=something' or 'size=something'. eg:
        
        sheet.update_format('A1',size=15)

*   sheet.get_cell_value(cell)
    <br> To retrieve a cell's value. Takes cell referencing (A1 notaiton), eg:
        
        x = sheet.get_cell_value("A1")
        print(x)
        # will print "Hello!" 
    Do keep in mind that it will return the value, not the formula, therefore if the cell is a formula, it will return the result, not the formula. eg:
    
        # theres a formula "=now()" in A1
        x = sheet.get_cell_formula("A1")
        print(x)
        #will print 20/04/2020 16:20:39 instead of "=now()"
    If you want to retrieve the formula, use the following function:
    
*   sheet.get_cell_formula(cell)  
    <br> To retrieve a cell's formula instead of its value. Takes cell referencing (A1 notaiton), eg:
        
        # theres a formula =now() in A1
        x = sheet.get_cell_formula("A1")
        print(x)
        #will print =now() insted of 20/04/2020 16:20:39
        
*   sheet.get_range(rng)
    <br>It will return a list of the cells you specified.
    <br>rng:Takes the cell range of the spreadsheet. Takes in cell referencing (A1 notation). eg:
        
        "A1:B2"
    It can also take multiple values, just use a list to hold them together. eg"
        
        cell_range = ["A1:B2","C3"]
    Do keep in mind that it will return in a multi-list form, in another words, the 'lists within a list' form.
    
*   sheet.find_cell(query)
    <br>To find the location of a cell that contains the value that you want to find. It returns in numbering format (C1R1). eg:
        
        x = sheet.find_cell("Hello!")
        print(x)
        #will print "C1,R1"
    Do keep in mind that it will only return the FIRST result. If you want to find more cells that fit the same value, you can try the following:
    
*   sheet.find_cell_list(query)
    <br>To find the location of a list of cells that contains the value that you want to find. It currently returns in raw cell format (<Cell R1C1 'value'>). eg:
        
        # "Hello!" at A1, A2
        x = sheet.find_cell_list("Hello!")
        print(x)
        #will print [<Cell R1C1 'Hello!'>, <Cell R2C1 'Hello!'>]
    
### Usage and examples
The following is an example that I put up. You can also find the example file in the repository:
    
    # You can modify this code to suit your needs
    
    from slgsw import * #import the module
    # if you choose to use 'import' only, then you will need to add 'slgsw.' in front of every single functions
    # for example, to initialize the function you will need to use 'slgsw.slgsw(blah,blah)' instead of just 'slgsw(blah,blah)'
    
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] # defining the scope. see read me for detail
    cred = "credentials.json" # defining the credential's file name
    
    # authorize the worksheet!
    ws = slgsw(scope,cred)
    # lets open an worksheet by using open_worksheet with the authorized credentials 'ws'.
    ws.open_sheet('Example','Example_ws_1') # 'variable'.'functions(arguments)' all other functions uses the same format
    
    # lets update a cell with a new value!
    x = ws.update_cell('A1','This is an example.')
    # the first argument is the cell's name in cell referncing (A1 notation), the second argument is the stuff you want to put in
    # you can either put a string ("words with quotes") or numerics (numbers only) in the second argument
    
    print(x)
    # here's the value we just updated. every update functions in this module will return the updated value you just put in (except formatting)
    
    # lets check our cell to see if it's updated
    y = ws.get_cell_value('A1')
    print(y)
    # looks like it updated correctly, hooray
    
    # that's it, you now know the basics of this module
    # do keep in mind that not all functions takes the same format for the same arguments, read the read me files before you go!

If you requires more complex functions, please refer to the gspread api docs and learn the apis yourself. Thank you.
<br> https://gspread.readthedocs.io/en/latest/index.html

### Todo
* Add fontFamily support for update_format
* Add numberingFormat support for update_format
* Make default of open_sheet to open first worksheet
* Fix the formatting in find_cell_list

### Other Stuff
This is my first wrapper and also my first public git repository. Kinda excited about this.
<br> Was kinda frustrated to use the gspread api, therefore wrote this wrapper to make it just a tiny bit user-friendly.
<br> Writing the read me takes more time than to actually write and debug the actual code lol.
<br> Feel free to pull request or whatever! I will check them if I have the time.
>gspread is copyrighted by Anton Burnashev.
