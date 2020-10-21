from doclass.hd_math import HdMath
import encodingutf8


if __name__=='__main__':
    try:
        hdmath=HdMath()
        while hdmath.runControl():
            hdmath.loginHD()
            hdmath.getTestId()
            hdmath.doAnswer()
            hdmath.driverQuit()
    except Exception as e:
        print(e)
        hdmath.driverQuit()