; Austen Edge: aedg256 
;
; Initialization
;
		.ORIG	x3000
		LD		R6, EMPTY		; R6 is the stack pointer
		LD		R5, PTR			; R5 is pointer to characters
		AND		R0, R0,	#0
		ADD		R0, R0,	#10		; Print a new line
		OUT
		
		LDR		R3, R5, #0		; R3 gets the first character
		NOT		R3, R3
		ADD		R3, R3, #1
		AND		R4, R4, #0		; R4 stores the operation type
		LD		R0, PLUS		; '+'
		ADD		R0, R0, R3
		BRz		O_PLUS
		LD		R0, MINUS		; '-'
		ADD		R0, R0, R3
		BRz		O_MINUS
		LD		R0, SOR			; '|'
		ADD		R0, R0, R3
		BRz		O_OR
		LD		R0, L_SHIFT		; '<'
		ADD		R0, R0, R3
		BRz		O_SHIFT
		LD		R0, XORing		; '_'
		ADD		R0, R0, R3
		BRz		O_XOR
		LD		R0, MULT		; '*'
		ADD		R0, R0, R3
		BRz		O_MULT
		LD		R0, MOD			; '%'
		ADD		R0, R0, R3
		BRz		O_MOD

O_PLUS	ADD		R4, R4, #0
		BRnzp	O_end
O_MINUS	ADD		R4, R4, #1
		BRnzp	O_end
O_OR	ADD		R4, R4, #2
		BRnzp	O_end	
O_SHIFT	ADD		R4, R4, #3
		BRnzp	O_end
O_XOR	ADD		R4, R4, #4
		BRnzp	O_end
O_MULT	ADD		R4, R4, #5
		BRnzp	O_end
O_MOD	ADD		R4, R4, #6
		BRnzp	O_end
O_end	ADD		R5, R5, #1

;	
REDO	LDR		R3, R5, #0		; R3 gets character

;
; Test character for end of file
;		
		ADD		R1, R3, #-10	; Test for end of line (ASCII xA)
		BRz		EXIT			; If done, quit
		LD		R1, ZERO
		ADD		R3, R3, R1		; Get the decimal value from ASCII
		JSR		CONV
		ADD		R5, R5, #1
		AND		R1, R5, #1		; check odd/even
		BRp		EVEN
		ADD		R2, R3, #0		; Save the first operand to R2; The second operand is at R3

		ADD		R0, R4, #0
		BRz		P_PLUS
		ADD		R0, R4, #-1
		BRz		P_MINUS
		ADD		R0, R4, #-2
		BRz		P_SOR
		ADD		R0, R4, #-3
		BRz		P_SHIFT
		ADD		R0, R4, #-4
		BRz		P_XOR
		ADD		R0, R4, #-5
		BRz		P_MULT
		ADD		R0, R4, #-6
		BRz		P_MOD
P_PLUS	LD		R0, PLUS		; '+'
		BRnzp	P_end
P_MINUS	LD		R0, MINUS		; '-'
		BRnzp	P_end
P_SOR	LD		R0, SOR			; '|'
		BRnzp	P_end
P_SHIFT	LD		R0, L_SHIFT		; '<'
		BRnzp	P_end
P_XOR	LD		R0, XORing		; '_'
		BRnzp	P_end			
P_MULT	LD		R0, MULT		; '*'
		BRnzp	P_end
P_MOD	LD		R0, MOD			; '%'
		BRnzp	P_end			
P_end	OUT
		BRnzp	REDO
EVEN	LD		R0, EQUAL		; '='
		OUT
		
      
; Start calculation
		ADD		R0, R4, #0
		BRz		C_PLUS
		ADD		R0, R4, #-1
		BRz		C_MINUS
		ADD		R0, R4, #-2
		BRz		C_SOR
		ADD		R0, R4, #-3
		BRz		C_SHIFT		
		ADD		R0, R4, #-4
		BRz		C_XOR
		ADD		R0, R4, #-5
		BRz		C_MULT
		ADD		R0, R4, #-6
		BRz		C_MOD
C_PLUS	JSR		MyADD			; '+'
		BRnzp	C_end
C_MINUS	JSR		MySUB			; '-'
		BRnzp	C_end
C_SOR	JSR		MyOR			; '|'
		BRnzp	C_end
C_SHIFT	JSR		MySHIFT			; '<'
		BRnzp	C_end
C_XOR	JSR		MyXOR			; '_'
		BRnzp	C_end	
C_MULT	JSR		MyMULT			; '*'
		BRnzp	C_end	
C_MOD	JSR		MyMOD			; '%'
		BRnzp	C_end				
;
C_end	JSR		CONV
		AND		R0,	R0,	#0
		ADD		R0,	R0,	#10		; Print a new line
		OUT
		BRnzp	REDO	
		

;
; A subroutine to add the values from R2 and R3 (R2 + R3). The result is saved at R3.
;	
MyADD	
	ADD	R3, R2, R3


		RET
	
	
