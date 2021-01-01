import pyautogui;
import time;
import keyboard;

CANTIDAD_PARTIDAS = 20;


def getImageName(localPgnFile):
    localPgnFile = str(localPgnFile)
    pathArray = localPgnFile.split('/')
    nameWithPNG = pathArray[-1]

    return nameWithPNG

def findImage(localPgnFile):
    imageName = getImageName(localPgnFile);
    print('Searching... ' + imageName)
    pyautogui.moveTo(10, 10)

    xCord = 0
    yCord = 0
    for i in range(4):
        try:
            xCord, yCord = pyautogui.locateCenterOnScreen(localPgnFile);
            print(xCord, yCord);
            print('Found: ' + imageName)
            time.sleep(1)
            break;
        except TypeError:
            print('image not found');

    return xCord, yCord

def findImageAndClick(localPgnFile):
    buttonClicked = False;
    xCord, yCord = findImage(localPgnFile)
    if(xCord != 0 and yCord !=0):
        pyautogui.moveTo(xCord, yCord)
        #pyautogui.click()
        pyautogui.mouseDown();
        time.sleep(1)
        pyautogui.mouseUp()  # does the same thing as a left-button mouse click

        buttonClicked = True;
    return buttonClicked;

def findImageBoolean(localPgnFile):
    imageWasFound = False
    xCord, yCord = findImage(localPgnFile)
    if (xCord != 0 and yCord != 0):
        imageWasFound = True

    return imageWasFound;

def isFindingMatch():
    boolean = findImageBoolean('./Resources/images/Finding_Match_Text.PNG')
    print('match found? : ' + str(boolean))
    return boolean;


def isClientOpen():
    # wait 8 seconds and check if game is loading

    boolean = findImageBoolean('./Resources/images/League_Client_Open_Text.PNG')
    print(boolean)
    return boolean

def waitForStatus3_2():
    initialTime = time.time()
    currentTime = 0;
    while True:

        imageFound = findImageBoolean('./Resources/images/3-2_Stage_Text.PNG')
        if imageFound:
            print('Reached Status 3-2')
            break;
        elif currentTime > 1200:
            break;
        else:
            time.sleep(20)
        currentTime = initialTime - time.time()
        print('waitingFor3-2 Time: ' + str(currentTime))

def surrender():
    #press esc
    time.sleep(3)
    #pyautogui.press('escape')
    keyboard.press('esc')

    findImageAndClick('./Resources/images/Surrender_Button.PNG')
    time.sleep(3)
    findImageAndClick('./Resources/images/Surrender_Button_2.PNG')

def navigateToTFT():
    # Play
    findImageAndClick('./Resources/images/Play_Button.PNG');

    # Go to TFT
    findImageAndClick('./Resources/images/TFT_Button.PNG');

    # Confirm selection
    findImageAndClick('./Resources/images/Confirm_Button.PNG');

def findMatch():
    time.sleep(3)

    while True:
        #Find Match
        boolean = findImageAndClick('./Resources/images/Find_Match_Button.PNG');
        if boolean:
            break;


def waitFormatch():
    # Loop till match is found for n time
    initialTime = time.time()
    print(initialTime)
    timeDiference = 0;


    #Wait for the match popup
    while timeDiference < 1000:

        # if the game is loading breack loop
        if isClientOpen():
            break;

        findImageAndClick('./Resources/images/Accept_Button.PNG');


        timeDiference = time.time() - initialTime;
        print(timeDiference)




def playAgain():
    time.sleep(3)
    while True:

        boolean = findImageAndClick('./Resources/images/Play_Again_Button.PNG')
        if boolean:
            break;

def main():

    numeroPartida = 0;

    navigateToTFT();
    while numeroPartida < CANTIDAD_PARTIDAS:
        print('Partida numero: ' + str(numeroPartida + 1))

        findMatch();

        waitFormatch();

        waitForStatus3_2();

        surrender();

        playAgain();

        numeroPartida = numeroPartida + 1;



#start program

main();
