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
        
    def vs_send_keys(self):
        letter_index = 0
        write=''
        #WRITE THE TEXT
        for letters in self.text:
            
            #Adjust indentation
            try:
                if letters == '<':
                    if self.text[letter_index-1] == '\n' and self.text[letter_index+1] == '/':
                        self.wsh.SendKeys('{DELETE}')
            except Exception as e:
                print(str(e))
            
            #Select which character to write
            if letters == '\n':
                write='{ENTER}'
            elif self.check_char(letters):  #start the special character check
                write = '{' + letters + '}'                
            elif letters==' ' and self.text[letter_index-1] == '\n' or letters==' ' and write=='': #fix indentation issue
                write=''
            else:
                write=letters

            #fix auto-compleatation issue
            try:
                if (self.text[letter_index+1] == '\n'):
                    write+=' {DELETE}'
            except Exception as e:
                print(str(e))

            #actually send keys
            self.wsh.SendKeys(write)
            time.sleep(self.delay)
            letter_index+=1

    def send_keys(self):

        #Select which character to write
        for letters in self.text:
            if letters == '\n':
                write='{ENTER}'
            elif self.check_char(letters):  #start the special character check
                write = '{' + letters + '}'               
            else:
                write=letters

            #actually send keys
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
        print('Insert the delay you want me to use between each letter (in seconds).')
        try:
            self.delay = float(input('>>> '))
        except Exception as e:
            print('Input not valid. Error: ' + str(e))
            self.get_inputs()

        #DO YOU WANT TO WRITE IN VS MODE?
        print('Do you want to write it in vs code mode?(tested on html, css. It might work in other programming languages but it\'s not tested) \nImportant: If you select yes, before to start go to File>Preferences>Settings>Extensions>HTML and disable auto-closing tags\n(y/n)')
        vs_mode=input('>>> ')


        print('How many seconds do you need to put the cursor in the right place? (Countdown will start after you insert the seconds and press enter)')
        wait=input('>>> ')

        #wait time to make the user position the cursor
        try:
            time.sleep(float(wait))
        except Exception as e:
            print('Error: ' + str(e))
            self.get_inputs() 

        #SEND KEYS
        if(vs_mode.lower() == 'y' or vs_mode.lower() == 'yes'):
            self.vs_send_keys()
        elif(vs_mode.lower() == 'n' or vs_mode.lower() == 'no'):
            self.send_keys()
        else:
            print('Error: command not valid')
            self.get_inputs()
            

a = write()