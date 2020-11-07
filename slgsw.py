import gspread
from oauth2client.service_account import ServiceAccountCredentials

class slgsw:
    def __init__(self,scp,cred): #scp is the scope, cred is the credentials file (strictly in json)
        self.scope = scp
        self.creds = cred
        creds = ServiceAccountCredentials.from_json_keyfile_name(str(self.creds), self.scope)
        self.client = gspread.authorize(creds) #authorize it

    def open_sheet(self,ws,ws_name):
        if ws_name: #if there is a specific worksheet declared
            self.sheet = self.client.open(str(ws))
            self.ws = self.sheet.worksheet(ws_name) #open the specific work sheet
        else: #if no specific worksheet declared
            print("Insufficient arguments. Make sure the worksheet you are trying to work with is al filled in!")

    def update_cell(self,cell,item): #in cell referencing (A1 notation) format
        self.ws.update_acell(str(cell),item)
        return item#return the written item

    def update_range(self,rng,item): #in cell referencing (A1 notation) format. item variable takes 2d list ([[]]). Full format see read me
        if type(item) is not list:
            print("Invalid argument format! Please check if the value you want to input is in a list! If you want to udpate a single cell's value, please use update_cell instead!")
        self.ws.update(rng,item)
        return item #return the written item list

    def update_format(self,rng,txt,size): #simply formatting a (range of) cell for its font size and text format. rng as cell (range) in cell referncing (A1 notation), txt as format, size as font size
        size = eval(size)
        if txt is not None and size is None:
            self.ws.format(rng, {'textFormat':{txt: True}})
            return f"Set {txt} at {rng}" #return format
        elif txt is None and size is not None:
            self.ws.format(rng, {'textFormat':{"fontSize": size}})
            return f"Set Font size {size} at {rng}" #return format
        elif txt is not None and size is not None:
            self.ws.format(rng, {'textFormat':{"fontSize": size, txt: True}})
            return f"Set {txt} and font size {size} at {rng}" #return format
        else:
            print("Insufficient arguments.")

    def get_cell_value(self,cell): #retrieve a specific cell's value
        item = self.ws.acell(str(cell)).value
        return item

    def get_cell_formula(self,cell): #retrieve a specific cell's formula
        item = self.ws.acell(str(cell),value_render_option='FORMULA').value
        return item

    def get_range(self,rng):
        item = self.ws.batch_get(rng)
        return item

    def find_cell(self,query): #retrieve a cell's position in number format (C,R)
        cell = self.ws.find(query)
        return f"C{cell.col},R{cell.row}"

    def find_cell_list(self,query): #retrieve multiple cell's position in number format (C,R)
        cell = self.ws.findall(query)
        return cell

