/*********************************************
 * OPL 12.5.1.0 Model
 * Author: miguel.alcon
 * Creation Date: 01/10/2018 at 10:31:23
 *********************************************/

int nTasks=...;
int nCPUs=...;
int K=...; //P2a
range T=1..nTasks;
range C=1..nCPUs;
float rt[t in T]=...;
float rc[c in C]=...;
dvar boolean x_tc[t in T, c in C]; //P2
dvar float+ z;

// Preprocessing
execute {
	var totalLoad=0;
	for (var t=1;t<=nTasks;t++)
		totalLoad += rt[t];
	writeln("Total load "+ totalLoad);
	var totalCapacity=0;
	for (var c=1;c<=nCPUs;c++)
		totalCapacity += rc[c];
	if (totalLoad <= totalCapacity)
		writeln("All correct.");
	else
		writeln("Not enough capacity.");
};

// Objective
minimize z;
subject to {
	// Constraint 1
	forall(t in T)
		sum(c in C) x_tc[t,c] <= 1; //P2a
	// Constraint 2
	forall(c in C)
		sum(t in T) rt[t]* x_tc[t,c] <= rc[c];
	// Constraint 3
	forall(c in C)
		z >= (1/rc[c])*sum(t in T) rt[t]* x_tc[t,c];
	// Constraint 4
	sum(c in C)sum(t in T) x_tc[t,c] >= (nTasks-K); //P2a
	
}

// Postprocessing
execute {
	for (var c=1;c<=nCPUs;c++) {
		var load=0;
		for (var t=1;t<=nTasks;t++)
			load+=(rt[t]* x_tc[t][c]);
		load = (1/rc[c])*load;
		writeln("CPU " + c + " loaded at " + load + "%");
	}
};