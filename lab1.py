# NOT gate Implementation using NAND in Python
CHIP Not {
    IN in;
    OUT out;

    PARTS:
    Nand(a=in, b=in, out=out);
}
# OUTPUT:
|in |out|
| 0 | 1 |
| 1 | 0 |

# AND gate Implementation using NAND in Python
CHIP And {
    IN a, b;
    OUT out;
    
    PARTS:
    Nand(a=a , b=b , out=c );
    Nand(a=c , b=c , out=out );
}
#  OUTPUT:
| a | b |out|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

# OR gate Implementation using NAND in Python
CHIP Or {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a , b=a , out=a1 );
    Nand(a=b , b=b , out=b1 );
    Nand(a=a1 , b=b1 , out=out );
}
# OUTPUT:
| a | b |out|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

