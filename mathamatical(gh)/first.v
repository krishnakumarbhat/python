module  gtmod(a,b,c,x,y,z,p,q);
input a,b,c;
output x,y,z,p,q;
xor xor1(p,c,b);
nor n1(q,c);
nand nd1(y,a,b);
not and2(x,a,b);
or or1(z,a,b);


endmodule




