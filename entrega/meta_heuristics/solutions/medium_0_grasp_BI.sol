isFeasible = True;
cost = 656.18000000;
x_b = [
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
];
x_d = [
	[ 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ]
	[ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ]
	[ 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ]
	[ 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ]
	[ 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 ]
	[ 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ]
	[ 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ]
	[ 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ]
	[ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ]
];
x_usedb = [
0 0 1 0 1 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 ];
x_timed = [
219 162 171 0 107 232 158 197 0 0 145 167 154 149 0 194 118 145 ];