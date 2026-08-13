# NOT gate Implementation using NAND in Python
CHIP Not {
    IN in;
    OUT out;

    PARTS:
    Nand(a=in, b=in, out=out);
}

# AND gate Implementation using NAND in Python
CHIP And {
    IN a, b;
    OUT out;
    
    PARTS:
    Nand(a=a , b=b , out=c );
    Nand(a=c , b=c , out=out );
}
# OR gate Implementation using NAND in Python
CHIP Or {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a , b=a , out=a1 );
    Nand(a=b , b=b , out=b1 );
    Nand(a=a1 , b=b1 , out=out );
}