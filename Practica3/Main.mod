/*********************************************
 * OPL 12.5.1.0 Model
 * Author: adrian.munera
 * Creation Date: 01/10/2018 at 11:08:32
 *********************************************/
main {
var src = new IloOplModelSource("Prueba.mod");
var def = new IloOplModelDefinition(src);
var cplex = new IloCplex();
var model = new IloOplModel(def,cplex);
var data = new IloOplDataSource("Practica3.dat");
model.addDataSource(data);
model.generate();
if (cplex.solve()) {
writeln("Max load " + cplex.getObjValue() + "%");
for (var c=1;c<=model.nCPUs;c++) {
var load=0;
for (var t=1;t<=model.nTasks;t++)
load+=(model.rt[t]* model.x_tc[t][c]);
load = (1/model.rc[c])*load;
if (load<1)
writeln("CPU " + c + " loaded at " + load + "%"+" computer�s processing capacity can be reduced by "+(1-load));
else
writeln("CPU " + c + " loaded at " + load + "%"+" computer�s processing capacity can not be reduced");
}
}
else {
writeln("Not solution found");
}
model.end();
data.end();
def.end();
cplex.end();
src.end();
};