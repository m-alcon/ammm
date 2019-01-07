# Usage of our code
## CPLEX (ILP)
In order to use our model you have to open the _IBM ILOG CPLEX Optimization Studio_ and from there open the project found in the folder _opl_.
Once the project is open you have to create a configuration with the _project.mod_ and the instance that you want to solve. Then you only have to run the configuration.
## Meta-HeuristicS
## Instance Generator
To generate all the instances with the current configurations you can run script _run.sh_ (in linux) or _run.bat_ (in windows) from the folder *instance_generator* (these instances will be generated at the folder _opl/instances_). If you want to use a different configuration you can do it by running the command:
`$ python2 Main.py your/config/path`