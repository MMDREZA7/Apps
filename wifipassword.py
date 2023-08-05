import subprocess
import wifipassword


name = (
    subprocess.getoutput("netsh wlan show profile")
    .replace("---------------------------------", "")
    .replace("<None>)", "")
    .replace("User profiles", "")
    .replace("-------------", "")
    .replace("<None>", "")
    .replace("Profiles on interface Wi-Fi", "")
    .replace("Group policy profiles (read only)", "")
    .replace("All User Profile     :", "")
    .replace(":", "")
    .replace("Ryan Heida", "Ryan Heida")
)


name_split = name.split()

print(name)
print(name_split)
# print(name_split)
for i in name_split:
    password = subprocess.getoutput("wifipassword " + i)
    print(password)

input()
