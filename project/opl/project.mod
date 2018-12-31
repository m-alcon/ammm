/*********************************************
 * OPL 12.5.1.0 Model
 * Author: miguel.alcon & roger.pujol
 * Creation Date: 01/10/2018 at 10:21:32
 *********************************************/

int nServices=...;
int nDrivers=...;
int nBuses=...;
int maxBuses=...;
range S=1..nServices;
range D=1..nDrivers;
range B=1..nBuses;
int startingTime [s in S]=...;
int durationTime [s in S]=...;
int durationDist [s in S]=...;
int passangers [s in S]=...;
int capacity [b in B]=...;
int costTime [b in B]=...;
int costDist [b in B]=...;
int maxTime [d in D]=...;
int costBM [d in D]=...;
int costEM [d in D]=...;
int BM [d in D]=...;


dvar boolean x_d[s in S, d in D];
dvar boolean x_b[s in S, b in B];
dvar boolean x_usedb[b in B];
dvar int+ x_timed[d in D];
dvar float+ z;

//for preprocesing
int finalTime[s in S];



//execute{
//for (var s=1; s<= nServices;s++)
//		finalTime[s] = startingTime[s]+durationTime[s]
//
//for (var c=1; c<= nCPUs;c++)
//	for (var k=1; k<=nCores;k++){
//		nC[c]=nC[c]+CK[c][k];
//	}
//}
// Objective
minimize (sum(s in S) sum(b in B) x_b[s,b]*(durationTime[s]*costTime[b] + durationDist[s]*costTime[b])) + 
		 (sum(d in D) (minl(x_timed[d],BM[d])*costBM[d] + maxl(x_timed[d]-BM[d],0)*costEM[d]));
subject to{

	// Constraint 1
	forall(s in S, b in B: passangers[s] > capacity[b])
		x_b[s,b] == 0;
	
	// Constraint 2.b
	forall(s1 in S, b in B) {
		sum(s2 in S: s2 > s1 && (
			// starting time s2 between duration s1
			(startingTime[s1] <= startingTime[s2] && finalTime[s1] >= startingTime[s2]) ||
			// final time s2 between duration s1
			(startingTime[s1] <= finalTime[s2] && finalTime[s1] >= finalTime[s2]) ||
			// duration s1 inside duration s2
			(startingTime[s1] >= startingTime[s2] && finalTime[s1] <= finalTime[s2])
		)) x_b[s2][b] == 1;
 	}			
		
	// Constraint 2.d
	forall(s1 in S, d in D) {
	    sum(s2 in S: s2 > s1 && (
	          // starting time s2 between duration s1
	          (startingTime[s1] <= startingTime[s2] && finalTime[s1] >= startingTime[s2]) ||
	          // final time s2 between duration s1
	          (startingTime[s1] <= finalTime[s2] && finalTime[s1] >= finalTime[s2]) ||
	          // duration s1 inside duration s2
	          (startingTime[s1] >= startingTime[s2] && finalTime[s1] <= finalTime[s2])
	     )) x_d[s2][d] == 1;
	}
	// Constraint 3
	
	forall(d in D)
	 	sum(s in S) durationTime[s]*x_d[s,d] <= maxTime[d];
	 
	 // Constraint 4.1
	 forall(b in B)
	   ceil((sum(s in S) x_b[s,b])/nServices) == x_usedb[b];
	 
	 // Constraint 4.2
	 sum(b in B) x_usedb[b] <= maxBuses;
	   
	 // Final Constraints
	forall(s in S)
	  	sum(b in B) x_b[s,b] == 1;
	
	forall(s in S)
	  	sum(d in D) x_d[s,d] == 1;
	  	
	forall(d in D)
	  	x_timed[d] == sum(s in S) x_d[s,d]*durationTime[s];

}

