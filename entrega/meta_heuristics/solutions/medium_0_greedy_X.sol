isFeasible = True;
cost = 663.55000000;
x_b = [
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
];
x_d = [
	[ 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 ]
	[ 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ]
	[ 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
];
x_usedb = [
0 0 1 0 1 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 ];
x_timed = [
195 127 146 118 186 239 141 155 0 0 142 147 157 128 0 209 148 80 ];
