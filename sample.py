# This is an example file.
# You can modify this file to suit your needs

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