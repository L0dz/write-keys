import time
import win32com.client as comclt
class write():
    def __init__(self):
        #VARIABLES
        self.wsh = comclt.Dispatch('WScript.Shell')
        self.text = ''
        self.delay = 0
        self.char_list=['(', ')','{','}','+','%','&','£']

        self.get_inputs()

    def check_char(self,letter):
        #RETURN TRUE IF IT'S A SPECIAL CHARACTER
        for symbol in self.char_list:
            if symbol == letter:
                return True
        return False
        


    def send_keys(self):
        #WAIT 10 SECONDS
        time.sleep(10)

        #WRITE THE TEXT
        for letters in self.text:
            if letters == '\n':
                write='{ENTER}'
            elif self.check_char(letters):  #start the special character check
                write = '{' + letters + '}'                
            else:
                write=letters
            self.wsh.SendKeys(write)
            time.sleep(self.delay)


    def readFile(self):
        #OPEN FILE AND READ IT'S CONTENT
        try:
            file_name = input('File name (with extension) => ')
            with open(file_name, 'r') as f:
                self.text = f.read()
        except Exception as e:
            print('Error: ' + str(e))
            self.get_inputs()


    def get_inputs(self):

        #GET TEXT TO WRITE
        print('Insert the text you want me to print. If you want me to use a text file, just write $ and press enter')
        self.text = input('>>> ')

        #IF YOU WANT TO GET TEXT FROM A FILE
        if(self.text == '$'):
            self.readFile()
            print('Text: \n' + self.text)

        #INSERT DELAY BETWEEN EACH LETTER
        print('Insert the delay you want me to use between each letter (in seconds).  After you will press enter, you\'re gonna have 10 seconds to put the cursor wherever you want me to write.')
        try:
            self.delay = float(input('>>> '))
        except Exception as e:
            print('Input not valid. Error: ' + str(e))
            self.get_inputs()

        self.send_keys()

a = write()