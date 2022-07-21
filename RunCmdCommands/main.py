import cmd
import subprocess

print('Python Cmd Application')
def runCommands():
    while True:
        try:
            command = input('# ')
            if command.lower() == 'exit':
                print('Bye ')
                break
            subprocess.run(command , shell=cmd)
        except:
            command = input('# ')

runCommands()