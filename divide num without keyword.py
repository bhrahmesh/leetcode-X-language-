class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0 or divisor==0:
            a=0
        elif dividend>0 and divisor>0:
            a=dividend//divisor
        elif dividend<0 and divisor<0:
          a=abs(dividend)//abs(divisor)
        elif dividend>0 and divisor<1:
            a=-1*(dividend//abs(divisor))
        else:
            a=-1*(abs(dividend)//divisor)
        a=min(max(a,-(2**31)),2**31-1)
        return a
