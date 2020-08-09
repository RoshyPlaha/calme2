Setup with conda w/:
environmental_droplet.yml

Set Python path in root directory (above outbound):
export PYTHONPATH=.

Run test w/ in the root directory of outbound:
python -m unittest


____
Can use message timers -> lambda -> message timers to cycle messages until they are ready?
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html


or using at:
https://linuxize.com/post/at-command-in-linux/

to remove a job - for testing purposes: atrm <job number>
to see a job: at -c <job number>
execute a script at a given time: at 09:00 -f /home/linuxize/script.sh

https://superuser.com/questions/43678/mac-os-x-at-command-not-working
https://unix.stackexchange.com/questions/478823/making-at-work-on-macos/478840#478840