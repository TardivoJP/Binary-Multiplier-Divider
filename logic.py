import math

def convertDecimalToBinary(integer):
    binaryValue = ""
    while (integer > 0):
        binaryValue = str(integer % 2) + binaryValue
        integer = integer // 2
    return binaryValue

def convertBinaryArrayToDecimal(binaryArray):
    decimalValue = 0
    
    for i in range(len(binaryArray)):
        if(binaryArray[i] == 1):
            decimalValue += math.pow(2, len(binaryArray)-1-i)
    
    return int(decimalValue)

def generateArr(binaryString):
    binaryArray = [0] * 15
    zeroes = 15 - len(binaryString)
    
    for i in range(zeroes):
        binaryArray[i] = 0
        
    for i in range(len(binaryString)):
        binaryArray[zeroes+i] = int(binaryString[i])
    
    return binaryArray

def binarySum(binaryArrayA, binaryArrayB):
    binaryArraySum = []
    carryOut = 0
    
    for i in reversed(range(len(binaryArrayA))):
        total = binaryArrayA[i] + binaryArrayB[i] + carryOut
        binaryArraySum.insert(0, total % 2)
        carryOut = total // 2
    
    return binaryArraySum, carryOut

def twoComplement(binaryArray):
    complement = [0] * len(binaryArray)
    oneArray = [0] * len(binaryArray)
    oneArray[len(binaryArray) - 1] = 1
    
    for i in range(len(binaryArray)):
        if (binaryArray[i] == 0):
            complement[i] = 1
        else:
            complement[i] = 0
    
    complement, carryOut = binarySum(complement, oneArray)
    
    return complement

def shiftRight(carryOut, binaryArrayA, binaryArrayB):
    transferredValue = 0
    
    for i in reversed(range(len(binaryArrayA))):
        if(i == len(binaryArrayA) - 1):
            transferredValue = binaryArrayA[i]
        
        if(i > 0):
            binaryArrayA[i] = binaryArrayA[i-1]
        else:
            binaryArrayA[i] = carryOut
            
    for i in reversed(range(len(binaryArrayB))):
        if(i > 0):
            binaryArrayB[i] = binaryArrayB[i-1]
        else:
            binaryArrayB[i] = transferredValue
    
    return binaryArrayA, binaryArrayB

def shiftLeft(binaryArrayA, binaryArrayB):
    transferredValue = 0
    
    for i in range(len(binaryArrayB)):
        if(i == 0):
            transferredValue = binaryArrayB[i]
        
        if(i < len(binaryArrayB) - 1):
            binaryArrayB[i] = binaryArrayB[i+1]
        else:
            binaryArrayB[i] = 0
            
    for i in range(len(binaryArrayA)):
        if(i < len(binaryArrayA) - 1):
            binaryArrayA[i] = binaryArrayA[i+1]
        else:
            binaryArrayA[i] = transferredValue
            
    return binaryArrayA, binaryArrayB

def binaryMultiply(binaryArrayA, binaryArrayB):
    log = []
    carryOut = 0
    varA = [0] * len(binaryArrayA)
    varM = binaryArrayA
    varQ = binaryArrayB
    result = [0] * (len(binaryArrayA) + len(binaryArrayB))
    
    for i in range(len(binaryArrayA)):
        log.append("================================================")
        log.append("Inicio da iteracao")
        log.append("Contador: "+str(15-i))
        log.append("Q0: "+str(varQ[len(varQ)-1]))
        log.append("C: "+str(carryOut))
        log.append("A: "+str(varA))
        log.append("Q: "+str(varQ))
        
        if(varQ[len(varQ)-1] == 1):
            varA, carryOut = binarySum(varA, varM)
            log.append("Apos soma")
            log.append("C: "+str(carryOut))
            log.append("A: "+str(varA))
            
        varA, varQ = shiftRight(carryOut, varA, varQ)
        carryOut = 0
        
        log.append("Apos deslocamento")
        log.append("C: "+str(carryOut))
        log.append("A: "+str(varA))
        log.append("Q: "+str(varQ))

    for i in range(len(varA)):
        result[i] = varA[i]
        
    for i in range(len(varQ)):
        result[i+len(varA)] = varQ[i]
        
    log.append("================================================")
    log.append("Final da operacao")
    log.append("Q0: "+str(varQ[len(varQ)-1]))
    log.append("C: "+str(carryOut))
    log.append("A: "+str(varA))
    log.append("Q: "+str(varQ))
    log.append("M: "+str(varQ))
    log.append("Resultado em binario: "+str(result))
    log.append("Resultado em decimal: "+str(convertBinaryArrayToDecimal(result)))
    log.append("================================================")
        
    return result, log

def binaryDivide(binaryArrayA, binaryArrayB):
    log = []
    varA = [0] * len(binaryArrayA)
    varM = binaryArrayA
    varMTwoComplement = twoComplement(varM)
    varQ = binaryArrayB
    
    for i in range(len(binaryArrayA)):
        log.append("================================================")
        log.append("Inicio da iteracao")
        log.append("Contador: "+str(15-i))
        log.append("Q0: "+str(varQ[len(varQ)-1]))
        log.append("A: "+str(varA))
        log.append("Q: "+str(varQ))
        
        varA, varQ = shiftLeft(varA, varQ)
        log.append("Apos deslocamento")
        log.append("Q0: "+str(varQ[len(varQ)-1]))
        log.append("A: "+str(varA))
        log.append("Q: "+str(varQ))
        
        varA, carryOut = binarySum(varA, varMTwoComplement)
        log.append("Apos subtracao (soma com complemento de 2)")
        log.append("A: "+str(varA))
        
        if(varA[0] == 1):
            varQ[len(varQ)-1] = 0
            varA, carryOut = binarySum(varA, varM)
            log.append("A < 0")
            log.append("Apos soma")
            log.append("Q0: "+str(varQ[len(varQ)-1]))
            log.append("A: "+str(varA))
            log.append("Q: "+str(varQ))
        else:
            varQ[len(varQ)-1] = 1
            log.append("A > 0")
            log.append("Q0: "+str(varQ[len(varQ)-1]))
            log.append("Q: "+str(varQ))
            
    log.append("================================================")
    log.append("Final da operacao")
    log.append("Q0: "+str(varQ[len(varQ)-1]))
    log.append("M: "+str(varQ))
    log.append("Quociente em binario: "+str(varQ))
    log.append("Quociente em decimal: "+str(convertBinaryArrayToDecimal(varQ)))
    log.append("Resto em binario: "+str(varA))
    log.append("Resto em decimal: "+str(convertBinaryArrayToDecimal(varA)))
    log.append("================================================")
        
    return varQ, varA, log