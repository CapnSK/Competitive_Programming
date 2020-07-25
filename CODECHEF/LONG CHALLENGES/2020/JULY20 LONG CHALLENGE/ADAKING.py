# import sys
# sys.stdout = open('C:/Users/Acer/Desktop/VsCode(input_output)/Output.txt', 'w')
# sys.stdin = open('C:/Users/Acer/Desktop/VsCode(input_output)/Input.txt', 'r')
import math
testCasesNo=int(input())
for i in range(testCasesNo):
    totalmove=int(input()) #K
    chessBoard=[["." for col in range(8) ]for row in range(8)]
    chessBoard[0][0]="O"
    row=(math.ceil(totalmove/8))
    col=(8 if totalmove%8==0 else totalmove%8)

    for idx in range(8):
        if row < 8 and idx <= col:
            chessBoard[row][idx]="X"
        if col < 8 and idx >= col:
            chessBoard[row-1][idx]="X"      
    for row in chessBoard:
        print(*row,sep='')   