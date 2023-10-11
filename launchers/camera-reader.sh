# ausführen eines anderen launch files
source /environment.sh

# initialize launch file
dt-launchfile-init

# launch subscriber 
# rosrun <catking-workspace-directory> camera_reader_node.py
# FRAGE catking-workspace-directory ist aber doch nicht my_package
rosrun my_package camera_reader_node.py

# wait for app to end
dt-launchfile-join