# Change port and possibly the paths
# pwd
folder_name="/mpy_app"
app_dir=$(pwd)
firmware_dir+=$app_dir
firmware_dir+="/bins/firmware.bin"
app_dir+=$folder_name
RED='\033[0;31m'
NC='\033[0m' # No Color
echo -e "${RED}Starting..., remember to press BOOT and hold until it starts to flash";
echo -e "Flashing${NC}";
esptool.py --port /dev/tty.usbserial-0001 erase_flash;
echo -e "${RED}Upload Firmware${NC}";
esptool.py --port /dev/tty.usbserial-0001 write_flash 0x1000 $firmware_dir
echo -e "${RED}Uploading files${NC}";
for entry in $app_dir/*
do
    msg="uploading: "
    msg+="$entry"
    echo "$msg"
    ampy --port /dev/tty.usbserial-0001 put "$entry"
    echo "DONE"
done
echo -e "${RED}Show Screen${NC}";
screen /dev/tty.usbserial-0001 115200;