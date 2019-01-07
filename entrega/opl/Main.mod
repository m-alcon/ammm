/*********************************************
 * OPL 12.5.1.0 Model
 * Author: miguel.alcon
 * Creation Date: 01/10/2018 at 11:39:05
 *********************************************/

main {
	var src = new IloOplModelSource("p3a.mod");
	var def = new IloOplModelDefinition(src);
	var cplex = new IloCplex();
	var model = new IloOplModel(def,cplex);
	var data = new IloOplDataSource("InstanceGenerator/instances/small_1.dat");
	model.addDataSource(data);
	model.generate();
	cplex.epgap=0.01;
	// cplex.tiLim=1;
	if (cplex.solve()) {
		writeln("Solved");
		writeln(cplex.getBestObjValue());
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