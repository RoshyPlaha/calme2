Setup with conda w/:
environmental_droplet.yml

Set Python path in root directory (above outbound):
export PYTHONPATH=.

Run test w/ in the root directory of outbound:
python -m unittest


____
Lot of folders here...
Plan for backend is for:
1) chrono to be called with id of request (from db?) and time to set request. This ceates AT job
2) AT job triggers and calls outbound code
3) receiver server receives udp message and needs to call twilio



or using at:
https://linuxize.com/post/at-command-in-linux/

AT commands:
to remove a job - for testing purposes: atrm <job number>
to see a job: at -c <job number>
atq - see pending jobs
execute a script at a given time: at 09:00 -f /home/linuxize/script.sh

https://superuser.com/questions/43678/mac-os-x-at-command-not-working
https://unix.stackexchange.com/questions/478823/making-at-work-on-macos/478840#478840 