;
; A subroutine to subtract the value of R3 from R2 (R2 - R3). The result is saved at R3.
;
MySUB	NOT 	R3, R3
	ADD	R3, R3, 1
	ADD     R3, R2, R3
	        RET
;
; A subroutine to OR the values from R2 and R3 (R2 OR R3). The result is saved at R3.
;		
MyOR	NOT	R2, R2
	NOT     R3, R3
        AND     R3, R2, R3
        NOT     R3, R3
		RET
		
		
;		
; A subroutine to calculate the value stored at R2 left-shift by the value stored at R3 (R2 << R3). The result is saved at R3.
;				
MySHIFT ADD R3, R3, #0
	BRz ZZERO
	ADD R0, R2, R2
	ADD R3, R3, #-1
        BRz SDONE
        ADD R2, R0, #0
	BRp MySHIFT
SDONE   ADD R3, R0, #0
	RET
ZZERO   ADD R3, R2, #0
	RET	

;
; A subroutine to XOR the values from R2 and R3 (R2 XOR R3). The result is saved at R3.
;		
MyXOR  
 	AND R0, R2, R3  ; R0 <- A AND B
	NOT R1, R0      ; R1 <- NOT(A AND B)
	NOT R2, R2      ; R2 <- NOT A
	NOT R3, R3      ; R3 <- NOT B
	AND R2, R2, R3  ; R2 <- NOT A AND NOT B
	NOT R2, R2      ; R2 <- NOT(NOT A AND NOT B)
	AND R3, R1, R2  ; R3 <- (NOT(A AND B)) AND (NOT(NOT A AND NOT B))
	RET

; A subroutine to multiply the value from R3 and R2 (R2 * R3). The result is saved at R3.
;
MyMULT	AND	R1, R1, #0
        ADD     R2, R2, #0
        ADD     R3, R3, #0
        ;loop
MULTI   BRnz    EXITL
        ADD     R1, R1, R2
        ADD     R3, R3, #-1

        BRnzp   MULTI
EXITL   ADD     R3, R1, #0  
		RET


;
;A subroutine to divide the value stored at R2 (dividend) with the value stored at R3 (divisor) (R2 % R3). The result (remainder) is saved at R3.
;		
		
MyMOD	

RET
		
		
;
; A subroutine to output a 3-digit decimal result.
;
CONV	ADD		R1, R7, #0		; R3, R4, R5 and R7 are used in this subroutine
		JSR		Push
		ADD		R1, R3, #0		; R3 is the input value
		JSR		Push
		ADD		R1, R4, #0
		JSR		Push
		ADD		R1, R5, #0
		JSR		Push
		AND 	R5, R5, #0
OUT100	LD		R4, HUNDRED
		ADD		R4, R3, R4		; R3 - #100
		BRn		PRI100
		LD		R4, HUNDRED
		ADD		R3, R3, R4		; R3 - #100
		ADD		R5, R5, #1
		BRnzp	OUT100
PRI100	LD		R0, ASCII		; Load the ASCII template
		ADD		R0, R0, R5		; Convert binary count to ASCII
		OUT						; ASCII code in R0 is displayed.
		AND 	R5, R5, #0
OUT10	ADD		R4, R3, #-10
		BRn		PRI10
		ADD		R3, R3, #-10
		ADD		R5, R5, #1
		BRnzp	OUT10
PRI10	LD		R0, ASCII		; Load the ASCII template
		ADD		R0, R0, R5		; Convert binary count to ASCII
		OUT						; ASCII code in R0 is displayed.		
		LD		R0, ASCII
		ADD		R0, R0, R3		; Convert binary count to ASCII
		OUT						; ASCII code in R0 is displayed.
		JSR		Pop
		ADD		R5, R1, #0
		JSR		Pop
		ADD		R4, R1, #0
		JSR		Pop
		ADD		R3, R1, #0
		JSR		Pop
		ADD		R7, R1, #0
		RET
EXIT	HALT					; Halt machine


; Stack operations
Push	STR 	R1, R6, #0		; Stack Push
		ADD 	R6, R6, #-1 
		RET 
Pop 	ADD 	R6, R6, #1		; Stack Pop
		LDR 	R1, R6, #0
		RET
		
; End of the subroutine

SAVEREG1 .FILL x0
SAVEREG2 .FILL x0
SAVEREG3 .FILL x0
SAVEREG4 .FILL x0
SAVEREG5 .FILL x0
SAVEREG6 .FILL x0
SAVEREG7 .FILL x0


PTR	.FILL	x3500
EMPTY 	.FILL 	x4000 
ASCII	.FILL	x0030				; '0'
ZERO	.FILL	xFFD0				; -'0'
HUNDRED	.FILL	xFF9C				; -#100
EQUAL	.FILL	x003D				; '='
PLUS	.FILL	x002B				; '+'
MINUS	.FILL	x002D				; '-'
SOR	.FILL	x007C				; '|'
L_SHIFT	.FILL 	x003C				; '<'
XORing	.FILL	x005F		 	   	; '_'
MULT	.FILL 	x002A				; '*'
MOD	.FILL	x0025				; '%'
VAL	.BLKW	1
	.END


