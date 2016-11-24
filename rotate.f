      SUBROUTINE ROTATE (X, Y, CS, SN, N)
      INTEGER N, J
      REAL X(N),Y(N),CS,SN,XX
      DO 10 J=1,N
      XX=X(J)
      X(J)=XX*CS + Y(J)*SN
   10 Y(J)=X(J)*CS - XX*SN
      RETURN
      END
