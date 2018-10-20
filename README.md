---
### Skeleton Game - DotNet Mode Generator
---
To generate new files and modes for SkeletonGame

#### Prerequisites

Dotnet runtime needs to be instaled on the system. Windows, Linux, Mac 


#### Install

Run following to install locally:
	
	dotnet new -i skeletongame

#### Usages:

	dotnet new -skelegame --help


##### New Mode Template
*Run from wherever you need the file to be generated.*

The following will create a new **AdvancedMode**. The name is required.

	dotnet new -skelegame -m MyNewMode

##### Extra Options:

Sets Name to "MyNewMode", **Priority** to 69 and the **AdvancedMode** type.

- **Priority = Any integer**
- **AdvancedMode** = [Game, System, Ball, Manual]

---

	
	dotnet new -skelegame -m MyNewMode -p 69 -t Ball



