# quick_hash_encrypt


This program quickly generates the hashed / encrypted / encoded output of a given string through multiple algorithms. 
This comes really hand for pentesters while inspecting strange encrypted / encoded / hashed values is encounterd. 

Example:
Password reset token, that comes on mail is hashed using some algorithm. To find out which one, this script will help. 


Currently script generates simple hashes.

###RoadMap:
Generate hashes with common salts (ex. hashed_password = salt(email,password), timestamp as salt, etc.)
Handle more algorithms. 

