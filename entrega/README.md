# Usage of our code
## CPLEX (ILP)
In order to **use our model** you have to open the *IBM ILOG CPLEX Optimization Studio* and from there open the project found in the folder *opl/*.
Once the project is open you have to create a configuration with the _opl/project.mod_ and the instance that you want to solve. Then you only have to run the configuration.
## Meta-Heuristics
To use the **meta-heuristic** algorithms on a certain instance, to execute the configurations used in the experiments and to save the logs and the solutions, you can run the script *run.sh* (in Linux, recommended) or *run.bat* (in Windows) found in *meta_heuristics/* folder. In order to select this instance and save consistently the results, you have to modify variables *inputDataFile* and *solutionFile* in each configuration file inside *meta_heuristics/config*. If you run the Linux script, you should also modify the variable *file*.

If you want to execute a self-made instance, you can run the following command:
`$ python3 Main.py your/config/path`

## Instance Generator
In order to **generate all the instances** with the current configurations you can run script *run.sh* (in Linux) or *run.bat* (in Windows) from the folder *instance_generator/* (these instances will be generated at the folder *opl/instances*). If you want to use a different configuration you can do it by running the command:
`$ python2 Main.py your/config/path`