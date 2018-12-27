/*********************************************
 * OPL 12.5.1.0 Model
 * Author: marcel.porta
 * Creation Date: 01/10/2018 at 10:31:23
 *********************************************/

int nTasks=...;
int nCPUs=...;
int nThreads=...;
int nCores=...;
range T=1..nTasks;
range C=1..nCPUs;
range K=1..nCores;
range H=1..nThreads;
float rh[h in H]=...;
float rc[c in C]=...;
int CK[c in C,k in K]=...;
int TH[t in T,h in H]=...;
dvar boolean x_tc[t in T, c in C];
dvar boolean x_hk[h in H, k in K];
dvar float+ z;
int n_threads[t in T];
int n_cores[t in T];

// Preprocessing

execute {
	for (var t=1;t <= nTasks ;t ++){
		for (var h =1; h <= nThreads ; h ++){
			n_threads[t] += TH[t][h];
		}
	}
	for (var c=1;c <= nCPUs ;c ++){
		for (var k =1;k <= nCores ; k ++){
			n_cores[c] += CK[c][k];
		}
	}
};


// Objective
minimize z;
subject to{
	// Constraint 1
	forall(h in H)
		sum(k in K) x_hk[h,k] == 1;
		
	// Constraint 2
	forall (t in T ){
		forall (c in C){
			sum (h in H )( sum (k in K ) ( TH[t, h]* CK[c, k]* x_hk[h ,k])) ==	n_threads[t]* x_tc[t, c];
		}
	}
	// Constraint 3
	forall (c in C){
		forall ( k in K ){
			CK[c, k] * sum ( h in H )( rh[h] * x_hk[h][k]) <= rc[c];
		}
	}
	// Constraint 4
	forall (c in C){
		z >= (1/( n_cores[c]* rc[c]))* 
		sum(h in H)
		  ( sum (k in K) CK[c, k]* rh[h]* x_hk[h, k]);
	}
	
}

// Postprocessing
execute {
	for ( var c=1;c <= nCPUs ;c++) {
		var load =0;
		for ( var t=1;t <= nTasks ;t ++){
			for (var h =1;h <= nThreads ; h ++){
				load +=( rh [ h ]* TH [t][ h ]);
			}
		}
		load = (1/ rc [c])* load ;
		writeln ("CPU " + c + " loaded at " + load + "%");
	}
};
