import gspread
from gspread import utils
from oauth2client.service_account import ServiceAccountCredentials

from typing import Union


class slgsw:
    def __init__(self, cred, scp: str = ('https://www.googleapis.com/auth/spreadsheets.readonly')):  # scp is the scope, cred is the credentials file (strictly in json). defaults to read on access
        self.scope = scp
        self.creds = cred
        creds = ServiceAccountCredentials.from_json_keyfile_name(str(self.creds), self.scope)
        self.client = gspread.authorize(creds)  # authorize it

    def open_sheet(self, sp: str, ws_name: str = None):
        self.sheet = self.client.open(sp)
        if ws_name is not None:
            self.ws = self.sheet.worksheet(ws_name)  # open the specific work sheet
        else:
            self.ws = self.client.open(sp).sheet1

    def update_cell(self, cell: str, item):  # in cell referencing (A1 notation) format
        if list(cell)[0].isalpha():
            self.ws.update_acell(str(cell), item)
            return item  # return the written item
        else:
            raise ValueError("Cell parameter expects A1 notation!")

    def update_range(self, rng: list, item):  # in cell referencing (A1 notation) format. item variable takes 2d list ([[]]). Full format see read me
        if type(item) is not list:
            raise SyntaxError(
                "Invalid argument format! Please check if the value you want to input is in a list! If you want to udpate a single cell's value, please use update_cell instead!")
        else:
            self.ws.update(rng, item)
            return item  # return the written item list

    def update_format(self, rng: list,
                      txt: str = None,
                      size: Union[int, float] = None,
                      fontFamily: str = None,
                      numFormat=None,
                      numPattern=None) -> str:  # simply formatting a (range of) cell for its font size and text format. rng as cell (range) in cell referncing (A1 notation), txt as format, size as font size
        '''
        Important: the update_format function will reset the cell's format first, then apply the format!
        '''
        flag = False
        if str(txt).lower() is not None and str(txt).lower() in ['bold', 'italic', 'strikethrough', 'underline']:  # check for valid input
            flag = True
        elif txt is not None:
            raise SyntaxError("Invalid argument format! Please check if the value you inputted in valid (eg: textFormat needs to be either 'bold','italic','strikethrough', or 'underline') !")

        if flag == True:
            self.ws.format(rng, {'numberFormat': {'type': numFormat, 'pattern': numPattern},
                                 'textFormat': {'fontFamily': fontFamily, 'fontSize': size, txt: True}})
        else:
            self.ws.format(rng, {'numberFormat': {'type': numFormat, 'pattern': numPattern},
                                 'textFormat': {'fontFamily': fontFamily, 'fontSize': size}})

        return f'At cell {rng} : text format "{txt}", Size {size}, font family "{fontFamily}", number format "{numFormat}" with pattern "{numPattern}"'

    def get_cell_value(self, cell: str):  # retrieve a specific cell's value
        if list(cell)[0].isalpha():
            item = self.ws.acell(str(cell)).value
            return item
        else:
            raise ValueError("Cell parameter expects A1 notation!")

    def get_cell_formula(self, cell: str):  # retrieve a specific cell's formula
        if list(cell)[0].isalpha():
            item = self.ws.acell(str(cell), value_render_option='FORMULA').value
            return item
        else:
            raise ValueError("Cell parameter expects A1 notation!")

    def get_range(self, rng: list):  # retrieve a range of values
        item = self.ws.batch_get(rng)
        return item

    def find_cell(self, query) -> list:  # retrieve one or more cell's position in A1 notation
        cell = self.ws.findall(query)
        for i in range(len(cell)):
            cell[i] = utils.rowcol_to_a1(cell[i].row, cell[i].col)
        return cell