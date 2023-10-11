# ausführen eines anderen launch files
source /environment.sh

# initialize launch file
dt-launchfile-init #duckie town zeug

# launch subscriber
rosrun my_package my_subscriber_node.py

# wait for app to end
dt-launchfile-join