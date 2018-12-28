/*********************************************
 * OPL 12.5.1.0 Model
 * Author: miguel.alcon & roger.pujol
 * Creation Date: 01/10/2018 at 10:21:32
 *********************************************/

int nServices=...;
int nDrivers=...;
int nBuses=...;
range S=1..nServices;
range D=1..nDrivers;
range B=1..nBuses;
int staringTime [s in S]=...;
int durationTime [s in S]=...;
int durationDist [s in S]=...;
int passangers [s in S]=...;
int capacity [b in B]=...;
int costTime [b in B]=...;
int costDist [b in B]=...;
int maxTime [d in D]=...;

dvar boolean x_d[s in S, d in D];
dvar boolean x_b[s in S, b in B];
dvar float+ z;

//for preprocesing
int nT[t in T];
int nC[c in C];



execute{
for (var t=1; t<= nTasks;t++)
	for (var th=1; th<=nThreads;th++){
		nT[t]=nT[t]+TH[t][th];
	}

for (var c=1; c<= nCPUs;c++)
	for (var k=1; k<=nCores;k++){
		nC[c]=nC[c]+CK[c][k];
	}
}
// Objective
minimize z;
subject to{

	// Constraint 1
	forall(s in S, b in B: passangers[s] > capacity[b])
	  sum(s in S) sum(b in B) x_b == 0 
	
	// Constraint 2
	forall(t in T, c in C)
		sum(h in H: TH[t][h]==1) sum (k in K: CK[c][k]==1) x_hk[h,k]== nT[t]*x_tc[t,c];

}

// Objective
minimize z;
subject to{
// Constraint 1
forall(h in H)
sum(k in K) x_hk[h,k] == 1;
// Constraint 2
forall(t in T, c in C)
sum(h in H: TH[t][h]==1) sum (k in K: CK[c][k]==1) x_hk[h,k]== nT[t]*x_tc[t,c];
// Constraint 3
forall(c in C,k in K: CK[c][k]==1)
sum(h in H) rh[h]*x_hk[h,k]<=rc[c];
// Constraint 4
forall(c in C)
z >= (1/(nC[c]*rc[c]))*(sum(h in H) sum(k in K: CK[c][k]==1)rh[h]*x_hk[h,k]);
}