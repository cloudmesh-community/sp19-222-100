BASE PATH:
- /cloudmesh/ai/voting
  - Prefixes all endpoints; for example, `/cloudmesh/ai/voting/run/test/0`.

END POINTS:
- /data/download/\<file\>.csv
  - Downloads the csv data file, named as the argument provided for file.
- /data/show/graph
  - Shows the graph generated from /run/neighbors
- /run/neighbors
  - Runs an analysis that determines the best argument for n_neighbors.
- /run/test
  - Runs an analysis with testing and training sets, also exports a graph.
- /run/custom/\<neighbors\>/\<healthcare\>/\<military\>/\<education\>/\<tax wealthy\>/\<womens rights\>/\<globalism\>/\<gun rights\>/\<infrastructure\>/\<minority rights\>/\<immigration\>
  - Allows user to perform classification with custom arguments.
