import vlab

class CommandProcessor():
    def command_c(self):
        print "continue command"
    def command_pause(self):
        print "Exec in pause()"
        
    def command_CAN(self):
        print "This is can sender prototype"

    def command_LIN(self):
        print "This is lin sender prototype"

    def command_UART(self):
        print "This is uart_sender prototype"
    def command_ASTC(self):
        print "Hi from ASTC Design Partners"

    def command_not_found(self, command):
        print command

    def command_Colombia(self):
        print "Colombia, those are your arguments"
        for arg in self.argv:
            print arg
    
    def exec_command(self, command_):
        self.argv = command_.split(" ")
        command = "command_" + self.argv[0]
        print command
        self.kwargs = {}
        
        try: 
            method = getattr(self, command)
            # get keys and values
            for arg in self.argv:
                try:
                    splitted = arg.split('=')
                    self.kwargs[splitted[0]] = splitted[1]
                except: pass
            print self.kwargs
            return method()
        #AttributeError: 'hybrid_node' object has no attribute 'command_!ASTC'
        except AttributeError:
            self.command_not_found(command)
        except Exception as e:
            print "Error: ", e   
        
if __name__ == "__main__":
    ex = CommandProcessor()
    command = "CAN 0x238 --random"
    ex.exec_command(command)
    command = "CA1N 0x238 --random"
    ex.exec_command(command)
    command = "LIN 0x238 --random"
    ex.exec_command(command)