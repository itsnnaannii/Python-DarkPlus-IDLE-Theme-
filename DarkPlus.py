from os import environ, name, system
import time

if name == "nt":
        userProfileName = environ["USERPROFILE"]
        configHighlightFile = open(userProfileName+"\.idlerc\config-highlight.cfg","a+")
        def clscr():
            __ = system("cls")
else:
        print("This program is only intended for Windows. (Enter To Close)\n")
        exit()

while True:
    replaceFonts = input("Replace Fonts? [Y/N]\n> ")
    replaceFonts.upper()
    if replaceFonts == "Y":
        clscr()
        print("Replacing Fonts...")
        time.sleep(1)
        try:
            configMainFile = open(userProfileName+"\.idlerc\config-main.cfg","w")
            configMainFile.write("[Theme]\ndefault = False\nname2 = IDLE Dark\nname = Python DarkPlus\n\n[EditorWindow]\nwidth = 150\nfont = microsoft yahei\nfont-bold = True\nfont-size = 11")
            configMainFile.close()
            clscr()
            print("Fonts Successfully Replaced.")
            time.sleep(1)
            break
        except:
            print("Failed to Replace Fonts.\nIf you believe this is an error, please contact nani via GitHub.\n")
            time.sleep(3)
            break
    elif replaceFonts == "N":
        clscr()
        print("Program will not replace fonts.")
        time.sleep(1)
        break
    else:
        print("Invalid Argument.")
        time.sleep(1)
        clscr()

clscr()
print("Applying Theme...")
time.sleep(1)
try:
    configHighlightFile.write("\n\n[Python DarkPlus]\nnormal-foreground = #00ff00\nnormal-background = #191919\nkeyword-foreground = #ff8000\nkeyword-background = #191919\nbuiltin-foreground = #a800a8\nbuiltin-background = #191919\ncomment-foreground = #c0c0c0\ncomment-background = #191919\nstring-foreground = #378d12\nstring-background = #191919\ndefinition-foreground = #9b9bff\ndefinition-background = #191919\nhilite-foreground = #191919\nhilite-background = #00ff00\nbreak-foreground = #FFFFFF\nbreak-background = #595900\nhit-foreground = #002240\nhit-background = #555555\nerror-foreground = #FFFFFF\nerror-background = #ff0000\ncontext-foreground = #ffffff\ncontext-background = #191919\nlinenumber-foreground = gray\nlinenumber-background = #191919\ncursor-foreground = #ffffff\nstdout-foreground = #ffffff\nstdout-background = #191919\nstderr-foreground = #ffffff\nstderr-background = #ff2f2f\nconsole-foreground = #ffffff\nconsole-background = #191919")
    configHighlightFile.close()
    clscr()
    filler = input("DarkPlus has been added to the IDLE Highlighting Page.\n\nSimply Open Python IDLE, Click 'Options' at the top,\nclick configure IDLE, Highlights and choose 'Python DarkPlus' in the\ncustom themes section.\n\nEnter To Close the Program.\n")
    exit()
except:
    print("Failed to add DarkPlus IDLE Theme.\nForce Quitting.\n")
    time.sleep(3)
    exit()
