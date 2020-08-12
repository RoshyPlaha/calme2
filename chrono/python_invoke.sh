#!/bin/bash
echo "id of users record to find: $1"

# creating file just to know a trigger occured
touch /Users/roshy/Documents/projects/calme2/chrono/rig.txt
echo $1 >> /Users/roshy/Documents/projects/calme2/chrono/rig.txt

# udp call to service to act on data. Using UDP to send message to service on otherside
echo "{\r\n  \"id\": \"$1\",\r\n  \"date\": \"$(date)\"\r\n}" > /dev/udp/127.0.0.1/3000