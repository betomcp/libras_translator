# RIGHT HAND LETTERS
def checkRightA(points):
    if(points[4][1] < points[8][1] 
        and points[4][1] < points[12][1] 
        and points[4][1] < points[16][1] 
        and points[4][1] < points[20][1]
        and points[4][0] > points[8][0]
        and points[8][0] > points[16][0]
        and points[16][0] > points[20][0]
        and points[4][0] > points[3][0] - 10
        and points[4][0] < points[3][0] + 10):
        return True
    return False

def checkRightB(points):
    if(points[4][0] < points[3][0]
       and points[3][0] < points[2][0]
       and points[4][0] < points[5][0]
       and points[4][1] > points[8][1]
       and points[4][1] > points[12][1]
       and points[4][1] > points[16][1]
       and points[4][1] > points[20][1]
       and points[5][1] > points[6][1]
       and points[6][1] > points[7][1]
       and points[7][1] > points[8][1]
       and points[9][1] > points[10][1]
       and points[10][1] > points[11][1]
       and points[11][1] > points[12][1]
       and points[13][1] > points[14][1]
       and points[14][1] > points[15][1]
       and points[15][1] > points[16][1]
       and points[17][1] > points[18][1]
       and points[18][1] > points[19][1]
       and points[19][1] > points[20][1]):
        return True
    return False

def checkRightC(points):
    if(points[4][0] > points[3][0]
       and points[3][0] > points[2][0]
       and points[2][0] > points[1][0]
       and points[8][0] > points[2][0]
       and points[12][0] > points[2][0]
       and points[16][0] > points[2][0]
       and points[20][0] > points[2][0] - 20
       and points[8][0] > points[7][0]
       and points[7][0] > points[6][0]
       and points[6][0] > points[5][0]
       and points[12][0] > points[11][0]
       and points[11][0] > points[10][0]
       and points[10][0] > points[9][0]
       and points[16][0] > points[15][0]
       and points[15][0] > points[14][0]
       and points[14][0] > points[13][0]
       and points[20][0] > points[19][0]
       and points[19][0] > points[18][0]
       and points[18][0] > points[17][0]
       and points[8][1] > points[4][1] - 120
       and points[12][1] > points[4][1] - 120
       and points[16][1] > points[4][1] - 120
       and points[20][1] > points[4][1] - 120
       and points[8][1] < points[4][1] - 27
       and points[12][1] < points[4][1] - 27
       and points[16][1] < points[4][1] - 27
       and points[20][1] < points[4][1] - 27
       and points[8][1] < points[5][1]
       and points[12][1] < points[9][1]
       and points[16][1] < points[13][1]
       and points[20][1] < points[17][1]
       and points[1][0] < points[4][0] - 20):
        return True
    return False

def checkRightO(points):
    if(points[4][0] > points[3][0]
       and points[3][0] > points[2][0]
       and points[2][0] > points[1][0]
       and points[8][0] > points[2][0]
       and points[12][0] > points[2][0]
       and points[16][0] > points[2][0]
       and points[20][0] > points[2][0] - 20
       and points[8][0] > points[7][0]
       and points[7][0] > points[6][0]
       and points[6][0] > points[5][0]
       and points[12][0] > points[11][0]
       and points[11][0] > points[10][0]
       and points[10][0] > points[9][0]
       and points[16][0] > points[15][0]
       and points[15][0] > points[14][0]
       and points[14][0] > points[13][0]
       and points[20][0] > points[19][0]
       and points[19][0] > points[18][0]
       and points[18][0] > points[17][0]
       and points[20][1] < points[4][1] + 8
       and points[16][1] < points[4][1] + 8
       and points[12][1] < points[4][1] + 8
       and points[8][1] < points[4][1] + 8
       and points[16][1] > points[4][1] - 15
       and points[12][1] > points[4][1] - 15
       and points[8][1] > points[4][1] - 15
       and points[4][0] < points[16][0] + 100
       and points[4][0] < points[12][0] + 100
       and points[4][0] < points[18][0] + 100
    ):
        return True
    return False

def checkRightE(points):
    if(points[4][0] < points[3][0]
       and points[3][0] < points[2][0]
       and points[20][1] > points[18][1]
       and points[16][1] > points[14][1]
       and points[12][1] > points[10][1]
       and points[8][1] > points[6][1]
       and points[4][1] > points[19][1] - 22
       and points[4][1] > points[15][1] - 22
       and points[4][1] > points[11][1] - 22
       and points[4][1] > points[7][1] - 22
       and points[4][0] < points[12][0]
       and points[4][0] < points[16][0] + 10):
        return True
    return False

def checkRightF(points):
    if(points[20][1] < points[19][1]
       and points[19][1] < points[18][1]
       and points[18][1] < points[17][1]
       and points[16][1] < points[15][1]
       and points[15][1] < points[14][1]
       and points[14][1] < points[13][1]
       and points[12][1] < points[11][1]
       and points[11][1] < points[10][1]
       and points[10][1] < points[9][1]
       and points[6][1] < points[8][1]
       and points[4][1] < points[3][1]
       and points[8][1] > points[4][1] - 30
       and points[8][1] <= points[4][1] + 23
       and points[4][0] > points[5][0]
       and points[4][0] > points[8][0] - 30
       and points[4][0] < points[8][0] + 30
       and points[8][0] > points[12][0]
       and points[12][0] > points[16][0]
       and points[16][0] > points[20][0]
       ):
        return True
    return False

def checkRightI(points):
    if(points[20][1] < points[16][1]
       and points[20][1] < points[12][1]
       and points[20][1] < points[8][1]
       and points[20][1] < points[4][1]
       and points[4][0] < points[3][0]
       and points[20][1] < points[19][1]
       and points[20][1] < points[18][1] - 8
       and points[20][1] < points[17][1]
       and points[14][1] < points[16][1]
       and points[10][1] < points[12][1]
       and points[6][1] < points[8][1]
       and points[4][1] < points[16][1]
       and points[4][1] < points[12][1]
       ):
        return True
    return False

def checkRightU(points):
    if(points[8][1] < points[7][1]
       and points[7][1] < points[6][1]
       and points[6][1] < points[5][1]
       and points[12][1] < points[11][1]
       and points[11][1] < points[10][1]
       and points[10][1] < points[9][1]
       and points[12][0] < points[8][0]
       and points[4][0] < points[3][0]
       and points[4][0] < points[5][0]
       and points[4][1] < points[20][1]
       and points[4][1] < points[16][1]
       and points[14][1] < points[20][1]
       and points[18][1] < points[16][1]
       and points[20][0] < points[16][0]
       and points[12][1] < points[8][1]
       and points[8][0] - points[12][0] < 25
       ):
        return True
    return False


#MAIN FUNC
def translate(points):
    #RIGHT HAND
    if(points[1][0] > points[0][0]):
        #A
        if(checkRightA(points)):
            return 'A'
        #B
        if(checkRightB(points)):
            return 'B'
        #C
        if(checkRightC(points)):
            return 'C'
        #E
        if(checkRightE(points)):
            return 'E'
        #I
        if(checkRightI(points)):
            return 'I'
        #O
        if(checkRightO(points)):
            return 'O'
        #F
        if(checkRightF(points)):
            return 'F'
        #U
        if(checkRightU(points)):
            return 'U'     