chmod 777 /sys/class/gpio/gpio398/value
chmod 777 /sys/class/gpio/gpio389/value
chmod 777 /sys/class/gpio/gpio388/value
chmod 777 /sys/class/gpio/gpio481/value


echo 398  > /sys/class/gpio/export
echo out  > /sys/class/gpio/gpio398/direction

echo 389  > /sys/class/gpio/export
echo out  > /sys/class/gpio/gpio389/direction

echo 388  > /sys/class/gpio/export
echo out  > /sys/class/gpio/gpio388/direction

echo 481  > /sys/class/gpio/export
echo out  > /sys/class/gpio/gpio481/direction

